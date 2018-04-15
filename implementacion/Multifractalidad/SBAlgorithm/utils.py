#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 07th April 2018
#Description: This file contains some utilities for multifractality app
import numpy
import snap

def generateFlowerUV():
	

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
	
	#snap.SaveEdgeList(G1, 'mygraph.txt')
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
	Rnd = snap.TRnd(1,0)
	N = graph.GetNodes()
	return snap.GetBfsEffDiam(graph, int(random.uniform(1,N)), False)


#Remove nodes
def removeNodes(graph, DegV,typeRemoval, percent):
	if typeRemoval == 'degree':
		

		N = DegV.Len()
		TotalRemoved = int(N*percent)
			
		for i in range(0, TotalRemoved):
			graph.DelNode(DegV[i].GetVal1())
			
		return graph		
	elif typeRemoval == 'centrality':
		print 1
	else:
		print 'Error: Invalid option'
	return graph
