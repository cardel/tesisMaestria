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
import BCAlgorithm.BCAlgorithm as BCAlgorithm
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
		
	logR, Indexzero,Tq, Dq,lnMrq = BCAlgorithm.BCAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)	
	RTq = Dq
	
	sizeChromosome = int(0.1*N)
	
	for p in r:
		measureGC = 0.
		measureAPL = 0.
		#try:
		Ng = g.GetNodes()	
		print(Ng)
		diameterG = snap.GetBfsFullDiam(g,10,False)	
		listID = snap.TIntV(Ng)
		index = 0
		#Calculate clossness centrality
		ClosenessCentrality = utils.getOrderedClosenessCentrality(g,Ng)
		nodesToRemove = numpy.array([])
			
		listID = snap.TIntV(Ng)
		listDegree =  snap.TIntV(Ng)
		
		maxDegree = 0.
		index = 0
		for ni in g.Nodes():
			listID[index] = ni.GetId()
			listDegree[index] = int(ni.GetOutDeg())
			
			if listDegree[index] > maxDegree:
				maxDegree=listDegree[index]
			index+=1
					
		distances = utils.getDistancesMatrix(g,Ng, listID)	
			
			
		if(	typeRemoval=='Genetic'):
			nodesToRemove = Genetic.calculateCentersFixedSize(g, Ng, iterationsGenetic, sizePopulation, diameterG, distances, percentCrossOver, percentMutation,listDegree,maxDegree, sizeChromosome,degreeOfBoring)
		elif typeRemoval=='Simulated':
			nodesToRemove = SimulatedAnnealing.calculateCenters(g, Ng,percentNodesT, temperature, diameterG,distances, listID, listDegree)			
				
		measureGC,measureAPL=utils.removeNodes(g,typeRemoval, p, numberNodesToRemove, ClosenessCentrality,listID,nodesToRemove)
		#There are errors if p > 0.7
		logR, Indexzero,Tq, Dq,lnMrq = BCAlgorithm.BCAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)
		RTq = numpy.vstack((RTq,Dq))
		#except:
			#print "Error try to delete ",p," percent of nodes ",typeRemoval	
			#print("Error inesperado:", sys.exc_info()[0])
		#finally:
		robustnessGC = numpy.append(robustnessGC,measureGC)
		robustnessAPL = numpy.append(robustnessAPL,measureAPL)

	return RTq, robustnessGC/N, robustnessAPL/d
	
