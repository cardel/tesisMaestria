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
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm
import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
import robustness.robustness as robustness
import utils.utils as utils
import math
import numpy
import time
numpy.set_printoptions(threshold=numpy.nan)
from matplotlib.font_manager import FontProperties

def main(argv):
	fileInput = ""
	typeNet = ""
	fileOutput = ""
	try:
		opts, args = getopt.getopt(argv,'f:t:o:h',['file=','type=','output=', 'help='])
	except getopt.GetoptError as err:
		print(err)
		print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> ")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-f', '--file'):
			fileInput = arg
		elif opt in ('-t','--type'):
			typeNet = arg
		elif opt in ('-o','--output'):
			fileOutput = arg
		elif opt in ('-n','--node'):
			nodes = int(arg)
		else:
			print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> ")
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
	percentOfSandBoxes = 0.5
	repetitionsSB = 100

	#Genetic
	iterationsGenetic = 100
	sizePopulation = 200 
	percentCrossOver = 0.4
	percentMutation = 0.05	
	degreeOfBoring = 20
	
	
	#Box counting
	percentNodesT = 0.6
	
	#Simulated annealing
	temperature = 1500
		
	#Analysis with component gigaint
	print("start")
	RTqA,measureGCA,measureAPLA=robustness.robustness_analysis(graph,'Random',minq,maxq,percentOfSandBoxes,repetitionsSB)
	print("random")
	RTqB,measureGCB,measureAPLB=robustness.robustness_analysis(graph,'Degree',minq,maxq,percentOfSandBoxes,repetitionsSB)
	print("degree")
	RTqC,measureGCC,measureAPLC=robustness.robustness_analysis(graph,'Centrality',minq,maxq,percentOfSandBoxes,repetitionsSB)
	print("Centrality")
	RTqD,measureGCD,measureAPLD=robustness.robustness_analysis(graph,'Genetic',minq,maxq,percentOfSandBoxes,repetitionsSB,0,sizePopulation,iterationsGenetic,percentCrossOver,percentMutation,degreeOfBoring)
	print("Genetic")
	RTqE,measureGCE,measureAPLE=robustness.robustness_analysis(graph,'Simulated',minq,maxq,percentOfSandBoxes,repetitionsSB,temperature)
	print("simulated")

	r = numpy.arange(0.0, 1.0, 0.1)
	
	timestr = time.strftime("%Y%m%d_%H%M%S")
	file_object = open("Results/Robustness/"+timestr+fileOutput, 'w') 
	
	file_object.write("PercentOfNodes\n")
	file_object.write(numpy.array2string(r , precision=8, separator=','))
	
	file_object.write("\n\nRandomAttack\n")
	file_object.write("Tq\n")	
	file_object.write(numpy.array2string(RTqA, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(numpy.array2string(measureGCA, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(numpy.array2string(measureAPLA, precision=8, separator=','))


	file_object.write("\n\nDegree\n")
	file_object.write("Tq\n")	
	file_object.write(numpy.array2string(RTqB, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(numpy.array2string(measureGCB, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(numpy.array2string(measureAPLB, precision=8, separator=','))
	
	file_object.write("\n\nCentrality\n")
	file_object.write("Tq\n")	
	file_object.write(numpy.array2string(RTqC, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(numpy.array2string(measureGCC, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(numpy.array2string(measureAPLC, precision=8, separator=','))
	
	file_object.write("\n\nGenetic\n")
	file_object.write("Tq\n")	
	file_object.write(numpy.array2string(RTqD, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(numpy.array2string(measureGCD, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(numpy.array2string(measureAPLD, precision=8, separator=','))
	
	
	file_object.write("\n\nSimulated\n")
	file_object.write("Tq\n")	
	file_object.write(numpy.array2string(RTqE, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(numpy.array2string(measureGCE, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(numpy.array2string(measureAPLE, precision=8, separator=','))
		
	#symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	#symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	#r = numpy.arange(0.0, 1.0, 0.1)

	#timestr = time.strftime("%Y%m%d_%H%M%S")
	#fig0 = plt.figure()
	#for i in range(0,9):
		#if i < RTqA.shape[0]:
			#plt.plot(range(minq,maxq+1),RTqA[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality attack Random')
	#plt.show()
	##plt.savefig('Results/Robustness/'+timestr+'_'+'sizeComponent'+fileOutput+'.png')

	#fig1 = plt.figure()
	#for i in range(0,9):
		#if i < RTqB.shape[0]:
			#plt.plot(range(minq,maxq+1),RTqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality attack Degree')
	#plt.show()
	##plt.savefig('Results/Robustness/'+timestr+'_'+'lenghtPath'+fileOutput+'.png')	

	#fig1 = plt.figure()
	#for i in range(0,9):
		#if i < RTqC.shape[0]:
			#plt.plot(range(minq,maxq+1),RTqC[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality attack Centrality')
	#plt.show()
	##plt.savefig('Results/Robustness/'+timestr+'_'+'attackGenetic'+fileOutput+'.png')	

	#fig2 = plt.figure()
	#for i in range(0,7):
		#if i < RTqD.shape[0]:
			#plt.plot(range(minq,maxq+1),RTqD[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality attack Genetic')
	#plt.show()
	##plt.savefig('Results/Robustness/'+timestr+'_'+'attackGenetic'+fileOutput+'.png')		
	
	#fig3 = plt.figure()
	#for i in range(0,9):
		#if i < RTqE.shape[0]:
			#plt.plot(range(minq,maxq+1),RTqE[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(int(100*r[i]))+"%")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('q')
	#plt.ylabel('D(q)')
	#plt.title('Multifractality attack Simulated')
	#plt.show()
						
	#fig4 = plt.figure()	
	#plt.plot(r[0:numpy.size(measureGCA)],measureGCA,'.-r', label="Random ")		
	#plt.plot(r[0:numpy.size(measureGCB)],measureGCB,'.-b', label="Degree")			
	#plt.plot(r[0:numpy.size(measureGCC)],measureGCC,'.-k', label="Centrailiy")	
	#plt.plot(r[0:numpy.size(measureGCD)],measureGCD,'.-g', label="Genetic ")	
	#plt.plot(r[0:numpy.size(measureGCE)],measureGCE,'.-m', label="Simulated annealing ")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('percent')
	#plt.ylabel('Value')
	#plt.title('Robustness measure Size of Giant component ')
	#plt.show()
	
	#fig5 = plt.figure()	
	#plt.plot(r[0:numpy.size(measureAPLA)],measureAPLA,'.-r', label="Random ")		
	#plt.plot(r[0:numpy.size(measureAPLB)],measureAPLB,'.-b', label="Degree")			
	#plt.plot(r[0:numpy.size(measureAPLC)],measureAPLC,'.-k', label="Centrailiy")	
	#plt.plot(r[0:numpy.size(measureAPLD)],measureAPLD,'.-g', label="Genetic ")	
	#plt.plot(r[0:numpy.size(measureAPLE)],measureAPLE,'.-m', label="Simulated annealing ")	
	#ymin, ymax = plt.ylim()
	#plt.ylim((ymin, ymax*1.2))
	#fontP = FontProperties()
	#fontP.set_size('small')
	#plt.legend(prop=fontP)
	#plt.xlabel('percent')
	#plt.ylabel('Value')
	#plt.title('Robustness measure Average Path Lenght ')
	#plt.show()
	#plt.savefig('Results/Robustness/'+timestr+'_'+'measure'+fileOutput+'.png')	
							
if __name__ == "__main__":
   main(sys.argv[1:])
