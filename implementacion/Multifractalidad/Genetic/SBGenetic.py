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
import multiprocessing as mp
import time

#Search profile about the algortihm
def calculateFitness(index,graph, chromosome,radius, distances,listDegree,maxDegree,output):
	

	numNodes = graph.GetNodes()	
	sqrDistance = int(math.sqrt(radius))
	#First position ID node, second position Fitness
	
	#Count nodes to distancie sqrt(N)
		
	averageDistance = 0.0
	averageDegree = 0.0
	punishment = 1.0
	
	for node in chromosome:
		distanceOtherNode = 0.0
		countNodesPerNode=0.0
		
		for ni in chromosome:
			distanceOtherNode+=distances[int(node)][int(ni)]/radius
			if distanceOtherNode == 0:
				punishment+=1.0
		
		averageDistance += distanceOtherNode/chromosome.size
		averageDegree += listDegree[int(node)]/(chromosome.size*maxDegree)

	fitness = (averageDegree + averageDistance)/punishment
	
	return output.put((index, fitness))

def calculateCenters(graph, numNodes,iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listDegree,maxDegree):
	
	population = []
	fitNessAverage = numpy.zeros([iterations])
	fitNessMax = numpy.zeros([iterations])
	fitNessMin = numpy.zeros([iterations])
	bestFiness = 0.0
	#Random Size
	random = numpy.arange(numNodes)
	for i in range(0,sizePopulation):
		sizeRandom = rnd.randint(1,numNodes)
		#random = numpy.random.permutation(numNodes)[0:centerNodes]
		numpy.random.shuffle(random)
		population.append(random[0:sizeRandom])

	for it in range(0,iterations):
		#Calculate fitness
		fitness = numpy.zeros([sizePopulation])
		
		#Multiprocessing
		output = mp.Queue()
		#Process
		processes = [mp.Process(target=calculateFitness, args=(index, graph, population[index],radius, distances,listDegree,maxDegree,output)) for index in range(0, sizePopulation)]
		#Start process
		for p in processes:
			p.start()

		# Exit the completed processes
		for p in processes:
			p.join()
			
		results = [output.get() for p in processes]
		
		for r in results:
			fitness[int(r[0])]=r[1]
			 
		sumFitness = numpy.sum(fitness)
		
		accFiness = fitness/sumFitness
		
		for i in range(1,sizePopulation):
			accFiness[i]+=accFiness[i-1]
		
		#Crossover, we select percent of new individuals
		numberOfNewIndividuals = int(percentCrossOver*float(sizePopulation))
		newPopulation = []
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
			size1 = numpy.size(parent1)
			size2 = numpy.size(parent2)	
			union = numpy.append(parent1,parent2)
			numpy.random.shuffle(union)
			
			totalSize = (size1 + size2)/2
			children = numpy.zeros([totalSize])
	
			#Generate children
			for g in range(0,totalSize):
				children[g] = union[g]
			
			#Mutation
			r3 = rnd.random() 
			
			#Add or remove a center
			if r3 <= percentMutation:
				#Select action
				r4 = rnd.randint(0,1)
				#Remove if it is possible
				if r4==1 and numpy.size(children)>1:
					r5 = rnd.randint(0,numpy.size(children)-1)
					children = numpy.delete(children,r5)
				else:
					#Or add an element
					r5 = rnd.randint(0,numpy.size(union)-1)
					element = union[r5]
					children = numpy.append(children,element)	
							
			newPopulation.append(children)
			
		#Add new individuals to pull, and delete worst individos
		
		for individual in newPopulation:
			#Replace a random old individual
			index = rnd.randint(0, sizePopulation-1) 
			del population[index] 
			population.append(individual)
		
		fitNessAverage[it] = numpy.average(fitness)
		fitNessMax[it]=numpy.max(fitness)
		fitNessMin[it]=numpy.min(fitness)
		index =  numpy.argmax(fitness)
		if bestFiness < fitness[index]:
			best = population[index]

	return best,fitNessAverage,fitNessMax,fitNessMin
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBGenetic(graph,minq,maxq,sizePopulation, iterations, percentCrossOver, percentMutation):
	
	d = snap.GetBfsFullDiam(graph,10,False)
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	maxDegree = 0.
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		listDegree[index] = ni.GetOutDeg()
		if listDegree[index] > maxDegree:
			maxDegree=listDegree[index]
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
	centerNodes,fitNessAverage,fitNessMax,fitNessMin = calculateCenters(graph, numNodes,iterations, sizePopulation,d,distances, percentCrossOver, percentMutation,listDegree,maxDegree)

	
	numberOfBoxes = numpy.size(centerNodes)
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
	
	return logR, Indexzero,Tq, Dq, lnMrq,iterations,fitNessAverage,fitNessMax,fitNessMin
