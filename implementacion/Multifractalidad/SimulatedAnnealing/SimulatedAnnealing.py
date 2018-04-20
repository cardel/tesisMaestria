#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 18th April 2018
#Last edition date 18th April 2018
#Description: This algorithm calculates the multifractal dimension with SimulatedAlleaning
import numpy
import math
import random as rnd
from sets import Set
import lib.snap as snap
import utils.utils as utils
	
def calculateFitness(graph, element, radius, distances, listID,listDegree):
	numNodes = graph.GetNodes()	
	sqrDistance = int(math.sqrt(radius))
	#First position ID node, second position Fitness
	
	#Count nodes to distancie sqrt(N)
	averageDistance = 0.0
	averageDegree = 0.0
	#closeNessCentralityNode = 0.0
	#averageCountNodes = 0.0
	for node in element:		
		#Box of size sqr(N)
		distanceOtherNode = 0.0
		#countNodesPerNode = 0.0
			#Distance to other centers
		#for ni in range(0,numNodes):
				#dis = distances[int(node)][ni];
				#if dis <= sqrDistance:
					#countNodesPerNode+=1
					
		for ni in element:
			distanceOtherNode+=distances[int(node)][int(ni)]/radius	
		
		averageDistance += distanceOtherNode/element.size
		#averageCountNodes+=countNodesPerNode/element.size
		#closeNessCentralityNode+=snap.GetClosenessCentr(graph,listID[int(node)])	
		averageDegree += listDegree[int(node)]/element.size
		
	#fitness = averageDistance*averageCountNodes*closeNessCentralityNode
	#fitness = closeNessCentralityNode*averageDistance	
	fitness = averageDegree/max(listDegree) + averageDistance/radius
	return fitness
	
#Return neighbors of a specific node
def createNeighbors(node,numNodes, distances):
	neighbors = numpy.array([])
				
	for i in range(0,numNodes):
		if i != node and distances[i][node] == 1:
			neighbors=numpy.append(neighbors,i)
			
	return neighbors

def calculateCenters(graph, numNodes,percentSandBox, Kmax, d,distances, listID,listDegree):
	
	numberNodosState = int(percentSandBox*numNodes);
	currentState = numpy.random.permutation(numNodes)[0:numberNodosState]
	
	#In graah problems To is a sqrt(nodes)
	for k in range(1,Kmax+1):
		Temperature = float(k)/Kmax
		#Select random node
		r = rnd.randint(0,numberNodosState-1)
		node = currentState[r]
		radius = int(math.sqrt(d))
		#Search neighbors
		neighbors = createNeighbors(node,numNodes,distances)
		
		#Delete neighbors in the solution (We can't get duplicates)
		neighbors = numpy.setdiff1d(neighbors,currentState)
		
		#Newstate
		newState = currentState
		
		#Select random
		if neighbors.size>0:
			r2 = rnd.randint(0,neighbors.size-1)
			newNode = neighbors[r2]
			newState[r] = newNode
			
		
		#Calculate fitness each state
		fitNessCurrentState = calculateFitness(graph, currentState, radius, distances,listID,listDegree)
		fitNessNewState = calculateFitness(graph, newState, radius, distances, listID,listDegree)
	
		difference = fitNessCurrentState - fitNessNewState
		r3 = rnd.random()
		p = math.exp(-difference/Temperature)
		if fitNessNewState > fitNessCurrentState:
			currentState = newState
		elif p < r3:
			currentState = newState
	
	return currentState
	
	
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
#Algorithm Simulated Annealing
def SBSA(graph,minq,maxq,percentSandBox,sizePopulation, Kmax):
	
	d = snap.GetBfsFullDiam(graph,10,False)
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		listDegree[index] = ni.GetOutDeg()
		index+=1

	rangeQ = maxq-minq+1
	#Total q
	lnMrq = numpy.zeros([rangeQ,d],dtype=float)
	
	#Mass Exponents
	Tq = numpy.zeros(rangeQ)
	
	#Generalized dimensions
	Dq = numpy.zeros(rangeQ)
	
	##High computational cost operation
	##I generated a matriz with distancies between nodes
	distances = utils.getDistancesMatrix(graph,numNodes, listID)	
	#Create a random population of nodes	
	centerNodes = calculateCenters(graph, numNodes,percentSandBox, Kmax, d,distances, listID,listDegree)

	numberOfBoxes = int(percentSandBox*numNodes);
	sandBoxes = numpy.zeros([d,numberOfBoxes])
	logR = numpy.array([])
		
	for radius in range(1,d+1):
		
		logR = numpy.append(logR,math.log(float(radius)/d))
		i = 0
		for currentNode in centerNodes:
			countNodes = 1
			#print i, radius
			for ni in range(0, numNodes):
				distance = distances[int(currentNode)][ni]
				if  distance <= radius and distance > 0:
					countNodes+=1
			sandBoxes[radius-1][i] = countNodes
			i+=1
	
	count = 0
	Indexzero  = 0 
	
	for q in range(minq,maxq+1,1):
		i = 0
		for sand in sandBoxes:
			Mr = numpy.power(sand,q-1)
			Mr = numpy.log(numpy.average(Mr))
			lnMrq[count][i]=Mr
			i+=1
			
	
		m,b = utils.linealRegresssion(logR,lnMrq)
		#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
		#Find the mass exponents
		if q == 0: 
			countDim = count;
	

		Tq[count] = m
		
		#Find the Generalizated Fractal dimensions
		if q != 1:
			m,b = utils.linealRegresssion((q-1)*logR,lnMrq[count])
		else:
			Z1e = numpy.array([])
			for sand in sandBoxes:
				Ze = numpy.log(sand)
				Ze = numpy.average(Ze)
				Z1e = numpy.append(Z1e,Ze)
			m,b = utils.linealRegresssion(logR,Z1e)	
		Dq[count] = m
		if q == 0:
			Indexzero = count

		count+=1
	return logR, Indexzero,Tq, Dq, lnMrq
