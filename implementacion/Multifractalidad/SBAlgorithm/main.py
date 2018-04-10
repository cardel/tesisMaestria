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
import utils

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
	elif typeNet == "ScaleFree":
		grafo = snap.GenRndPowerLaw(300, 1.5)
	elif typeNet == "ScaleFree":
		grafo = snap.GenPrefAttach(400, 30,Rnd)
	elif typeNet == "Random":
		grafo = snap.GenRndGnm(snap.PUNGraph, 300, 1200)
	elif typeNet == "Flower":
		grafo = utils.generateFlowerUV()
	else:
		grafo = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1, ' ')
	
	SBAlgorithm.SBAlgorithm(grafo)
			
if __name__ == "__main__":
   main(sys.argv[1:])

