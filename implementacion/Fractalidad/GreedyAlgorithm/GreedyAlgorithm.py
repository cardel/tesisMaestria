#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th March 2018
#Description: This algorithm calculates the fractal dimension with Greedy method

import snap
import sys
import getopt
import numpy
import random
import math
from datetime import datetime

from sets import Set

def calculateLb(boxes):
	lb = 0.0
	
	#Calculate others
	sumLogX = 0
	sumLogY = 0
	sumLogXLogY = 0
	sumQuadLogX = 0
	N = boxes.Len();
	
	for i in range(0, boxes.Len()):
		x = i+1;
		y = boxes[i];
		
		sumLogX+=math.log10(x)
		sumLogY+=math.log10(y)
		sumLogXLogY+=(math.log10(x)*math.log10(y))
		sumQuadLogX+=(math.log10(x)*math.log10(x))
	
	lb = (-1)*(N*sumLogXLogY - sumLogX*sumLogY)/(N*sumQuadLogX-sumLogX*sumLogX)
	return lb




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
	else:
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')

	#Get lbmax (max distance in the network)
	lbMax = snap.GetBfsFullDiam(grafo,10,False)
	lbMax+=1
	
	listaID = snap.TIntV()
	for ni in grafo.Nodes():
		listaID.Add(ni.GetId())
	
	numNodes = grafo.GetNodes()
	colorForNodeNbyLB = numpy.zeros((numNodes,lbMax),dtype=int)
	maxColor = 0;
	
	for i in range(1,listaID.Len()):
		distanceij = numpy.zeros(i)
		
		for j in range(0,i):
			distanceij[j]=snap.GetShortPath(grafo,listaID[j],listaID[i]);
			
			
		for lb in range(1,lbMax):
			nonValidColors = Set()
			validColors = Set()
			
			for j in range(0,i):
				if distanceij[j]>=lb:
					nonValidColors.add(colorForNodeNbyLB[j][lb-1])
				else:
					validColors.add(colorForNodeNbyLB[j][lb-1])
			
			possibleColors = validColors - nonValidColors
			
			if len(possibleColors) > 0:
				colorForNodeNbyLB[i][lb-1] = next(iter(possibleColors))
			else:
				unionColors = validColors | nonValidColors
				colorForNodeNbyLB[i][lb-1] = max(unionColors) + 1
	
	boxes = snap.TIntV()
	
	for lb in range(0,lbMax):
		numColors = Set()
		
		for i in range(0, numNodes):
			numColors.add(colorForNodeNbyLB[i][lb])
			
		boxes.Add(len(numColors))
	
	print("Lb","Boxes")
	
	for i in range(0,boxes.Len()):
		print(i+1,boxes[i])
		
	lb = calculateLb(boxes)
	print("The dimension fractal is: ",lb)

if __name__ == "__main__":
   main(sys.argv[1:])
