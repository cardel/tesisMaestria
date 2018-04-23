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
	sizeChr = chromosome.size
	averageDistance = 0.0
	averageDegree = 0.0
	percentCovered = 0.
	nodesCovered = numpy.zeros([numNodes])
	
	for node in chromosome:		
		#Box of size sqr(N)
		distanceOtherNode = 0.0
					
		for ni in chromosome:
			distanceNodeNI = distances[int(node)][int(ni)]
			distanceOtherNode+=float(distanceNodeNI)
			
		#Percent covered at radius sqr(n)	
		if(nodesCovered[int(node)]==0):
			nodesCovered[int(node)]=1		
			for i in range(0,numNodes):
				if nodesCovered[i]==0:
					distanceNodeNI = distances[int(node)][int(ni)]
					if distanceNodeNI < sqrDistance:
						nodesCovered[i]=1
					
		averageDistance += distanceOtherNode
		averageDegree += listDegree[int(node)]
	
	averageDistance= averageDistance/(numNodes*sizeChr*radius+1.)
	averageDegree = averageDegree/(sizeChr*maxDegree+1.)
	percentCovered = 100*numpy.average(nodesCovered)
	
	fitness = percentCovered*(averageDegree + averageDistance)
	return output.put((index, fitness))
	

def calculateCentersFixedSize(graph, numNodes,iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listDegree,maxDegree, sizeChromosome):
	
	population = numpy.zeros([sizePopulation,sizeChromosome])

	for i in range(0,sizePopulation):
		random = numpy.random.permutation(numNodes)[0:sizeChromosome]
		population[i] = random
		
	
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
		
			
		index =  numpy.argmax(fitness)
		best = population[index]

	return best

def calculateCenters(graph, numNodes,iterations, sizePopulation, radius, distances, percentCrossOver, percentMutation,listDegree,maxDegree):
	
	population = []
	fitNessAverage = numpy.zeros([iterations])
	fitNessMax = numpy.zeros([iterations])
	fitNessMin = numpy.zeros([iterations])
	bestFiness = 0.0
	#Random Size
	random = numpy.arange(numNodes)
	for i in range(0,sizePopulation):
		sizeRandom = rnd.randint(int(0.4*numNodes),int(0.9*numNodes))
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
				if accFiness[i-1]<=r2 and accFiness[i]>=r2:
					parent2 = population[i]	
					
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
			
		#Add new individuals to pull, and delete random individues
		for individual in newPopulation:
			index = rnd.randint(0, sizePopulation-1) 
			population[index] = individual
		
		fitNessAverage[it] = numpy.mean(fitness)
		fitNessMax[it]=numpy.max(fitness)
		fitNessMin[it]=numpy.min(fitness)
		index =  numpy.argmax(fitness)
		if bestFiness < fitness[index]:
			best = population[index]
	return best,fitNessAverage,fitNessMax,fitNessMin
#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBGenetic(graph,minq,maxq,sizePopulation, iterations, percentCrossOver, percentMutation):
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
	numNodes = graph.GetNodes()
	
	listID = snap.TIntV(numNodes)
	listDegree =  snap.TIntV(numNodes)
	maxDegree = 0.
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
