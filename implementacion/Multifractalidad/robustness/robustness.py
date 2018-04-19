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
import Genetic.SBGenetic as SBGenetic
import lib.snap as snap

#Get meseaure of Robustness according giant component
#Article Mitigation of malicious attacks on networks
#http://w.pnas.org/cgi/doi/10.1073/pnas.1009440108
def robustness_analysis_GC(graph,typeRemoval,minq,maxq,percentOfSandBoxes,iterationsSandBox):
	#Remove per percent of nodes 0.1 to 1.0
	percent = 0.1
	r = numpy.arange(0.1, 1.0,percent)
	g = utils.copyGraph(graph)	
	N = g.GetNodes()
	
	measure = numpy.array([],dtype=float)
	initialSize = utils.getSizeOfGiantComponent(g)
	measure = numpy.append(measure,initialSize/N)
	
	ClosenessCentrality = numpy.empty([N,2], dtype=float)
	index=0
	for NI in g.Nodes():
		ClosenessCentrality[index][0]=NI.GetId()
		ClosenessCentrality[index][1]=snap.GetClosenessCentr(graph,NI.GetId())
		index+=1
		
	ClosenessCentrality = ClosenessCentrality[ClosenessCentrality[:,1].argsort()]
		
	logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
	RTq = Dq
	for p in r:
		me=utils.removeNodes(g,typeRemoval,percent,p,N,ClosenessCentrality,'GC')
		#There are errors if p > 0.7
		if p <= 0.7:
			logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
			RTq = numpy.vstack((RTq,Dq))
		measure = numpy.append(measure,me)
		
	robustnessmeasure = numpy.sum(measure)/N
	return RTq, measure,robustnessmeasure
	

#Get mesaure of Robustness according average path lenght
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133
def robustness_analysis_APL(graph,typeRemoval,minq,maxq,percentOfSandBoxes,iterationsSandBox):
	#Remove per percent of nodes 0.1 to 1.0
	percent = 0.1
	r = numpy.arange(0.1, 1.0,percent)
	g = utils.copyGraph(graph)	
	N = g.GetNodes()
	
	measure = numpy.array([],dtype=float)
	
	initial = utils.getAveragePathLength(g)
	measure = numpy.append(measure,1)
	
	ClosenessCentrality = numpy.empty([N,2], dtype=float)
	index=0
	for NI in g.Nodes():
		ClosenessCentrality[index][0]=NI.GetId()
		ClosenessCentrality[index][1]=snap.GetClosenessCentr(graph,NI.GetId())
		index+=1
		
	ClosenessCentrality = ClosenessCentrality[ClosenessCentrality[:,1].argsort()]
		
	logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
	RTq = Dq
	for p in r:
		me=utils.removeNodes(g,typeRemoval,percent,p,N,ClosenessCentrality,'APL')
		#There are errors if p > 0.7
		if p <= 0.7:
			logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
			RTq = numpy.vstack((RTq,Dq))
		measure = numpy.append(measure,me/initial)
		
	robustnessmeasure = numpy.sum(measure)/N
	return RTq, measure,robustnessmeasure



	
def robustness_analysis_Genetic(graph,minq,maxq,percentOfSandBoxes,iterations,sizePopulation,percentCrossOver,percentMutation,iterationsSandBox,typeMeasure):
	
	radius = snap.GetBfsFullDiam(graph,10,False)
	percent = 0.1
	r = numpy.arange(0.1, 1.0,percent)
	g = utils.copyGraph(graph)	
	N = g.GetNodes()	
	
	measure = numpy.array([],dtype=float)
	
	logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
	RTq = Dq
	for p in r:
		##I generated a matriz with distancies between nodes
		Ng = g.GetNodes()	
		listID = snap.TIntV(Ng)
		index = 0
		for ni in g.Nodes():
			listID[index] = ni.GetId()
			index+=1
			
		distances = utils.getDistancesMatrix(g,Ng, listID)
			
		nodesToRemove = SBGenetic.calculateCenters(g, Ng,percent, iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listID)
		for node in nodesToRemove:
			print listID[int(node)]
			g.DelNode(listID[int(node)])
		
		#nodesGRemove = snap.TIntV(numpy.size(nodesToRemove))
		me = 0
		#me=utils.removeNodesGenetic(g,nodesToRemove, N,listID, typeMeasure)

		logR, Indexzero,Tq, Dq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes,iterationsSandBox)
		RTq = numpy.vstack((RTq,Dq))
		
		measure = measure = numpy.append(measure,me)
	robustnessmeasure = numpy.sum(measure)/N
	return RTq, measure,robustnessmeasure
