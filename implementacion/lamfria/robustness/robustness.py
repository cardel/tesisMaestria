#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th Aprim 2018
#Description: This algorithm provide some methods for robustness in complex networks

import random
import numpy
import sys
import utils.utils as utils
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import Genetic.Genetic as Genetic
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import lib.snap as snap

#Get meseaure of Robustness according giant component
#Article Mitigation of malicious attacks on networks
#http://w.pnas.org/cgi/doi/10.1073/pnas.1009440108
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133
def robustness_analysis(graph,typeRemoval,minq,maxq,percentNodesT,repetitionsDeterminics, temperature=0, sizePopulation=0, iterationsGenetic=0, percentCrossOver=0,percentMutation=0,degreeOfBoring=0):
	#Remove per percent of nodes 0.1 to 1.0
	
	r = numpy.arange(0.1, 1.0,0.1)
	
	#Copy graph
	g = utils.copyGraph(graph)	
	
	#NumNodes
	N = g.GetNodes()
	
	#Remove 10% of nodes	
	numberNodesToRemove = int(0.1*float(N))
	
	#Initial distance
	d = snap.GetBfsFullDiam(g,10,False)	
	
	#Outputs
	robustnessGC = numpy.array([N],dtype=float)
	robustnessAPL = numpy.array([d],dtype=float)	
		
	logR, Indexzero,Tq, Dq,lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)
	RTq = Dq
	
	sizeChromosome = int(0.1*N)
	
	for p in r:
		measureGC = 0.
		measureAPL = 0.
		#try:
		Ng = g.GetNodes()	
		diameterG = snap.GetBfsFullDiam(g,10,False)	
		maxDegree = 0.
		index = 0
		listID = snap.TIntV(Ng)
		listDegree =  snap.TIntV(Ng)
		for ni in g.Nodes():
			listID[index] = ni.GetId()
			listDegree[index] = int(ni.GetOutDeg())
			
			if listDegree[index] > maxDegree:
				maxDegree=listDegree[index]
				
			index+=1
		

		distances = utils.getDistancesMatrix(g,Ng, listID)	
				
		
		#Calculate clossness centrality
		ClosenessCentrality = utils.getOrderedClosenessCentrality(g,Ng)
		nodesToRemove = numpy.array([])			
			
		if(	typeRemoval=='Genetic'):
			nodesToRemove = Genetic.calculateCentersFixedSize(g, Ng, iterationsGenetic, sizePopulation, diameterG, distances, percentCrossOver, percentMutation,listDegree,maxDegree, sizeChromosome,degreeOfBoring)
		elif typeRemoval=='Simulated':
			nodesToRemove = SimulatedAnnealing.calculateCenters(g, Ng,0, temperature, diameterG,distances, listID, listDegree, sizeChromosome)	
		
		measureGC,measureAPL=utils.removeNodes(g,typeRemoval, p, numberNodesToRemove, ClosenessCentrality,listID,nodesToRemove)
		try:
			logR, Indexzero,Tq, Dq,lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)
			RTq = numpy.vstack((RTq,Dq))
		except:
			print "It is not possible to calculate fractal dimensiones ",typeRemoval, " remove percent= ",p 

		robustnessGC = numpy.append(robustnessGC,measureGC)
		robustnessAPL = numpy.append(robustnessAPL,measureAPL)

	return RTq, robustnessGC/N, robustnessAPL/d
	
