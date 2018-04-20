#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 18th April 2018
#Last edition date 18th April 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import numpy
import math
import random as rnd
from sets import Set
import lib.snap as snap
import utils.utils as utils
from joblib import Parallel, delayed
import time

		
#Search profile about the algortihm
def calculateFitness(graph, population, sizePopulation,radius, distances,listID,listDegree):
	

	numNodes = graph.GetNodes()	
	sqrDistance = int(math.sqrt(radius))
	#First position ID node, second position Fitness
	fitness = numpy.zeros([sizePopulation])
	
	#Count nodes to distancie sqrt(N)
	
	for i in range(0,sizePopulation):
		
		averageDistance = 0.0
		chromosome = population[i]
		averageDegree = 0.0
		
		for node in chromosome:
			distanceOtherNode = 0.0
			countNodesPerNode=0.0
			
			for ni in chromosome:
				distanceOtherNode+=distances[int(node)][int(ni)]
			
			averageDistance += distanceOtherNode/chromosome.size
			averageDegree += listDegree[int(node)]/chromosome.size

		fitness[i] = averageDistance + averageDistance
	
	return fitness

def calculateCenters(graph, numNodes,percentSandBox, iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listID,listDegree):

	sizeChromosome = int(percentSandBox*numNodes);
	population = numpy.zeros([sizePopulation,sizeChromosome])

	#Initial will be degree (highest)
	#Heurusitca para eso. %Highs restos son middles
	for i in range(0,sizePopulation):
		random = numpy.random.permutation(numNodes)[0:sizeChromosome]
		population[i] = random
		
	totalStartTime = time.time()	
	#Grado deaburrimiento 5% variación
	for i in range(0,iterations):
		#Calculate fitness
		fitness = calculateFitness(graph, population, sizePopulation,radius, distances,listID,listDegree)
		##Select nodes Fitness proportionate selection
		sumFitness = numpy.sum(fitness)
		
		accFiness = fitness/sumFitness
		
		for i in range(1,sizePopulation):
			accFiness[i]+=accFiness[i-1]
		
		#Crossover, we select percent of new individuals
		numberOfNewIndividuals = int(percentCrossOver*sizePopulation)
		newPopulation = numpy.array([[],[]])
		for i in range(0, numberOfNewIndividuals):
			#Select parents
			r1 = rnd.random() 
			r2 = rnd.random() 
			parent1 = population[0]
			parent2 = population[0]
			#Search individuals
			for i in range(1,sizePopulation):
				if accFiness[i-1]<=r1 and accFiness[i]>=r1:
					parent1 = population[i]
				if accFiness[i-1]<=r2 and accFiness[i]>=r2:
					parent2 = population[i]	
			
		
			#Cross		
			individual = numpy.random.permutation(numpy.unique(numpy.append(parent1,parent2)))[0:sizeChromosome]
			
			#Mutation
			r3 = rnd.random() 
			
			#Cambiar el nodo por uno cualquiera
			if r3 <= percentMutation:
				#Select node to change
				r4 = rnd.randint(0,sizeChromosome-1)
				#Select random node				
				newElement = rnd.randint(0, numNodes-1) 
				
				if numpy.size(numpy.where(individual==newElement))==0:
					individual[r4] = newElement
						
			if numpy.size(newPopulation)==0:
				newPopulation = individual
			else:
				newPopulation = numpy.vstack((newPopulation,individual))
				
			
		#Add new individuals to pull, and delete randomly old individuals
		for individual in newPopulation:
			#Replace a random old individual
			index = rnd.randint(0, sizePopulation-1) 
			population[i] = individual
		
		#print numpy.average(fitness)
		
	#Fitness 100th generation
	fitness = calculateFitness(graph, population, sizePopulation,radius, distances,listID,listDegree)
	index =  numpy.argmax(fitness)
	best = population[index]
		
	return best
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBGenetic(graph,minq,maxq,percentSandBox,sizePopulation, iterations, percentCrossOver, percentMutation):
	
	d = snap.GetBfsFullDiam(graph,10,False)
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		listDegree[index] = ni.GetOutDeg()
		index+=1

	rangeQ = maxq-minq+1
	#Total q
	lnMrq = numpy.zeros([rangeQ,d],dtype=float)
	
	#Mass Exponents
	Tq = numpy.zeros(rangeQ)
	
	#Generalized dimensions
	Dq = numpy.zeros(rangeQ)
	
	##High computational cost operation
	##I generated a matriz with distancies between nodes
	distances = utils.getDistancesMatrix(graph,numNodes, listID)	
	#Create a random population of nodes	
	centerNodes = calculateCenters(graph, numNodes,percentSandBox, iterations, sizePopulation,d,distances, percentCrossOver, percentMutation,listID,listDegree)

	numberOfBoxes = int(percentSandBox*numNodes);
	sandBoxes = numpy.zeros([d,numberOfBoxes])
	logR = numpy.array([])
		
	for radius in range(1,d+1):
		
		logR = numpy.append(logR,math.log(float(radius)/d))
		i = 0
		for currentNode in centerNodes:
			countNodes = 1
			#print i, radius
			for ni in range(0, numNodes):
				distance = distances[int(currentNode)][ni]
				if  distance <= radius and distance > 0:
					countNodes+=1
			sandBoxes[radius-1][i] = countNodes
			i+=1
	
	count = 0
	Indexzero  = 0 
	
	for q in range(minq,maxq+1,1):
		i = 0
		for sand in sandBoxes:
			Mr = numpy.power(sand,q-1)
			Mr = numpy.log(numpy.average(Mr))
			lnMrq[count][i]=Mr
			i+=1
			
	
		m,b = utils.linealRegresssion(logR,lnMrq)
		#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
		#Find the mass exponents
		if q == 0: 
			countDim = count;
	

		Tq[count] = m
		
		#Find the Generalizated Fractal dimensions
		if q != 1:
			m,b = utils.linealRegresssion((q-1)*logR,lnMrq[count])
		else:
			Z1e = numpy.array([])
			for sand in sandBoxes:
				Ze = numpy.log(sand)
				Ze = numpy.average(Ze)
				Z1e = numpy.append(Z1e,Ze)
			m,b = utils.linealRegresssion(logR,Z1e)	
		Dq[count] = m
		if q == 0:
			Indexzero = count

		count+=1
	
	return logR, Indexzero,Tq, Dq, lnMrq
