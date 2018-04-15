#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 07th April 2018
#Description: The main file
import sys
import getopt
import snap
import SBAlgorithm
import robustness
import utils
import matplotlib.pyplot as plt
import math
import numpy

def main(argv):
	fileInput = "";
	typeNet = "";
	try:
		opts, args = getopt.getopt(argv,'f:t:',['file=','type='])
	except getopt.GetoptError as err:
		print(err)
		print("You must execute: python GreedyAlgorithm.py --file <file> --type <type>")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-f', '--file'):
			fileInput = arg
		elif opt in ('-t','--type'):
			typeNet = arg

	
	Rnd = snap.TRnd(1,0)
	if typeNet == "Edge":
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	elif typeNet == "ConnList":
		grafo = snap.LoadConnList(snap.PUNGraph, fileInput)
	elif typeNet == "Pajek":
		grafo = snap.LoadPajek(snap.PUNGraph, fileInput)
	elif typeNet == "TinyWorld":
		
		grafo = snap.GenSmallWorld(200, 3, 0, Rnd)
	elif typeNet == "ScaleFreePowerLaw":
		grafo = snap.GenRndPowerLaw(500, 2.5)
	elif typeNet == "ScaleFreePrefAttach":
		grafo = snap.GenPrefAttach(400, 30,Rnd)
	elif typeNet == "Random":
		grafo = snap.GenRndGnm(snap.PUNGraph, 1000, 999)
	elif typeNet == "Flower":
		grafo = utils.generateFlowerUV()
	else:
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	

	minq = -10
	maxq = 10
	percentOfSandBoxes = 0.4
	RTq=robustness.robustness_analysis_GC(grafo,'centrality',minq,maxq,percentOfSandBoxes)
	#print RTq
	logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(grafo,minq,maxq,percentOfSandBoxes)
	
	
	##Matplotlib
	symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
	fig0 = plt.figure()
	r = numpy.arange(0.0, 0.7, 0.1)
	for i in range(0,7):
		plt.plot(range(minq,maxq+1),RTq[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label="% nodes="+str(r[i]))
	
	ymin, ymax = plt.ylim()
	plt.ylim((ymin, ymax*1.2))
	plt.legend(loc=1, bbox_to_anchor=(0.1, 1))
	plt.xlabel('q')
	plt.ylabel('D(q)')
	plt.title('Multifractality by loss of highest degree nodes')
	plt.show()
	
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
	#fig3 = plt.figure()
	#plt.xlabel('q')
	#plt.ylabel('D(q)')	
	#plt.title("Generalizated Fractal dimensions")
	#plt.plot(range(minq,maxq+1), Dq,'ro-')
	
	#ymin, ymax = plt.ylim()
	#xmin, xmax = plt.xlim()
	#plt.ylim((ymin, 1.1*ymax))
	#plt.text(xmin/2,ymax,'Fractal Dim '+str(Dq[Indexzero])+'Dim inf '+str(Dq[Indexzero+1])+'Corr '+str(Dq[Indexzero+2]))
	#plt.show()
			
if __name__ == "__main__":
   main(sys.argv[1:])

