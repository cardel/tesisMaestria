#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 15th April 2018
#Description: The main file
import sys
import getopt
import lib.snap as snap
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import Genetic.SBGenetic as SBGenetic
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import robustness.robustness as robustness
import utils.utils as utils
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy
import time
from matplotlib.font_manager import FontProperties

def main(argv):
	fileInput = ""
	typeNet = ""
	fileOutput = ""
	message=""
	attack=""
	nodes=0
	desiredGrade=0
	typeMeasure = ""
	try:
		opts, args = getopt.getopt(argv,'f:t:o:m:a:h:n:d:y',['file=','type=','output=', 'message=','attack=','help=','node=','desired=','measure='])
	except getopt.GetoptError as err:
		print(err)
		print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> --attack centrality|degree|random --typeMeasure GC|APL")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-f', '--file'):
			fileInput = arg
		elif opt in ('-t','--type'):
			typeNet = arg
		elif opt in ('-o','--output'):
			fileOutput = arg
		elif opt in ('-m','--message'):
			message = arg
		elif opt in ('-a','--attack'):
			attack = arg
		elif opt in ('-d','--desired'):
			desiredGrade = int(arg)
		elif opt in ('-n','--node'):
			nodes = int(arg)
		elif opt in ('-y','--measure'):
			typeMeasure=arg
		else:
			print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> --attack centrality|degree|random")
			sys.exit(0)
										
	Rnd = snap.TRnd(1,0)
	if typeNet == "Edge":
		graph = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1)
	elif typeNet == "ConnList":
		graph = snap.LoadConnList(snap.PUNGraph, fileInput)
	elif typeNet == "Pajek":
		graph = snap.LoadPajek(snap.PUNGraph, fileInput)
	elif typeNet == "SmallWorld":		
		graph = snap.GenSmallWorld(nodes, desiredGrade, 0.03, Rnd)
	elif typeNet == "ScaleFreePowerLaw":
		graph = snap.GenRndPowerLaw(500, 2.5)
	elif typeNet == "ScaleFreePrefAttach":
		graph = snap.GenPrefAttach(nodes, desiredGrade,Rnd)
	elif typeNet == "Random":
		graph = snap.GenRndGnm(snap.PUNGraph, nodes, desiredGrade)
	elif typeNet == "Flower":
		graph = utils.generateFlowerUV()
	else:
		graph = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	

	minq = -10
	maxq = 10
	
	#SandBox
	percentOfSandBoxes = 0.4
	
	#Genetic
	iterations = 150
	iterationsDeterminics = 200
	sizePopulation = 100 
	percentCrossOver = 0.3
	percentMutation = 0.05	
	
	
	#Box counting
	percentNodesT = 0.7
	repetitionsBC = 300
	
	#Simulated annealing
	Kmax = 3000
	#	
	RTqA=0
	measureA=0
	robustnessmeasureA=0
	TqB=0
	measureB=0
	robustnessmeasureB=0
	#Analysis with component gigaint
	if typeMeasure=='GC':
		RTqA,measureA,robustnessmeasureA=robustness.robustness_analysis_GC(graph,attack,minq,maxq,percentOfSandBoxes,iterations)
	#Analysis with average path lenght
	if typeMeasure=='APL' :
		RTqB,measureB,robustnessmeasureB=robustness.robustness_analysis_APL(graph,attack,minq,maxq,percentOfSandBoxes,iterations)
	#Analysis with evolutive strategy
	RTqC,measureC,robustnessmeasureC=robustness.robustness_analysis_Genetic(graph,minq,maxq,percentOfSandBoxes,iterations,sizePopulation,percentCrossOver,percentMutation,iterationsDeterminics,typeMeasure)

	#Analysis with Simulated Annealing
	RTqD,measureD,robustnessmeasureD=robustness.robustness_analysis_Simulated(graph,minq,maxq,percentOfSandBoxes,Kmax,iterationsDeterminics,typeMeasure)
	
	symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	r = numpy.arange(0.0, 1.0, 0.1)

	timestr = time.strftime("%Y%m%d_%H%M%S")
	if typeMeasure=='GC':
		fig0 = plt.figure()
		for i in range(0,9):
			if i < RTqA.shape[0]:
				plt.plot(range(minq,maxq+1),RTqA[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
		ymin, ymax = plt.ylim()
		plt.ylim((ymin, ymax*1.2))
		fontP = FontProperties()
		fontP.set_size('small')
		plt.legend(prop=fontP)
		plt.xlabel('q')
		plt.ylabel('D(q)')
		plt.title('Multifractality componente Giant '+attack)
		#plt.show()
		plt.savefig('Results/Robustness/'+timestr+'_'+'sizeComponent'+fileOutput+'.png')
	
	if typeMeasure=='APL':
		fig1 = plt.figure()
		for i in range(0,9):
			if i < RTqB.shape[0]:
				plt.plot(range(minq,maxq+1),RTqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
		ymin, ymax = plt.ylim()
		plt.ylim((ymin, ymax*1.2))
		fontP = FontProperties()
		fontP.set_size('small')
		plt.legend(prop=fontP)
		plt.xlabel('q')
		plt.ylabel('D(q)')
		plt.title('Multifractality Attack Path Lenght '+attack)
		#plt.show()
		plt.savefig('Results/Robustness/'+timestr+'_'+'lenghtPath'+fileOutput+'.png')	

	fig2 = plt.figure()
	for i in range(0,7):
		if i < RTqC.shape[0]:
			plt.plot(range(minq,maxq+1),RTqC[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	ymin, ymax = plt.ylim()
	plt.ylim((ymin, ymax*1.2))
	fontP = FontProperties()
	fontP.set_size('small')
	plt.legend(prop=fontP)
	plt.xlabel('q')
	plt.ylabel('D(q)')
	plt.title('Multifractality Attack Genetic ')
	#plt.show()
	plt.savefig('Results/Robustness/'+timestr+'_'+'attackGenetic'+fileOutput+'.png')	
	
	fig3 = plt.figure()
	for i in range(0,9):
		if i < RTqD.shape[0]:
			plt.plot(range(minq,maxq+1),RTqD[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	ymin, ymax = plt.ylim()
	plt.ylim((ymin, ymax*1.2))
	fontP = FontProperties()
	fontP.set_size('small')
	plt.legend(prop=fontP)
	plt.xlabel('q')
	plt.ylabel('D(q)')
	plt.title('Multifractality Attack Simulated Allieaning')
	#plt.show()
	plt.savefig('Results/Robustness/'+timestr+'_'+'attackSimulated'+fileOutput+'.png')	
						
	fig4 = plt.figure()	
	if typeMeasure=='GC':
		plt.plot(r[0:numpy.size(measureA)],measureA,'.-r', label="Size gigaint component")	
		
	if typeMeasure=='APL':
		plt.plot(r[0:numpy.size(measureB)],measureB,'.-b', label="Average path lenght")	
		
	plt.plot(r[0:numpy.size(measureC)],measureC,'.-k', label="Genetic "+typeMeasure)	
	plt.plot(r[0:numpy.size(measureD)],measureD,'.-m', label="Simulated annealing "+typeMeasure)		
	ymin, ymax = plt.ylim()
	plt.ylim((ymin, ymax*1.2))
	fontP = FontProperties()
	fontP.set_size('small')
	plt.legend(prop=fontP)
	plt.xlabel('q')
	plt.ylabel('D(q)')
	plt.title('Robustness measure ')
	#plt.show()
	plt.savefig('Results/Robustness/'+timestr+'_'+'measure'+fileOutput+'.png')	
							
if __name__ == "__main__":
   main(sys.argv[1:])

