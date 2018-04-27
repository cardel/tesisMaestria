#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 18th April 2018
#Last edition date 18th April 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import numpy
import math
import sys
import random as rnd
from sets import Set
import lib.snap as snap
import utils.utils as utils
import SBAlgorithm.SBAlgorithm as SBAlgorithm
import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm
import BCAlgorithm.BCAlgorithm as BCAlgorithm

#Search profile about the algortihm
def calculateFitness(graph, chromosome,radius, distances,listDegree,maxDegree):
	
	totalDegree = numpy.array([], dtype=float)
	totalDistanceOtherNodes = numpy.array([], dtype=float)
	sizeC = numpy.size(chromosome)
	
	for node in chromosome:		
		totalDegree=numpy.append(totalDegree,listDegree[int(node)])
		totalDistIn = 0.
		for ni in chromosome:
			totalDistIn += distances[int(node)][int(ni)]
			
		totalDistanceOtherNodes=numpy.append(totalDistanceOtherNodes,totalDistIn/sizeC)
	
	totalDista = numpy.average(totalDistanceOtherNodes)/radius
	totalDeg =  numpy.average(totalDegree)/maxDegree
	return 100*(totalDista*totalDeg)

def calculateCentersFixedSize(graph, numNodes,iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listDegree,maxDegree, sizeChromosome,degreeOfBoring):
	
	population = numpy.zeros([sizePopulation,sizeChromosome])
	fitNessAverage = numpy.array([])
	fitNessMax =  numpy.array([])
	fitNessMin =  numpy.array([])	
	boring = 0
	
	for i in range(0,sizePopulation):
		random = numpy.random.permutation(numNodes)[0:sizeChromosome]
		population[i] = random
		
	best=population[0]
	bestFiness = 0.0
	
	for it in range(0,iterations):
		#Calculate fitness
		fitness = numpy.zeros([sizePopulation])	
		

		for index in range(0, sizePopulation):
			chromosome = population[index]
			fitness[index] = calculateFitness(graph, chromosome,radius, distances,listDegree,maxDegree)
			 
		#Stop condition
		fitNessAverage=numpy.append(fitNessAverage,numpy.mean(fitness))
		fitNessMax=numpy.append(fitNessMax,numpy.max(fitness))
		fitNessMin=numpy.append(fitNessMin,numpy.min(fitness))
		indexB =  numpy.argmax(fitness)
		currentBestFitness=fitness[indexB]

		if bestFiness < fitness[indexB]:
			best = population[indexB]
			bestFiness = currentBestFitness
			boring=0
		else:
			boring+=1
			
		if(boring>degreeOfBoring):
				return best
		##Select nodes Fitness proportionate selection
		sumFitness = numpy.sum(fitness)
		accFiness = fitness/sumFitness
		
		for i in range(1,sizePopulation):
			accFiness[i]+=accFiness[i-1]
		#Crossover, we select percent of new individuals
		numberOfNewIndividuals = int(math.ceil(percentCrossOver*float(sizePopulation)))
		newPopulation = numpy.array([[],[]])
		for i in range(0, numberOfNewIndividuals):
			#Select parents
			r1 = rnd.random() 
			r2 = rnd.random() 
			parent1 = population[0]
			parent2 = population[0]
			#Search individuals
			for j in range(1,sizePopulation):
				if accFiness[j-1]<=r1 and accFiness[j]>=r1:
					parent1 = population[j]
					break
				if accFiness[j-1]<=r2 and accFiness[j]>=r2:
					parent2 = population[j]
					break

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
				
			
		#Add new individuals to pull,delete worst individuals
		orderFitness = numpy.argsort(-fitness)
		index = 0
		for individual in newPopulation:
			#Replace a random old individual
			index = rnd.randint(0, sizePopulation-1) 
			population[orderFitness[index]] = individual
			index+=1			

	return best

