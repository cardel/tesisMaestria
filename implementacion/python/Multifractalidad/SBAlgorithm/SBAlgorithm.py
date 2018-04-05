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

def linealRegresssion(x, y):

	m = 0
	b = 0
	n = numpy.size(x)
	sumXplusY = numpy.sum(numpy.dot(x,y))
	sumXplusX = numpy.sum(numpy.dot(x,x))
	sumX = numpy.sum(x)
	sumY = numpy.sum(y)
	m = (n*sumXplusY - sumX*sumY)/(n*sumXplusX-sumX*sumX)
	b = (sumY - m*sumX)/n
	
	
	return m,b

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

	
	
	if typeNet == "Edge":
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	elif typeNet == "ConnList":
		grafo = snap.LoadConnList(snap.PUNGraph, fileInput)
	elif typeNet == "Pajek":
		grafo = snap.LoadPajek(snap.PUNGraph, fileInput)
	elif typeNet == "TinyWorld":
		Rnd = snap.TRnd(1,0)
		grafo = snap.GenSmallWorld(200, 3, 0, Rnd)
	elif typeNet == "ScaleFree":
		grafo = snap.GenRndPowerLaw(200, 3)
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
	maxq = 10
	#Mass Exponents
	Tq = numpy.zeros(maxq-minq)
	
	
	#Permutation of 20 percent of nodes8
	randomNodes = numpy.random.permutation(listaID)	
		
	
	totalSandBoxes = numpy.array([])
	logR = numpy.array([])
	for radius in range(1,d+1):
		#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.

		#setOfNodes = Set(listaID)
		sandBoxes = numpy.array([])
				 
		logR = numpy.append(logR,math.log(float(radius)/d))
		
		for i in range(0,int(0.4*numpy.size(randomNodes))):
			currentNode = int(randomNodes[i])
			countNodes = 0
			#Discard current node
			for ni in grafo.Nodes():
				distance = snap.GetShortPath(grafo,ni.GetId(),currentNode);
				if  distance <= radius and distance > 0:
					countNodes+=1
			sandBoxes = numpy.append(sandBoxes,countNodes)
		totalSandBoxes = numpy.append(totalSandBoxes,numpy.average(sandBoxes)) 

	#Calculate Dq, variate q from 0 to 10	
	count = 0	
	countDim = 0;
	fractalInformation = numpy.zeros(3);
	for q in range(minq,maxq,1):	
		if q==0:
			countDim = count
				
		totalSandBoxesLog = numpy.log(numpy.power(totalSandBoxes,q-1))
		if math.fmod(q,4)==0:
			plt.plot(logR,totalSandBoxesLog,symbols[int(math.fmod(count,numpy.size(symbols)))], label="q="+str(q))
		m,b = linealRegresssion(logR,totalSandBoxesLog)
		Tq[count] = m
		count+=1
		
	
	
	#Box counting dimension
	fractalInformation[0] = -1*Tq[countDim] #Fractal dimension
	fractalInformation[1] = math.log(totalSandBoxes[0])/math.log(d) #Information dimension
	fractalInformation[2] = Tq[countDim+2]/2 #Correlation dimension
	print fractalInformation
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
	plt.plot(range(minq,maxq), Tq,'o-r')
	plt.show()
			
if __name__ == "__main__":
   main(sys.argv[1:])
