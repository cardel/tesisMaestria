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
import robustness.robustness as robustness
import Genetic.SBGenetic as SBGenetic
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import utils.utils as utils
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
	
	try:
		opts, args = getopt.getopt(argv,'f:t:o:m:a:h:n:d',['file=','type=','output=', 'message=','attack=','help=','node=','desired='])
	except getopt.GetoptError as err:
		print(err)
		print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> --attack centrality|degree|random")
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
			nodes = int(arg)
		elif opt in ('-n','--node'):
			desiredGrade = int(arg)
		elif opt in ('-h','--help'):
			print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> --attack centrality|degree|random")
			sys.exit(0)
										
	Rnd = snap.TRnd(1,0)
	if typeNet == "Edge":
		graph = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	elif typeNet == "ConnList":
		graph = snap.LoadConnList(snap.PUNGraph, fileInput)
	elif typeNet == "Pajek":
		graph = snap.LoadPajek(snap.PUNGraph, fileInput)
	elif typeNet == "SmallWorld":		
		graph = snap.GenSmallWorld(nodes, desiredGrade, 0, Rnd)
	elif typeNet == "ScaleFreePowerLaw":
		graph = snap.GenRndPowerLaw(500, 2.5)
	elif typeNet == "ScaleFreePrefAttach":
		graph = snap.GenPrefAttach(1000, 300,Rnd)
	elif typeNet == "Random":
		graph = snap.GenRndGnm(snap.PUNGraph, 1000, 999)
	elif typeNet == "Flower":
		graph = utils.generateFlowerUV()
	else:
		graph = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	

	minq = -10
	maxq = 10
	percentOfSandBoxes = 0.4
	#SandBox and Genetic
	iterations = 300
	iterationsSandBox = 100
	sizePopulation = 100 
	percentCrossOver = 0.3
	percentMutation = 0.05	
	typeMeasure = 'GC'
	
	#Simulated annealing
	Kmax = 3000
	#RTq,measure,robustnessmeasure=robustness.robustness_analysis_GC(graph,attack,minq,maxq,percentOfSandBoxes,iterations)

	#RTq,measure,robustnessmeasure=robustness.robustness_analysis_APL(graph,attack,minq,maxq,percentOfSandBoxes,iterations)
	
	#print robustnessmeasure
	executionTime = numpy.zeros(3,dtype=float)
	executionTime[0] = time.time()

	logRA, IndexzeroA,TqA, DqA = SBAlgorithm.SBAlgorithm(graph,minq,maxq,percentOfSandBoxes,iterationsSandBox)
	
	executionTime[1] = time.time()
	executionTime[0] = executionTime[1] - executionTime[0]

	logRB, IndexzeroB,TqB, DqB, lnMrqB = SBGenetic.SBGenetic(graph,minq,maxq,percentOfSandBoxes,sizePopulation,iterations, percentCrossOver, percentMutation)
	
	executionTime[2] = time.time()
	executionTime[1] = executionTime[2] - executionTime[1]
	
	logRC, IndexzeroC,TqC, DqC, lnMrqB = SimulatedAnnealing.SBSA(graph,minq,maxq,percentOfSandBoxes,sizePopulation, Kmax)
	
	executionTime[2] = time.time() - executionTime[2]
	
	
	##Robustness measure Genetic Algorithm
	#RTq,measure,robustnessmeasure=robustness.robustness_analysis_Genetic(graph,minq,maxq,percentOfSandBoxes,iterations,sizePopulation,percentCrossOver,percentMutation,iterationsSandBox,typeMeasure)
	
	##Robusness messure  Simulated Annealing
	#RTqB,measureB,robustnessmeasureB=robustness.robustness_analysis_Simulated(graph,minq,maxq,percentOfSandBoxes,Kmax,iterationsSandBox,typeMeasure)
	
	##Matplotlib
	#symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	#fig0 = plt.figure()
	#r = numpy.arange(0.0, 1.0, 0.1)
	#for i in range(0,7):
		#plt.plot(range(minq,maxq+1),RTq[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")

	
	#timestr = time.strftime("%Y%m%d_%H%M%S")
	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality Attack Genetic '+message)
	##plt.show()
	#plt.savefig('Results/'+timestr+'_'+'genetic'+fileOutput+'.png')
	
	#fig5 = plt.figure()
	#r = numpy.arange(0.0, 1.0, 0.1)
	#for i in range(0,7):
		#plt.plot(range(minq,maxq+1),RTqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")

	
	#timestr = time.strftime("%Y%m%d_%H%M%S")
	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality Attack Simulated Annealing '+message)
	#plt.savefig('Results/'+timestr+'_'+'simulated'+fileOutput+'.png')
	#plt.show()		
	#fig1 = plt.figure()
	#i = 0
	#for q in range(minq,maxq+1):
		#plt.plot(logR,lnMrq[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="q="+str(q))
		#i+=1
	
	#plt.xlabel('ln(r/d)')
	#plt.ylabel('ln(<M(r)>)^q')
	#plt.title("Mass exponents")
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax+20)) 
	#plt.legend(loc=9, bbox_to_anchor=(0.1, 1))
	#plt.show()
	
	#fig2 = plt.figure()
	#plt.xlabel('q')
	#plt.ylabel('t(q)')	
	#plt.title("Mass exponents")
	#plt.plot(range(minq,maxq+1), Tq,'bo-')
	#plt.show()
	fig3 = plt.figure()
	plt.xlabel('q')
	plt.ylabel('D(q)')	
	plt.title("Generalizated Fractal dimensions")

	plt.plot(range(minq,maxq+1), DqA,'ro-', label='SBAlgorithm')
	plt.plot(range(minq,maxq+1), DqB,'bo-', label='Genetic')
	plt.plot(range(minq,maxq+1), DqC,'mo-', label='Simulated Annealing')
	ymin, ymax = plt.ylim()
	xmin, xmax = plt.xlim()
	plt.ylim((ymin, 1.1*ymax))
	#plt.text(xmin/2,ymax,'Fractal Dim '+str(Dq[Indexzero])+'Dim inf '+str(Dq[Indexzero+1])+'Corr '+str(Dq[Indexzero+2]))
	fontP = FontProperties()
	fontP.set_size('small')
	plt.legend(prop=fontP)
	plt.savefig('Results/'+timestr+'_'+'fractality'+fileOutput+'.png')
	#plt.show()
	
	fig4 = plt.figure()
	plt.xlabel('Strategy')
	plt.ylabel('Time(s)')
	x=numpy.arange(3)
	plt.bar(x, executionTime)
	plt.xticks(x, ('SBAlgorithm', 'Evolutive', 'Simulated'))
	plt.savefig('Results/'+timestr+'_'+'timeAlgorithms'+fileOutput+'.png')
	#plt.show()
					
if __name__ == "__main__":
   main(sys.argv[1:])

