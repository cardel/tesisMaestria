#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th April 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import snap
import numpy
import math
from sets import Set
import utils
		
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBAlgorithm(grafo,minq,maxq,percentSandBox):
	
	d = snap.GetBfsFullDiam(grafo,10,False)
	numNodes = grafo.GetNodes()
	
	listID = snap.TIntV(numNodes)
	
	index = 0
	for ni in grafo.Nodes():
		listID[index] = ni.GetId()
		index+=1

	rangeQ = maxq-minq+1
	#Total q
	lnMrq = numpy.zeros([rangeQ,d],dtype=float)
	
	#Mass Exponents
	Tq = numpy.zeros(rangeQ)
	
	#Generalized dimensions
	Dq = numpy.zeros(rangeQ)
	
	#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.
	randomNodes = numpy.random.permutation(numNodes)	
	#I select 40 percent of nodes
	numberOfBoxes = int(percentSandBox*numpy.size(randomNodes));
	
	sandBoxes = numpy.zeros([d,numberOfBoxes])
	logR = numpy.array([])
	
	#High computational cost operation
	#I generated a matriz with distancies between nodes
	distances = numpy.zeros([numNodes,numNodes])
	
	#Due to ID nodes are not contiguous, I use the array with relation beetween index of array and ID node (listaID)
	for i in range(0, numNodes):
		for j in range(i, numNodes):
			#Same node
			if i == j:				
				distances[i][j] = 0
				distances[j][i] = 0
			else:
				dis = snap.GetShortPath(grafo,listID[i],listID[j]);
				distances[i][j] = dis
				distances[j][i] = dis
	
	
	
	for radius in range(1,d+1):
		
		logR = numpy.append(logR,math.log(float(radius)/d))
		
		for i in range(0, numberOfBoxes):
			currentNode = randomNodes[i]
			countNodes = 1
			#print i, radius
			for ni in range(0, numNodes):
				distance = distances[currentNode][ni];
				if  distance <= radius and distance > 0:
					countNodes+=1
			sandBoxes[radius-1][i] = countNodes
	
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
