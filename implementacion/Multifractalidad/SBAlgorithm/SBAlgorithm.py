#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th March 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import snap
import sys
import getopt
import numpy
import random
import math
from datetime import datetime
from sets import Set
import matplotlib.pyplot as plt

import utils

def main(argv):
	random.seed(datetime.now())
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
	elif typeNet == "ScaleFree":
		grafo = snap.GenRndPowerLaw(300, 1.5)
	elif typeNet == "ScaleFree":
		grafo = snap.GenPrefAttach(400, 30,Rnd)
	elif typeNet == "Random":
		grafo = snap.GenRndGnm(snap.PUNGraph, 300, 1200)
	elif typeNet == "Flower":
		grafo = generateFlowerUV()
	else:
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
		
	#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
	
	#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
	
	d = snap.GetBfsFullDiam(grafo,10,False)
	numNodes = grafo.GetNodes()
	listaID = numpy.zeros(numNodes)
	
	
	index = 0
	for ni in grafo.Nodes():
		listaID[index] = ni.GetId()
		index+=1

	#Matplotlib
	symbols = ['r-p','b-s','g-^','y-o','m->','c-<']
	
	fig1 = plt.figure()

	minq = -10
	maxq = 12
	#Mass Exponents
	Tq = numpy.zeros(maxq-minq+1)
	
	
	#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.
	randomNodes = numpy.random.permutation(listaID)	
	#I select 40 percent of nodes
	numberOfBoxes = int(0.4*numpy.size(randomNodes));
	
	sandBoxes = numpy.zeros([d,numberOfBoxes])
	logR = numpy.array([])
	
	for radius in range(1,d+1):
		
		logR = numpy.append(logR,math.log(float(radius)/d))
		
		for i in range(0, numberOfBoxes):
			currentNode = randomNodes[i]
			countNodes = 1
			for ni in grafo.Nodes():
				#High computational cost operation
				distance = snap.GetShortPath(grafo,ni.GetId(),int(currentNode));
				if  distance <= radius and distance > 0:
					countNodes+=1
			sandBoxes[radius-1][i] = countNodes
	
	count = 0
	for q in range(minq,maxq+1,1):
		infoPlot = numpy.array([])
	
		for sand in sandBoxes:
			Mr = numpy.power(sand,q-1)
			Mr = numpy.log(numpy.average(Mr))
			infoPlot=numpy.append(infoPlot, Mr)			
		
		if math.fmod(q,2)==0 and q >= 0:
			plt.plot(logR,infoPlot,symbols[int(math.fmod(count,numpy.size(symbols)))], label="q="+str(q))
		
		m,b = linealRegresssion(logR,infoPlot)
		#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
		if q == 0: 
			countDim = count;
	

		Tq[count] = m
		count+=1
		

	##Box counting dimension
	fractalInformation = numpy.zeros(3);
	fractalInformation[0] = -1*Tq[countDim] #Fractal dimension
	
	#fractalInformation[1] = math.log(totalSandBoxes[0])/math.log(d) #Information dimension
	fractalInformation[2] = Tq[countDim+2]/2 #Correlation dimension
	plt.xlabel('ln(r/d)')
	plt.ylabel('ln(<M(r)>)^q')

	ymin, ymax = plt.ylim()
	plt.ylim((ymin, ymax+20)) 
	plt.legend(loc=9, bbox_to_anchor=(0.1, 1))
	plt.show()
	
	fig2 = plt.figure()
	plt.xlabel('q')
	plt.ylabel('T(q)')	
	plt.title("Dimension fractal generalizada "+str(fractalInformation[0]))
	plt.plot(range(minq,maxq+1), Tq,'bo-')
	plt.show()


	
			
if __name__ == "__main__":
   main(sys.argv[1:])
