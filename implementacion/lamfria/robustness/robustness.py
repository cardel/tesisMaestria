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
import Genetic.Genetic as SBGenetic
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import lib.snap as snap

#Get meseaure of Robustness according giant component
#Article Mitigation of malicious attacks on networks
#http://w.pnas.org/cgi/doi/10.1073/pnas.1009440108
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133
def robustness_analysis(graph,typeRemoval,minq,maxq,percentNodesT,repetitionsDeterminics, nodesToRemove = numpy.array([])):
	#Remove per percent of nodes 0.1 to 1.0
	percent = 0.1
	r = numpy.arange(0.1, 1.0,percent)
	
	#Copy graph
	g = utils.copyGraph(graph)	
	
	#NumNodes
	N = g.GetNodes()
	
	#Initial distance
	d = snap.GetBfsFullDiam(graph,10,False)	
	
	#Outputs
	robustnessGC = numpy.array([N],dtype=float)
	robustnessAPL = numpy.array([d],dtype=float)		
	logR, Indexzero,Tq, Dq,lnMrq = BCAlgorithm.BCAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)
	RTq = Dq
	for p in r:
		measureGC = 0.
		measureAPL = 0.
		try:
			Ng = g.GetNodes()	
			listID = snap.TIntV(Ng)
			index = 0
			#Calculate clossness centrality
			ClosenessCentrality = utils.getOrderedClosenessCentrality(graph,N)
				
			for ni in g.Nodes():
				listID[index] = ni.GetId()
				index+=1	
			measureGC,measureAPL=utils.removeNodes(g,typeRemoval,percent,p,ClosenessCentrality,listID,nodesToRemove)
			#There are errors if p > 0.7
			logR, Indexzero,Tq, Dq,lnMrq = BCAlgorithm.BCAlgorithm(g,minq,maxq,percentNodesT,repetitionsDeterminics)
			RTq = numpy.vstack((RTq,Dq))
		except:
			me=float('nan')
			print "Error try to delete ",p," percent of nodes"			
		finally:
			robustnessGC = numpy.append(robustnessGC,measureGC)
			robustnessAPL = numpy.append(robustnessAPL,measureAPL)

	return RTq, measureGC/N, measureAPL/d
	
