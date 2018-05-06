Genetic strategy
==================

Genetic algorithm for multifractal analysis

Genetic
------------------------------

.. automodule:: Genetic.Genetic
    :members:
    :undoc-members: 
    :show-inheritance:
    
Example
---------------

.. code-block:: python
	:emphasize-lines: 2,7
	
	import sys
	import lib.snap as snap
	import Genetic.Genetic as Genetic
	import numpy
	
	minq = -10
	maxq = 10	
	sizePopulation = 200 
	percentCrossOver = 0.4
	percentMutation = 0.05	
	degreeOfBoring = 20
	Rnd = snap.TRnd(1,0)
	graph = snap.GenPrefAttach(10000, 10,Rnd)  #ScaleFree with 10 edges per node
	
	logR, Indexzero,Tq, Dq, lnMrq,fitNessAverage,fitNessMax,fitNessMin = Genetic.Genetic(graph,minq,maxq,sizePopulation,iterations, percentCrossOver, percentMutation,degreeOfBoring, 'SB')	