def calculateCenters(graph, numNodes,iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listDegree,maxDegree,degreeOfBoring):
	
	population = []
	fitNessAverage = numpy.array([])
	fitNessMax =  numpy.array([])
	fitNessMin =  numpy.array([])
	bestFiness = 0.0
	boring = 0
	#Random Size
	rand = numpy.arange(numNodes)
	for i in range(0,sizePopulation):
		sizeRandom = rnd.randint(int(0.4*numNodes),int(0.9*numNodes))
		numpy.random.shuffle(rand)
		population.append(rand[0:sizeRandom])
	
	best=population[0]
	fitness = numpy.zeros([sizePopulation])
	for it in range(0,iterations):	#Calculate fitness	
		
		for index in range(0, sizePopulation):
			chromosome = population[index]
			fitness[index] = calculateFitness(graph, chromosome,radius, distances,listDegree,maxDegree)
		
		#Stop condition
		fitNessAverage=numpy.append(fitNessAverage,numpy.mean(fitness))
		fitNessMax=numpy.append(fitNessMax,numpy.max(fitness))
		fitNessMin=numpy.append(fitNessMin,numpy.min(fitness))
		indexB =  numpy.argmax(fitness)
		currentBestFitness=fitness[indexB]
		
		if bestFiness < fitness[indexB]:
			best = population[indexB]
			bestFiness = currentBestFitness
			boring=0
		else:
			boring+=1
			
		if(boring>degreeOfBoring):
			return best,fitNessAverage,fitNessMax,fitNessMin


		sumFitness = numpy.sum(fitness)
		
		accFiness = fitness/sumFitness
		
		for i in range(1,sizePopulation):
			accFiness[i]+=accFiness[i-1]
		
		#Crossover, we select percent of new individuals
		
		numberOfNewIndividuals = int(math.ceil(percentCrossOver*float(sizePopulation)))
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
					break
				if accFiness[i-1]<=r2 and accFiness[i]>=r2:
					parent2 = population[i]	
					break			
			#Cross	
			size1 = numpy.size(parent1)
			size2 = numpy.size(parent2)	
			union = numpy.unique(numpy.append(parent1,parent2))
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
				if r4==1 and numpy.size(children)>int(0.4*numNodes):
					r5 = rnd.randint(0,numpy.size(children)-1)
					children = numpy.delete(children,r5)
				else:
					#Or add an element
					if numpy.size(children)<int(0.9*numNodes):
						r5 = rnd.randint(0,numpy.size(union)-1)
						element = union[r5]
						children = numpy.unique(numpy.append(children,element))	
							
			newPopulation.append(children)
			
		#Add new individuals to pull,delete worst individuals
		orderFitness = numpy.argsort(-fitness)
		index = 0
		for individual in newPopulation:
			#Replace a random old individual
			index = rnd.randint(0, sizePopulation-1) 
			population[orderFitness[index]] = individual
			index+=1	
			
					
	return best, fitNessAverage,fitNessMax,fitNessMin
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def Genetic(g,minq,maxq,sizePopulation, iterations, percentCrossOver, percentMutation, degreeOfBoring, typeAlgorithm):
	"""Insert a function and its arguments in process pool.
  
	Input is inserted in queues using a round-robin fashion. Every job is
	identified by and index that is returned by function. Not all parameters
	of original multiprocessing.Pool.apply_aync are implemented so far.
  
	:param func: Function to process.
	:type func: Callable.
	:param args: Arguments for the function to process.
	:type args: Tuple.
	:returns: Assigned job id.
	:rtype: Int.
        """		
	graph = snap.GetMxScc(g)
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	maxDegree = 0.
	totalIterations = 0.
	index = 0
	for ni in graph.Nodes():
		listID[index] = ni.GetId()
		listDegree[index] = int(ni.GetOutDeg())
		if listDegree[index] > maxDegree:
			maxDegree=listDegree[index]
		index+=1
	
	d = snap.GetBfsFullDiam(graph,1,False)
	
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
	centerNodes,fitNessAverage,fitNessMax,fitNessMin = calculateCenters(graph, numNodes,iterations, sizePopulation,d,distances, percentCrossOver, percentMutation,listDegree,maxDegree,degreeOfBoring)

	logR = []
	Indexzero = 0
	Tq = []
	Dq = []
	lnMrq = []

	
	if typeAlgorithm=='SB':
		groupCenters = []
		groupCenters.append(centerNodes)
		logR, Indexzero,Tq, Dq, lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,1,1, centerNodes)	
	elif typeAlgorithm=='BCFS':
		#Complete nodes
		#This methos is too exactly, then I repeat 100 tiemes this process
		groupCenters = []
		nodes = numpy.arange(numNodes)	
		otherNodes = numpy.setdiff1d(nodes, centerNodes)	
		for i in range(0,100):		
			
			newNodes = numpy.append(centerNodes,otherNodes)
			numpy.random.shuffle(nodes)
			numpy.random.shuffle(centerNodes)
			groupCenters.append(newNodes)
		logR, Indexzero,Tq, Dq, lnMrq = FSBCAlgorithm.FSBCAlgorithm(g,minq,maxq,1,1, groupCenters)
	elif typeAlgorithm=='BC':
		#Complete nodes
		#This methos is too exactly, then I repeat 100 tiemes this process
		groupCenters = []
		nodes = numpy.arange(numNodes)	
		otherNodes = numpy.setdiff1d(nodes, centerNodes)	
		for i in range(0,100):		
			
			newNodes = numpy.append(centerNodes,otherNodes)
			numpy.random.shuffle(nodes)
			numpy.random.shuffle(centerNodes)
			groupCenters.append(newNodes)
		logR, Indexzero,Tq, Dq, lnMrq = FSBCAlgorithm.FSBCAlgorithm(g,minq,maxq,1,1, groupCenters)
	else:
		print "SBGenetic: Invalid option of Algorithm"
		sys.exit(0)

	return logR, Indexzero,Tq, Dq, lnMrq,fitNessAverage,fitNessMax,fitNessMin
