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
	

	executionTime = numpy.zeros(9,dtype=float)
	
	executionTime[0] = time.time()
	logR, Indexzero,Tq, Dq, lnMrq = BCAlgorithm.BCAlgorithm(graph,minq,maxq,percentNodesT,repetitionsDeterminics)
	executionTime[0] = time.time() - executionTime[0]
	
	executionTime[1] = time.time()
	logRA, IndexzeroA,TqA, DqA, lnMrqA = FSBCAlgorithm.FSBCAlgorithm(graph,minq,maxq,percentNodesT,repetitionsDeterminics)
	executionTime[1] = time.time() - executionTime[1]
	
	executionTime[2] = time.time()
	logRB, IndexzeroB,TqB, DqB, lnMrqB = SBAlgorithm.SBAlgorithm(graph,minq,maxq,percentOfSandBoxes,repetitionsDeterminics)	
	executionTime[2] = time.time() -  executionTime[2]
	
	executionTime[3] = time.time()	
	logRC, IndexzeroC,TqC, DqC, lnMrqC,fitNessAverage,fitNessMax,fitNessMin = Genetic.Genetic(graph,minq,maxq,sizePopulation,iterations, percentCrossOver, percentMutation,degreeOfBoring, 'SB')	
	executionTime[3] = time.time() - executionTime[3]
	
	executionTime[4] = time.time()
	logRD, IndexzeroD,TqD, DqD, lnMrqD = SimulatedAnnealing.SA(graph,minq,maxq,percentOfSandBoxes,sizePopulation, Kmax, 'SB')
	executionTime[4] = time.time() - executionTime[4]

	executionTime[5] = time.time()	
	logRE, IndexzeroE,TqE, DqE, lnMrqE,fitNessAverageE,fitNessMaxE,fitNessMinE = Genetic.Genetic(graph,minq,maxq,sizePopulation,iterations, percentCrossOver, percentMutation,degreeOfBoring, 'BC')	
	executionTime[5] = time.time() - executionTime[5]
	
	executionTime[6] = time.time()
	logRF, IndexzeroF,TqF, DqF, lnMrqF = SimulatedAnnealing.SA(graph,minq,maxq,percentOfSandBoxes,sizePopulation, Kmax, 'BC')
	executionTime[6] = time.time() - executionTime[6]

	executionTime[7] = time.time()	
	logRG, IndexzeroG,TqG, DqG, lnMrqG,fitNessAverageG,fitNessMaxG,fitNessMinG = Genetic.Genetic(graph,minq,maxq,sizePopulation,iterations, percentCrossOver, percentMutation,degreeOfBoring, 'BCFS')	
	executionTime[7] = time.time() - executionTime[7]
	
	executionTime[8] = time.time()
	logRH, IndexzeroH,TqH, DqH, lnMrqH = SimulatedAnnealing.SA(graph,minq,maxq,percentOfSandBoxes,sizePopulation, Kmax, 'BCFS')
	executionTime[8] = time.time() - executionTime[8]
	
	timestr = time.strftime("%Y%m%d_%H%M%S")
	file_object = open("Results/Fractality/"+timestr+fileOutput, 'w') 
	##Matplotlib
	#symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	#timestr = time.strftime("%Y%m%d_%H%M%S")
	file_object.write("BCAlgorithm\n")
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logR, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroA))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(Tq, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(Dq, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrq, precision=8, separator=','))
	
		
	file_object.write("FSBCAlgorithm\n")
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRA, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroA))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqA, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqA, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqA, precision=8, separator=','))
	
	file_object.write("\n")
	file_object.write("\n")	
	file_object.write("\SBAlgorithm\n")
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRB, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroB))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqB, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqB, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqB, precision=8, separator=','))
	file_object.write("\n")
	file_object.write("\n")
	file_object.write("\n SandBox Genetic\n")	
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRC, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroC))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqC, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqC, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqC, precision=8, separator=','))
	file_object.write("\nfitNessAverage\n")
	file_object.write(numpy.array2string(fitNessAverage, precision=8, separator=','))
	file_object.write("\nfitNessMax\n")
	file_object.write(numpy.array2string(fitNessMax, precision=8, separator=','))
	file_object.write("\nfitNessMin\n")
	file_object.write(numpy.array2string(fitNessMin, precision=8, separator=','))
	file_object.write("\n")
	file_object.write("\n")
	file_object.write("\n SandBox Simulated Annealing\n")
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRD, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroD))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqD, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqD, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqD, precision=8, separator=','))
	file_object.write("\n")
	file_object.write("\n")
	file_object.write("\n BoxCounting Genetic\n")	
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRE, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroE))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqE, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqE, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqE, precision=8, separator=','))
	file_object.write("\nfitNessAverage\n")
	file_object.write(numpy.array2string(fitNessAverageE, precision=8, separator=','))
	file_object.write("\nfitNessMax\n")
	file_object.write(numpy.array2string(fitNessMaxE, precision=8, separator=','))
	file_object.write("\nfitNessMin\n")
	file_object.write(numpy.array2string(fitNessMinE, precision=8, separator=','))
	file_object.write("\n")
	file_object.write("\n")	
	file_object.write("\n BoxCounting Simulated Annealing\n")
	file_object.write("logR\n")
	file_object.write(numpy.array2string(logRE, precision=8, separator=','))
	file_object.write("\nIndexZero\n")
	file_object.write(str(IndexzeroE))
	file_object.write("\nTq\n")
	file_object.write(numpy.array2string(TqE, precision=8, separator=','))
	file_object.write("\nDq\n")
	file_object.write(numpy.array2string(DqE, precision=8, separator=','))
	file_object.write("\nlnMrq\n")
	file_object.write(numpy.array2string(lnMrqE, precision=8, separator=','))
	file_object.write("\n")
	file_object.write("\n")	
	file_object.write("\nExecution time\n")
	file_object.write("\nBox Counting\tBox Counting Fixed\tSandBox\tGenetic SandBox\tSimulated SandBox\tGenetic BCFS\tSimulated BCFS\n")
	file_object.write(numpy.array2string(executionTime, precision=8, separator=','))
	
	file_object.close() 

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

