Simulated Annealing strategy
=============================

Simulated annealing algorithm for multifractal analysis


SimulatedAnnealing.SimulatedAnnealing module
--------------------------------------------

.. automodule:: SimulatedAnnealing.SimulatedAnnealing
    :members:
    :undoc-members:
    :show-inheritance:


Example
---------------

.. code-block:: python
	:emphasize-lines: 2,7
	
	import sys
	import lib.snap as snap
	import SimulatedAnnealing.SimulatedAnnealing as SimulatedAnnealing
	import numpy
	
	minq = -10
	maxq = 10	
	sizePopulation = 200 
	Kmax = 1500
	Rnd = snap.TRnd(1,0)
	graph = snap.GenPrefAttach(10000, 10,Rnd)  #ScaleFree with 10 edges per node
	
	logRD, IndexzeroD,TqD, DqD, lnMrqD = SimulatedAnnealing.SA(graph,minq,maxq,percentOfSandBoxes,sizePopulation, Kmax, 'BC')

