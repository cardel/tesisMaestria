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
def FSBCAlgorithm(g,minq,maxq,percentNodesT, centerNodes = numpy.array([])):
	
	#graph = 
	graph =snap.GetMxScc(g)
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
	d = snap.GetBfsFullDiam(graph,1,False)+1
	rangeQ = maxq-minq+1

	#Calculate loge = logR/d
	logR = numpy.array([])
	for radius in range(1,d+1):
		logR = numpy.append(logR,math.log(float(radius)/d))
		
	#Index of Tq[0]
	Indexzero = 0
	#Generate T random sequences
	#According to the number of nodes in the network, set t = 1, 2, . . . ,T appropriately. Group the nodes into T different ordered random sequences. More specifically, in each sequence, nodes which will be chosen as a seed or center of a box are randomly arrayed
	
	RandomSequences = centerNodes
	
	if(numpy.size(centerNodes)==0):
	
		RandomSequences = numpy.empty([T,numNodes])
		randomN = numpy.arange(0,numNodes)
		
		for i in range(0,T):
			numpy.random.shuffle(randomN)
			RandomSequences[i] = randomN
			
	#Total boxes content all boxes for T repetitions
	totalBoxes = []		
	#We take T repetitions
	#Mass Exponents
	Tq = numpy.zeros([rangeQ])
	
	#Generalized dimensions
	Dq = numpy.zeros([rangeQ])
	
	#Total q
	lnMrq = numpy.zeros([rangeQ,d],dtype=float)		
	for randomSequence in RandomSequences:
		#I select 40 percent of nodes
		#sandBoxes = numpy.zeros([d,numberOfBoxes])	
		BoxesRadio = []
		
		for radius in range(1,d+1):		
			nodesMark = numpy.zeros([numNodes])	
			RBoxes = numpy.array([],dtype=float)	
			#All nodes in gigaint component have to covered	
			for i in range(0, numNodes):				
				currentNode = randomSequence[i]
				box = numpy.array([currentNode], dtype=int)					
				
				if nodesMark[int(currentNode)]==0:
					countNodes = 0.
					for ni in range(0, numNodes):		
						if nodesMark[ni] == 0:				
							distance = Bnxn[int(currentNode)][ni]						
							if  distance <= radius:
								countNodes+=1
								box=numpy.append(box,ni)
						
					if countNodes>0:
						RBoxes = numpy.append(RBoxes,countNodes/numNodes)
						nodesMark[box] = 1			
			BoxesRadio.append(RBoxes)
		totalBoxes.append(BoxesRadio)	
	
	Boxes =[]
	boxA = 0
	for q in range(minq,maxq+1,1):
		Zrq = []
		for TBoxes in totalBoxes:
			BoxesQ = numpy.array([])
			for RBoxes in TBoxes:
				BoxesQ= numpy.append(BoxesQ,(numpy.sum(numpy.power(RBoxes,q))))
			Zrq.append(BoxesQ)
		Zrq = numpy.average(Zrq, axis=0)
		Boxes.append(Zrq)
	
	Boxes = numpy.array(Boxes)	
	#Index of q
	boxC = 0
	Zre = []
	for TBoxes in totalBoxes:
		boxC += 1
		BoxesLN = numpy.array([])
		for RBoxes in TBoxes:	
			BoxesLN= numpy.append(BoxesLN,(numpy.sum(RBoxes*numpy.log(RBoxes))))
		Zre.append(BoxesLN)
			
	Zre = numpy.array(Zre)
	Zre = numpy.average(Zre, axis=0)


	count = 0
	Indexzero  = 0 
	

	for q in range(minq,maxq+1,1):
		i = 0
		box = Boxes[count]
		lnMrq[count]= numpy.log(box)	
		m,b = utils.linealRegresssion(logR,lnMrq[count])
		#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
		#Find the mass exponents
		if q == 0: 
			countDim = count;		

		Tq[count] = m
		#Find the Generalizated Fractal dimensions
		if q != 1:
			m,b = utils.linealRegresssion(logR,lnMrq[count]/(q-1))
		else:	
			m,b = utils.linealRegresssion(logR,Zre)	
		Dq[count] = m
		if q == 0:
			Indexzero = count
		count+=1
		
	return logR, Indexzero,Tq, Dq,lnMrq

