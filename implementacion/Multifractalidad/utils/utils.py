#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 07th April 2018
#Description: This file contains some utilities for multifractality app
import numpy
import random
import os.path
import lib.snap as snap

#Get distances matrix
#Reduce high computational cost operation
def getDistancesMatrix(graph,numNodes,listID):
	#Due to ID nodes are not contiguous, I use the array with relation beetween index of array and ID node (listaID)
	distances = numpy.zeros([numNodes,numNodes])
	for i in range(0, numNodes):
		for j in range(i, numNodes):
			#Same node
			if i == j:				
				distances[i][j] = 0
				distances[j][i] = 0
			else:
				dis = snap.GetShortPath(graph,listID[i],listID[j]);
				distances[i][j] = dis
				distances[j][i] = dis
	
	return distances

#Generate fractal network (u,v)->flower with u = 2 and v = 2
def generateFlowerUV():
	
	G1 = snap.TUNGraph.New()
	
	if os.path.isfile('../../datos/flower.txt'):
		G1 = snap.LoadEdgeList(snap.PUNGraph, '../../datos/flower.txt', 0, 1)
	else:
		#First generation
		a = numpy.array([[0,1],[1,0]])
		for generation in range(2,8):
			
			rows = a.shape[0]
			cols = a.shape[1]
			currentIndex = rows
			for i in range(0, rows):
				for j in range(i, cols):
					#Per each edge we add two vertices and four edges
					if a[i][j] == 1:
						#Add two vertex to Graph
						#Add two rows
						a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
						a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
						#Add two columns
						a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
						a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
						
						#Delete current edge
						a[i][j] = 0
						a[j][i] = 0
						
						#Add four edges for two vertex
						a[i][currentIndex] = 1
						a[i][currentIndex+1] = 1
						a[currentIndex][j] = 1
						a[currentIndex+1][j] = 1
						
						#Due to the graph is indirect, we must to put 1 in simetric places
						a[currentIndex][i] = 1
						a[currentIndex+1][i] = 1
						a[j][currentIndex] = 1
						a[j][currentIndex+1] = 1
						
						#Our matrix
						currentIndex+=2
		
		
		size = a.shape[0]
		G1 = snap.TUNGraph.New()
		#numpy.savetxt("grafo.csv",a,"%i",delimiter=",")
		#Add nodes
		for i in range(0,size):
			G1.AddNode(i)
		#Add edges
		for i in range(0,size):
			for j in range(i, size):
				if(a[i][j]==1):
					G1.AddEdge(i,j)
		
		snap.SaveEdgeList(G1, '../../datos/flower.txt')
	return G1
	
#Lineal regression for calculte derivatives
def linealRegresssion(x, y):

	m = 0
	b = 0
	n = numpy.size(x)
	sumXplusY = numpy.sum(x*y)
	sumXplusX = numpy.sum(x*x)
	sumX = numpy.sum(x)
	sumY = numpy.sum(y)
	m = (n*sumXplusY - sumX*sumY)/(n*sumXplusX-sumX*sumX)
	b = (sumY - m*sumX)/n
	
	
	return m,b
	
#Get size giant component
def getSizeOfGiantComponent(graph):
	Component = snap.GetMxScc(graph)
	return Component.GetNodes()

# Get average path lenght
def getAveragePathLength(graph):
	N = graph.GetNodes()
	return snap.GetBfsEffDiam(graph, int(random.uniform(1,N)), False)

#Copy a graph

def copyGraph(graph):
	g = snap.TUNGraph.New()
	for NI in graph.Nodes():
		g.AddNode(NI.GetId())
	
	for EI in graph.Edges():
		g.AddEdge(EI.GetSrcNId(),EI.GetDstNId())
		
	return g
	
#Remove nodes
def removeNodes(graph,typeRemoval, percent, p, N,ClosenessCentrality, typeMeasure):
	TotalRemoved = int(N*percent)
	measure = numpy.array([],dtype=float)
	if typeRemoval == 'degree':		
		for i in range(0, TotalRemoved):
			node = snap.GetMxDegNId(graph)
			graph.DelNode(node)	
			if typeMeasure=='GC':
				measure = numpy.append(measure,float(getSizeOfGiantComponent(graph))/N)
			elif typeMeasure=='APL':
				measure = numpy.append(measure,float(getAveragePathLength(graph)))
			
	elif typeRemoval == 'centrality':
		startNode = int((p-0.1)*N)
		endNode = int(p*N)
		for i in range(startNode, endNode):
			graph.DelNode(int(ClosenessCentrality[i][0]))				
			if typeMeasure=='GC':
				measure = numpy.append(measure,float(getSizeOfGiantComponent(graph))/N)
			elif typeMeasure=='APL':
				measure = numpy.append(measure,float(getAveragePathLength(graph)))
						
	elif typeRemoval == 'random':
		Rnd = snap.TRnd(int(N))
		
		for i in range(0, TotalRemoved):
			Rnd.Randomize()
			node = graph.GetRndNId(Rnd)
			graph.DelNode(node)	
			if typeMeasure=='GC':
				measure = numpy.append(measure,float(getSizeOfGiantComponent(graph))/N)
			elif typeMeasure=='APL':
				measure = numpy.append(measure,float(getAveragePathLength(graph)))
	else:
		print 'Error: Invalid option'
	
	return measure

def removeNodesGenetic(graph,nodesToRemove, N,listID, typeMeasure):
	measure = numpy.array([],dtype=float)

	for node in nodesToRemove:
		ni = listID[int(node)]
		graph.DelNode(ni)
		if typeMeasure=='GC':
			measure = numpy.append(measure,float(getSizeOfGiantComponent(graph))/N)
			measure = 0
		elif typeMeasure=='APL':
			measure = numpy.append(measure,float(getAveragePathLength(graph)))	
			measure = 0	
	
	return measure
