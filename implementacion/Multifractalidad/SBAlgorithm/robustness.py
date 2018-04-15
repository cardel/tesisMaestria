#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th March 2018
#Description: This algorithm provide some methods for robustness in complex networks

import snap
import utils
import random
import SBAlgorithm
import numpy

#Get meseaure of Robustness according giant component
#Article Mitigation of malicious attacks on networks
#http://w.pnas.org/cgi/doi/10.1073/pnas.1009440108
def robustness_analysis_GC(graph,typeRemoval,minq,maxq,percentOfSandBoxes):
	#Remove per percent of nodes 0.1 to 0.7
	percent = 0.1
	r = numpy.arange(0.1, 0.7,percent)
	g = utils.copyGraph(graph)	
	N = g.GetNodes()
	
	ClosenessCentrality = numpy.empty([N,2], dtype=float)
	index=0
	for NI in g.Nodes():
		ClosenessCentrality[index][0]=NI.GetId()
		ClosenessCentrality[index][1]=snap.GetClosenessCentr(graph,NI.GetId())
		index+=1
		
	ClosenessCentrality = ClosenessCentrality[ClosenessCentrality[:,1].argsort()]
		
	logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes)
	RTq = Dq
	for p in r:
		utils.removeNodes(g,typeRemoval,percent,p,N,ClosenessCentrality)
		logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes)
		RTq = numpy.vstack((RTq,Dq))
	return RTq
	

#Get mesaure of Robustness according average path lenght
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133
def roburobustness_analysis_APL(graph,typeRemoval,minq,maxq,percentOfSandBoxes):
	#Remove per percent of nodes 0.1 to 0.7
	percent = 0.1
	r = numpy.arange(0.1, 0.7,percent)
	g = utils.copyGraph(graph)	
	N = g.GetNodes()
	
	ClosenessCentrality = numpy.empty([N,2], dtype=float)
	index=0
	for NI in g.Nodes():
		ClosenessCentrality[index][0]=NI.GetId()
		ClosenessCentrality[index][1]=snap.GetClosenessCentr(graph,NI.GetId())
		index+=1
		
	ClosenessCentrality = ClosenessCentrality[ClosenessCentrality[:,1].argsort()]
		
	logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes)
	RTq = Dq
	for p in r:
		utils.removeNodes(g,typeRemoval,percent,p,N,ClosenessCentrality)
		logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes)
		RTq = numpy.vstack((RTq,Dq))
	return RTq
