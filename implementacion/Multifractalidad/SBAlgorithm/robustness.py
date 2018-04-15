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
	#Remove per percent of nodes 0.1 to 0.9
	r = numpy.arange(0.0, 0.9, 0.1)
	DegV = snap.TIntPrV()
	snap.GetNodeInDegV(graph, DegV)
	sorted(DegV, key=lambda x: x.GetVal2())
	for p in r:
		g = utils.removeNodes(graph,DegV,typeRemoval,p)
		#logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentOfSandBoxes)
	

#Get mesaure of Robustness according average path lenght
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133
def roburobustness_analysis_APL(graph,typeRemoval):
	#Remove per percent of nodes 0.1 to 0.9
	print 0
