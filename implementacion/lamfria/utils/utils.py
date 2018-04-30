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
import sys

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
	
	#Test nodes are 40 percent of numNodes
	
	numNodes = graph.GetNodes()
	
	testNodes = int(float(numNodes)*0.4)	
	if testNodes == 0: testNodes = 1
	
	meanAverage = snap.GetBfsEffDiam(graph, testNodes, False)					
	return meanAverage
#Copy a graph

def copyGraph(graph):
	g = snap.TUNGraph.New()
	for NI in graph.Nodes():
		g.AddNode(NI.GetId())
	
	for EI in graph.Edges():
		g.AddEdge(EI.GetSrcNId(),EI.GetDstNId())
		
	return g
	
#Get ordered closeness Centrality with node ID

def getOrderedClosenessCentrality(graph,N):
	g = snap.GetMxScc(graph)
	ClosenessCentrality = numpy.empty([N,2], dtype=float)
	index=0
	for NI in g.Nodes():
		ClosenessCentrality[index][0]=NI.GetId()
		ClosenessCentrality[index][1]=snap.GetClosenessCentr(graph,NI.GetId())
		index+=1
		
	ClosenessCentrality = ClosenessCentrality[ClosenessCentrality[:,1].argsort()]
	return ClosenessCentrality
	
#Remove nodes
def removeNodes(graph,typeRemoval, p, numberNodesToRemove, ClosenessCentrality, listID, nodesToRemove = numpy.array([])):
	TotalRemoved = numberNodesToRemove
	measureGC = 0.
	measureAPL = 0.
	numNodes = graph.GetNodes()
	
	if typeRemoval == 'Degree':		
		for i in range(0, TotalRemoved):
			node = snap.GetMxDegNId(graph)
			graph.DelNode(node)	
						
	elif typeRemoval == 'Centrality':
		nodesToErase = snap.TIntV()
		for i in range(0, TotalRemoved):
			nodesToErase.Add(ClosenessCentrality[i][0])				
			
		snap.DelNodes(graph,nodesToErase)	
			
	elif typeRemoval == 'Random':		
		
		nodesToRemoveRandom=numpy.array([listID[rnd.randint(0, numNodes-1)]],dtype=int)
		
		while(numpy.size(nodesToRemoveRandom)<TotalRemoved):
			Rnd = rnd.randint(0, numNodes-1)
			nodesToRemoveRandom = numpy.unique(numpy.append(nodesToRemoveRandom, listID[int(Rnd)]))
		
		nodesToErase = snap.TIntV()
		for i in range(0, TotalRemoved):
			nodesToErase.Add(nodesToRemoveRandom[i])
		
		snap.DelNodes(graph,nodesToErase)	
			
	elif typeRemoval ==  'Genetic' or typeRemoval == 'Simulated':
		
		nodesToErase = snap.TIntV()
		for i in range(0, TotalRemoved):
			nodesToErase.Add(listID[int(nodesToRemove[i])])
						
		snap.DelNodes(graph,nodesToErase)	
		
	else:
		print 'Error: Invalid option of robustness attack'
		sys.exit(0)
		
	measureGC = float(getSizeOfGiantComponent(graph))
	measureAPL = float(getAveragePathLength(graph))
		
	return measureGC,measureAPL

