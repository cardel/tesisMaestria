#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 20th March 2018
#Last edition date 20th April 2018
#Description: This algorithm calculates the multifractal dimension with box counting fixed size
import numpy
import math
import lib.snap as snap
import utils.utils as utils
#Proceed
def FSBCAlgorithm(graph,minq,maxq,percentNodesT,repetitions):
	
	
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		index+=1

	#First: calculate shorstest path among all linked pairs into another matriz Bnxn
	Bnxn = utils.getDistancesMatrix(graph,numNodes,listID)
	#Second: Adjacence matrix Anxn
	Anxn = utils.getAdjacenceMatriz(Bnxn, numNodes)
	
	#According to the number of nodes in the network, set t = 1, 2, . . . ,T appropriately
	T = int(numNodes*percentNodesT)
	
	#Set the size of the box in the range r ∈ [1, d ],where d is the diameter of the network.
	d = snap.GetBfsFullDiam(graph,10,False)
	
	rangeQ = maxq-minq+1
	
	#Mass Exponents
	Tq = numpy.zeros([repetitions,rangeQ])
	
	#Generalized dimensions
	Dq = numpy.zeros([repetitions,rangeQ])
	
	#LnrqTotal
	lnZATotal = numpy.zeros([rangeQ,d],dtype=float)	
	
	#Calculate loge = logR/d
	logR = numpy.array([])
	for radius in range(1,d+1):
		logR = numpy.append(logR,math.log(float(radius)/d))
		
	#Index of Tq[0]
	Indexzero = 0
	
	#We take T repetitions
	for r in range(0,repetitions):
		
		
		#Generate T random sequences
		#According to the number of nodes in the network, set t = 1, 2, . . . ,T appropriately. Group the nodes into T different ordered random sequences. More specifically, in each sequence, nodes which will be chosen as a seed or center of a box are randomly arrayed
		RandomSequences = numpy.empty([T,numNodes])
		
		for i in range(0,T):
			RandomSequences[i] = numpy.random.permutation(numNodes)
			
		
		ZqAverage = []
		#For q = 1
		Z1eAverage = []
		#Generate boxes with random centers
		for randomCenters in RandomSequences:
			Ub = []			
			
			#Count nodes in each box
			for radius in range(1,d+1):
			#Select a node in randomlist		
				#Initially, all the nodes in the network are marked as uncovered and no node has been chosen as a seed or center of a box
				#0 is not marked, other value marked		
				boxes = numpy.array([])
				nodesMark = numpy.zeros(numNodes)				
				
				for center in randomCenters:				
					countNodes = 1.0
					#Mark center
					nodesMark[int(center)]=1
					#Count number of nodes per box
					for ni in range(0, numNodes):
						if nodesMark[ni]==0:
							distance = Bnxn[int(center)][ni]
							if  distance <= radius:
								countNodes+=1						
								nodesMark[ni]=1
					
						#Add non-empty boxes
					if countNodes > 0:	
						boxes = numpy.append(boxes,countNodes/numNodes)
					#If all nodes are marked visited, we stop the search of boxes				
				Ub.append(boxes)
				

			#Calculate partition sum
			Zq = []
			Z1e = []
			for q in range(minq,maxq+1,1):
				#For each r in (0, d)
				Zrq = []
				for ubr in Ub:
					ubQ = numpy.power(ubr,q)
					ubQ = numpy.sum(ubQ)
					Zrq.append(ubQ)
				Zq.append(Zrq)

			ZqAverage.append(Zq)

			#Z1e
			for ubr in Ub:
				ubQ = ubr*numpy.log(ubr)
				ubQ = numpy.sum(ubQ)
				Z1e.append(ubQ)
			Z1eAverage.append(Z1e)

		ZqAverage = numpy.mean(ZqAverage,axis=0)

		lnZqA = numpy.log(ZqAverage)
		lnZATotal+=numpy.log(ZqAverage)

		Z1eAverage = numpy.mean(Z1eAverage,axis=0)
		##I take average of T
		
		count = 0
		for q in range(minq,maxq+1,1):
			m,b = utils.linealRegresssion(logR,lnZqA[count])
			
			###Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
			###Find the mass exponents
			if q == 0: 
				countDim = count;		

			Tq[r][count] = m
		 
			###Find the Generalizated Fractal dimensions
			if q != 1:
				m,b = utils.linealRegresssion(logR,lnZqA[count]/(q-1))
			else:
				m,b = utils.linealRegresssion(logR,Z1eAverage)	
			
			Dq[r][count] = m

			if q == 0:
				Indexzero = count
				
			count+=1
	lnZATotal = lnZATotal/repetitions
	TqA = numpy.mean(Tq,axis=0)
	DqA = numpy.mean(Dq,axis=0)
	return logR, Indexzero,TqA, DqA,lnZATotal
