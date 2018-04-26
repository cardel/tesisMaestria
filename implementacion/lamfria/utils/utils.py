#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 07th April 2018
#Description: This file contains some utilities for multifractality app
import numpy
import random as rnd
import os.path
import lib.snap as snap

#Get distances matrix
#Reduce high computational cost operation
def getDistancesMatrix(graph,numNodes,listID):
	#Due to ID nodes are not contiguous, I use the array with relation beetween index of array and ID node (listaID)
	distances = numpy.zeros([numNodes,numNodes])
	for i in range(0, numNodes):
		for j in range(0, numNodes):
			#Same node
			if i == j:				
				distances[i][j] = 0
			else:
				dis = snap.GetShortPath(graph,listID[i],listID[j]);
				distances[i][j] = dis
	
	return distances
	
#Get adjacence pathMatrix
#Reduce high computational cost operation
def getAdjacenceMatriz(distances, numNodes):
	#Due to ID nodes are not contiguous, I use the array with relation beetween index of array and ID node (listaID)
	adjMatrix = numpy.zeros([numNodes,numNodes])
	for i in range(0, numNodes):
		for j in range(0, numNodes):
			#Same node
			if distances[i][j]==1:		
				adjMatrix[i][j] = 1
			else:
				adjMatrix[i][j] = 0
	
	return distances


	
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

# Get average path lenght in the giant component
def getAveragePathLength(graph):
	g = snap.GetMxScc(graph)
	NumNodes = g.GetNodes()	
	average = 0.
	maxDistance = 0.
	for ni in g.Nodes():
		for nj in g.Nodes():
			dist = snap.GetShortPath(g,ni.GetId(),nj.GetId())
			average+=dist
			if dist > maxDistance:
				maxDistance = dist
			
	average=average/(2.*NumNodes)		
			
	return float(average)/maxDistance
#Copy a graph

def copyGraph(graph):
	g = snap.TUNGraph.New()
	for NI in graph.Nodes():
		g.AddNode(NI.GetId())
	
	for EI in graph.Edges():
		g.AddEdge(EI.GetSrcNId(),EI.GetDstNId())
		
	return g
	
#Remove nodes
def removeNodes(graph,typeRemoval, percent, p, N,ClosenessCentrality, typeMeasure,listID):
	TotalRemoved = int(N*percent)
	measure = 0.
	if typeRemoval == 'degree':		
		for i in range(0, TotalRemoved):
			node = snap.GetMxDegNId(graph)
			graph.DelNode(node)				
	elif typeRemoval == 'centrality':
		startNode = int((p-0.1)*N)
		endNode = int(p*N)
		for i in range(startNode, endNode):
			graph.DelNode(int(ClosenessCentrality[i][0]))				
				
	elif typeRemoval == 'random':
		Rnd = snap.TRnd(int(N))
		
		for i in range(0, TotalRemoved):
			Rnd.Randomize()
			node = graph.GetRndNId(Rnd)
			graph.DelNode(node)	
	else:
		print 'Error: Invalid option'
		
	if typeMeasure=='GC':
		measure = float(getSizeOfGiantComponent(graph))/N
	elif typeMeasure=='APL':
		measure = float(getAveragePathLength(graph))
		
	return measure

def removeNodesGenetic(graph,nodesToRemove, N,listID, typeMeasure):
	measure = 0.

	for node in nodesToRemove:
		ni = listID[int(node)]
		graph.DelNode(ni)
	if typeMeasure=='GC':
		measure = float(getSizeOfGiantComponent(graph))/N
	elif typeMeasure=='APL':
		measure=float(getAveragePathLength(graph))		
	return measure
