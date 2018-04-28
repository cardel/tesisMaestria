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
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import BCAlgorithm.BCAlgorithm as BCAlgorithm
import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm

	
def calculateFitness(g, element, radius, distances, listID,listDegree):
	graph = snap.GetMxScc(g)
	
	numNodes = graph.GetNodes()	
	sqrDistance = int(math.sqrt(radius))
	#First position ID node, second position Fitness
	
	#Count nodes to distancie sqrt(N)
	averageDistance = 0.0
	averageDegree = 0.0
	for node in element:		
		#Box of size sqr(N)
		distanceOtherNode = 0.0
				
		for ni in element:
			distanceOtherNode+=distances[int(node)][int(ni)]/radius	
		
		averageDistance += distanceOtherNode/element.size
		averageDegree += listDegree[int(node)]/element.size
	
	maxDegree = max(listDegree)
	if maxDegree == 0:
		maxDegree = 1
	
	if radius == 0:
		radius = 1
		
	fitness = averageDegree/maxDegree + averageDistance/radius
	return fitness
	
#Return neighbors of a specific node
def createNeighbors(node,numNodes, distances):
	neighbors = numpy.array([])
				
	for i in range(0,numNodes):
		if i != node and distances[i][node] == 1:
			neighbors=numpy.append(neighbors,i)
			
	return neighbors

def calculateCenters(graph, numNodes,percentNodes, Kmax, d,distances, listID,listDegree, totalRemoved=0):
	
	numberNodosState = int(percentNodes*numNodes);
	
	if totalRemoved > 0:
		numberNodosState = totalRemoved
	
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
def SA(g,minq,maxq,percentNodes,sizePopulation, Kmax, typeAlgorithm):
	graph = snap.GetMxScc(g)
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		listDegree[index] = ni.GetOutDeg()
		index+=1
		
	rs = rnd.randint(0,numNodes-1)
	
	d = snap.GetBfsFullDiam(graph,int(listID[rs]),False)
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
	centerNodes = calculateCenters(graph, numNodes,percentNodes, Kmax, d,distances, listID,listDegree)


	if typeAlgorithm=='SB':
		groupCenters =[]
		groupCenters.append(centerNodes)
		logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,1,1, centerNodes)	
	elif typeAlgorithm=='BCFS':
		groupCenters = []
		nodes = numpy.arange(numNodes)	
		for i in range(0,100):
			otherNodes = numpy.setdiff1d(nodes, centerNodes)			
			newNodes = numpy.append(centerNodes,otherNodes)
			numpy.random.shuffle(nodes)
			numpy.random.shuffle(centerNodes)
			groupCenters.append(newNodes)
		
		groupCenters = numpy.array(groupCenters)
		logR, Indexzero,Tq, Dq, lnMrq = FSBCAlgorithm.FSBCAlgorithm(g,minq,maxq,1,1, groupCenters)
		
	elif typeAlgorithm=='BC':
		groupCenters = []
		nodes = numpy.arange(numNodes)	
		for i in range(0,100):
			otherNodes = numpy.setdiff1d(nodes, centerNodes)			
			newNodes = numpy.append(centerNodes,otherNodes)
			numpy.random.shuffle(nodes)
			numpy.random.shuffle(centerNodes)
			groupCenters.append(newNodes)
		
		groupCenters = numpy.array(groupCenters)
		logR, Indexzero,Tq, Dq, lnMrq = BCAlgorithm.BCAlgorithm(g,minq,maxq,1,1, groupCenters)
	else:
		print "SimulatedAnnealing: Invalid option of Algorithm"
		sys.exit(0)
			
	return logR, Indexzero,Tq, Dq, lnMrq
