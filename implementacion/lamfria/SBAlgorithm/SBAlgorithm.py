#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th April 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import numpy
import math
from sets import Set
import lib.snap as snap
import utils.utils as utils
import random

#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBAlgorithm(g,minq,maxq,percentSandBox,repetitions, centerNodes = numpy.array([])):
	"""Calculate fractal dimension with SandBox method

	Inputs are parameters to configure algorithm behaviour.

	:param g: Network.
	:type g: Snap PUN Graph.
	:param minq: Minimum value of q
	:type args: Integer
	:param minq: Maximum value of q
	:type maxq: Integer	
	:param percentSandBox: Number of combinations of center nodes. This value is a percent of the total nodes
	:type percentSandBox: Double
	:param repetitions: Number of repetitions of algorithm
	:type repetitions: Integer		
	:param CenterNodes: Calculated center. If this is null, then the centers are calculated
	:type CenterNodes: Numpy 1D Array	
	:returns:				
		logR: Numpy array
			logarithm of r/d
		Indexzero: Integer
			position of q=0 in Tq and Dq
		Tq: Numpy array
			mass exponents		
		Dq: Numpy array
			fractal dimensions		
		lnMrq: Numpy 2D array
			logarithm of number of nodes in boxes by radio
		"""	
	graph = g

	#if(numpy.size(centerNodes)==0):
	#	graph = snap.GetMxScc(g)	
	numNodes = graph.GetNodes()

	listID = snap.TIntV(numNodes)
	
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		index+=1
		
	#select random node
	
	d = snap.GetBfsFullDiam(graph,100,False)
	rangeQ = maxq-minq+1	
	#Mass Exponents
	Tq = numpy.zeros([repetitions,rangeQ])
	
	#Generalized dimensions
	Dq = numpy.zeros([repetitions,rangeQ])
	
	#Calculate loge = logR/d
	logR = numpy.array([])
	for radius in range(1,d+1):
		logR = numpy.append(logR,math.log(float(radius)/d))
	
	#LnrqTotal
	lnMrqTotal = numpy.zeros([rangeQ,d],dtype=float)	
	
	#Index of Tq[0]
	Indexzero = 0
	
	#I generated a matriz with distances between nodes
	distances = utils.getDistancesMatrix(graph, numNodes,listID)

	#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.

	for r in range(0,repetitions):
		#Total q
		lnMrq = numpy.zeros([rangeQ,d],dtype=float)
		
		numberOfBoxes = int(percentSandBox*numNodes);
		randomNodes = centerNodes
		#I select a percent of nodes
		if(numpy.size(centerNodes)==0):
			randomNodes = numpy.random.permutation(numNodes)[0:numberOfBoxes]		
		sandBoxes = []
		
		for radius in range(1,d+1):		
			sand = []
			for i in range(0, numpy.size(randomNodes)):
				currentNode = int(randomNodes[i])
				countNodes = 0.
				for ni in range(0, numNodes):
					distance = distances[currentNode][ni];
					if  distance <= radius:
						countNodes+=1				
				sand.append(countNodes)			
			sandBoxes.append(sand)
		

		#Index of q
		count = 0
		Indexzero  = 0 
		
		for q in range(minq,maxq+1,1):
			i = 0
			for sand in sandBoxes:
				Mr = numpy.power(sand,q-1)
				Mr = numpy.log(numpy.average(Mr))
				lnMrq[count][i]=Mr
				lnMrqTotal[count][i]+=Mr
				i+=1				
			
			m,b = utils.linealRegresssion(logR,lnMrq[count])

			#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
			#Find the mass exponents
			if q == 0: 
				countDim = count;		

			Tq[r][count] = m
			
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
			Dq[r][count] = m

			if q == 0:
				Indexzero = count
			
			count+=1
	
	lnMrqTotalA = lnMrqTotal/repetitions
	TqA = numpy.mean(Tq,axis=0)
	DqA = numpy.mean(Dq,axis=0)

	return logR, Indexzero,TqA, DqA,lnMrqTotalA
