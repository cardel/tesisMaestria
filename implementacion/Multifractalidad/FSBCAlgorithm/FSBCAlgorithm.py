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



	#Firsrt: calculate shorstest path among all linked pairs into another matriz Bnxn
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
	lnMrqTotal = numpy.zeros([rangeQ,d+1],dtype=float)	
	
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
			
		#Generate boxes with random centers
		ZqrMT = []
		for randomCenters in RandomSequences:
			Zrq = []			

			for radius in range(1,d+1):
			#Select a node in randomlist		
				#Initially, all the nodes in the network are marked as uncovered and no node has been chosen as a seed or center of a box
				#0 is not marked, other value marked		
				boxes = numpy.array([])
				nodesMark = numpy.zeros(numNodes)				
				
				for center in randomCenters:				
					countNodes = 0.0
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
					if numpy.prod(nodesMark) == 1:
						break		
				
				Zrq.append(boxes)
			ZqrMT.append(Zrq)
			
		print ZqrMT
		return
			#Radius = d only a box with size numNodes	
		#if true:	
			#Indexzero  = 0 
			##Actual secuence
			#qValor = 0			
			#for q in range(minq,maxq+1,1):
				#radius = 0	
				##Each box it is a radio	
				#ZqrM = numpy.array([])	
				#for box in Zrq:
					#Mr = numpy.power(box,q)
					#ZqrM = numpy.append(ZqrM,numpy.sum(Mr))
					##lnMrq[qValor][radius]+=numpy.average(Mr)
					##lnMrqTotal[qValor][radius]+=numpy.average(Mr)
					##radius+=1					
				#qValor+=1
				#ZqrMT.append(ZqrM)
		
		#print ZqrMT
		#return
		##Calculate average
		#lnMrq = numpy.zeros([rangeQ,d],dtype=float)
		#index = 0
		#for zq in ZqrMT:
			#lnMrq[index] = numpy.log(zq)
			#index+=1
		
		#print lnMrq
		#return	
			

		##I take average of T
		#lnMrq = numpy.log(lnMrq/T)
		
		#count = 0
		#for q in range(minq,maxq+1,1):
			#m,b = utils.linealRegresssion(logR,lnMrq[count])
			###Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
			###Find the mass exponents
			#if q == 0: 
				#countDim = count;		

			#Tq[r][count] = m
		 
			###Find the Generalizated Fractal dimensions
			#if q != 1:
				#m,b = utils.linealRegresssion((q-1)*logR,lnMrq[count])
			#else:
				#Z1e = numpy.array([])
				#for box in Zrq:
					#Ze = numpy.log(box)
					#Ze = numpy.average(Ze)
					#Z1e = numpy.append(Z1e,Ze)
				#m,b = utils.linealRegresssion(logR,Z1e)	
				
			#Dq[r][count] = m
			
			#if q == 0:
				#Indexzero = count
				
			#count+=1
			
	#lnMrqTotal =  numpy.log(lnMrqTotal/(T*repetitions))
	#TqA = numpy.mean(Tq,axis=0)
	#DqA = numpy.mean(Dq,axis=0)
	#return logR, Indexzero,TqA, DqA,lnMrqTotal
