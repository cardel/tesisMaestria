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
import Genetic.Genetic as Genetic
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm
import BCAlgorithm.BCAlgorithm as BCAlgorithm
import CBBAlgorithm.CBBAlgorithm as CBBAlgorithm
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import robustness.robustness as robustness
import utils.utils as utils
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy
numpy.set_printoptions(threshold=numpy.nan)
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
		opts, args = getopt.getopt(argv,'f:t:o:m:a:h:n:d:y',['file=','type=','output=','attack=','help=','node=','desired=','measure='])
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
		graph = snap.GenRndPowerLaw(1000, 1.8)
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
	percentOfSandBoxes = 0.6
	repetitionsDeterminics = 250

	#Genetic
	iterations = 200
	sizePopulation = 200 
	percentCrossOver = 0.4
	percentMutation = 0.05	
	degreeOfBoring = 20
	
	
	#Box counting
	percentNodesT = 0.7
	
	#Simulated annealing
	Kmax = 3000
	
	print CBBAlgorithm.CBBFractality(graph)
	

	#fig1 = plt.figure()
	#i = 0
	#for q in range(minq,maxq+1):
		#if q%2==0:
			#plt.plot(logRA,lnMrqA[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="q="+str(q))
		#i+=1
	#plt.ylabel('ln(<Z(r)>)^q')
	#plt.title("Mass exponents BC")
	#plt.xlabel('ln(r/d)')
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.savefig('Results/Fractality/'+timestr+'_'+'TqLnrBC'+fileOutput+'.png')

	#fig2 = plt.figure()
	#i = 0
	#for q in range(minq,maxq+1):
		#if q%2==0:
			#plt.plot(logRB,lnMrqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="q="+str(q))
		#i+=1
	#plt.ylabel('ln(<M(r)>)^q')
	#plt.title("Mass exponents SB")
	#plt.xlabel('ln(r/d)')
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.savefig('Results/Fractality/'+timestr+'_'+'TqLnrSB'+fileOutput+'.png')	

	#fig3 = plt.figure()
	#i = 0
	#for q in range(minq,maxq+1):
		#if q%2==0:
			#plt.plot(logRC,lnMrqC[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="q="+str(q))
		#i+=1
	#plt.ylabel('ln(<M(r)>)^q')
	#plt.title("Mass exponents Genetic")
	#plt.xlabel('ln(r/d)')
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.savefig('Results/Fractality/'+timestr+'_'+'TqLnrGenetic'+fileOutput+'.png')	
	
	#fig5 = plt.figure()
	#plt.xlabel('q')
	#plt.ylabel('D(q)')	
	#plt.title("Generalizated Fractal dimensions")

	#plt.plot(range(minq,maxq+1), DqA,'r<-', label='Box Counting Fixed')
	#plt.plot(range(minq,maxq+1), DqB,'b<-', label='Sand Box Algorithm')
	#plt.plot(range(minq,maxq+1), DqC,'m>-', label='Evolutive SB')
	#plt.plot(range(minq,maxq+1), DqD,'k>-', label='Simulated SB')
	#plt.plot(range(minq,maxq+1), DqE,'go-', label='Evolutive BC')
	#plt.plot(range(minq,maxq+1), DqF,'co-', label='Simulated BC')
	#ymin, ymax = plt.ylim()
	#xmin, xmax = plt.xlim()
	#plt.ylim((ymin, 1.1*ymax))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.savefig('Results/Fractality/'+timestr+'_'+'fractality'+fileOutput+'.png')
	##plt.show()
	#np.savez(message+timestr+"file.txt", genetico=arr1, name2=arr2)
	
	#fig6 = plt.figure()
	#plt.xlabel('Strategy')
	#plt.ylabel('Time(s)')
	#x=numpy.arange(6)
	#plt.bar(x, executionTime)
	#plt.xticks(x, ('Box counting', 'SBAlgorithm', 'Evolutive SB', 'Simulated SB', 'Evolutive BC', 'Simulated BC'))
	#plt.savefig('Results/Fractality/'+timestr+'_'+'timeAlgorithms'+fileOutput+'.png')
	
	
	
	#fig7 = plt.figure()
	#plt.xlabel('iterations')
	#plt.ylabel('Fitness')	
	#plt.title("Behaviour genetic algorithm")	 
	#plt.plot(range(0,numpy.size(fitNessAverage)), fitNessAverage,'r.-', label='Average')
	#plt.plot(range(0,numpy.size(fitNessMax)), fitNessMax,'b.-', label='Max')
	#plt.plot(range(0,numpy.size(fitNessMin)), fitNessMin,'m.-', label='min')
	#ymin, ymax = plt.ylim()
	#xmin, xmax = plt.xlim()
	#plt.ylim((ymin, 1.1*ymax))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.savefig('Results/Fractality/'+timestr+'_'+'evolutiveBehaviour'+fileOutput+'.png')
	
	#Files with open('multisave.npy','wb') as f:
	#https://stackoverflow.com/questions/42204368/how-to-append-many-numpy-files-into-one-numpy-file-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
					
if __name__ == "__main__":
   main(sys.argv[1:])

