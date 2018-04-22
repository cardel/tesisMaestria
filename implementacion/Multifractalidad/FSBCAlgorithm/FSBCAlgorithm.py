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
	T = int(float(numNodes)*percentNodesT)
	
	#Set the size of the box in the range r ∈ [1, d ],where d is the diameter of the network.
	d = snap.GetBfsFullDiam(graph,10,False)
	
	rangeQ = maxq-minq+1
	
	#Mass Exponents
	Tq = numpy.zeros([rangeQ])
	
	#Generalized dimensions
	Dq = numpy.zeros([rangeQ])
	
	#Total q
	lnMrq = numpy.zeros([rangeQ,d],dtype=float)
	
	#Calculate loge = logR/d
	logR = numpy.array([])
	for radius in range(1,d+1):
		logR = numpy.append(logR,math.log(float(radius)/d))
		
	#Index of Tq[0]
	Indexzero = 0
	#Generate T random sequences
	#According to the number of nodes in the network, set t = 1, 2, . . . ,T appropriately. Group the nodes into T different ordered random sequences. More specifically, in each sequence, nodes which will be chosen as a seed or center of a box are randomly arrayed
	RandomSequences = numpy.empty([T,numNodes])
	
	for i in range(0,T):
		RandomSequences[i] = numpy.random.permutation(numNodes)	
		
	#Total boxes content all boxes for T repetitions
	totalBoxes = []		
	#We take T repetitions
	
	for randomSequence in RandomSequences:
		#I select 40 percent of nodes
		
		#sandBoxes = numpy.zeros([d,numberOfBoxes])	
		BoxesRadio = []
		
		for radius in range(1,d+1):		
			nodesMark = numpy.zeros([numNodes])	
			RBoxes = numpy.array([],dtype=float)
			#Iterate each center in permutatio
			radiusCovered = numpy.zeros([radius])
			for i in range(0, numNodes):	
				
				currentNode = randomSequence[i]
				box = numpy.array([currentNode], dtype=int)				
				countNodes = 0.
				
				if nodesMark[int(currentNode)]==0:
					for ni in range(0, numNodes):
						
						distance = Bnxn[int(currentNode)][ni]
						
						if  distance <= radius and distance > 0:
							countNodes+=1
							radiusCovered[int(distance)-1]=1
							box=numpy.append(box,ni)
						
					if numpy.prod(radiusCovered)==1:
						RBoxes = numpy.append(RBoxes,countNodes)
						nodesMark[box] = 1	
			BoxesRadio.append(RBoxes)
		totalBoxes.append(BoxesRadio)
		
	Boxes = []
	for q in range(minq,maxq+1,1):
		Zrq = []
		for TBoxes in totalBoxes:
			BoxesQ = numpy.array([])
			for RBoxes in TBoxes:
				#Q-1 is equivalente to divide to M(0)
				BoxesQ= numpy.append(BoxesQ,(numpy.average(numpy.power(RBoxes,q-1)))/numNodes)
			Zrq.append(BoxesQ)
		
		Zrq=numpy.array(Zrq)
		Boxes.append(Zrq)
		
	Boxes = numpy.array(Boxes)
	#Index of q
	Zre = []
	for TBoxes in totalBoxes:
		BoxesLN = numpy.array([])
		for RBoxes in TBoxes:			
			BoxesLN= numpy.append(BoxesLN,(numpy.average(numpy.log(RBoxes))))
		Zre.append(BoxesLN)
	count = 0
	Indexzero  = 0 
		
	for q in range(minq,maxq+1,1):
		i = 0
		box = numpy.average(Boxes[count],axis=0)
		lnMrq[count]= numpy.log(box)
	
		
		m,b = utils.linealRegresssion(logR,lnMrq[count])
		#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
		#Find the mass exponents
		if q == 0: 
			countDim = count;		

		Tq[count] = m
		
		#Find the Generalizated Fractal dimensions
		if q != 1:
			m,b = utils.linealRegresssion((q-1)*logR,lnMrq[count])
		else:	
			Ze = numpy.average(Zre, axis=0)
			m,b = utils.linealRegresssion(logR,Ze)	
		Dq[count] = m
		if q == 0:
			Indexzero = count

		count+=1

	return logR, Indexzero,Tq, Dq,lnMrq

