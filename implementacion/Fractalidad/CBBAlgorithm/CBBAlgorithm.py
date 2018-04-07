#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Last edition date 14th March 2018
#Description: This algorithm calculates the fractal dimension with CBB method
import snap
import sys
import getopt
import numpy
import random
import math
from datetime import datetime

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
	numNodes = grafo.GetNodes()
	uncoveredNodes = []
	setBoxes = []
	
	for lb in range(1,lbMax):
		
		setBoxes.append([])
		
		for ni in grafo.Nodes():
			uncoveredNodes.append(ni.GetId())
			
			
		while len(uncoveredNodes) > 0:
			positionRandom = random.randint(0, len(uncoveredNodes)-1)
			
			node = uncoveredNodes[positionRandom]
			#Remove this node
			uncoveredNodes.remove(node)
			#Candidate set
			candidateSet = [node]
			for nd in uncoveredNodes:
				distance=snap.GetShortPath(grafo,node,nd)
				
				if distance < lb:
					candidateSet.append(nd)
					uncoveredNodes.remove(nd)
				
			setBoxes[lb-1].append(candidateSet)
			
	boxes = snap.TIntV()
	
	#boxes.Add(numNodes)
	
	for lb in range(0,lbMax-1):
		boxes.Add(len(setBoxes[lb]))
	
	boxes.Add(1)
	print("Lb","Boxes")
	
	for i in range(0,boxes.Len()):
		print(i+1,boxes[i])
		
	lb = calculateLb(boxes)
	print("The dimension fractal is: ",lb)
	
if __name__ == "__main__":
   main(sys.argv[1:])
