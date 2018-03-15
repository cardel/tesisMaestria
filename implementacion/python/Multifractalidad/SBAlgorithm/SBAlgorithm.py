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
		
	#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
	
	#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
	
	d = snap.GetBfsFullDiam(grafo,10,False)
	numNodes = grafo.GetNodes()
	initialSandBoxes = (int)(0.2*numNodes)
	
	for radius in range(1,d+1):
		
		#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.
		
		#I generate a permutation of 20 percent of nodes
		
		randomIndex = numpy.random.permutation(initialSandBoxes)
	
if __name__ == "__main__":
   main(sys.argv[1:])
