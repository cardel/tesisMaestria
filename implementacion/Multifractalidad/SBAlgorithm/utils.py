#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 07th April 2018
#Last edition date 07th April 2018
#Description: This file contains some utilities for multifractality app
import numpy
import snap

def generateFlowerUV():
	
	a = numpy.genfromtxt('flower223thGeneration.csv', delimiter=',')
	size = 44
	G1 = snap.TUNGraph.New()
	#Add nodes
	for i in range(0,size):
		G1.AddNode(i)
	#Add edges
	for i in range(0,size):
		for j in range(i, size):
			if(a[i][j]==1):
				G1.AddEdge(i,j)
	
	return G1

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
