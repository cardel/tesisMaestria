SandBox Algorithm
===================

This package provides multifractal analysis with SandBox Algorithm proposed in journal article: Determination of multifractal dimensions of complex networks by means of the sandbox algorithm DOI: 10.1063/1.4907557

SBAlgorithm
------------------------------

.. automodule:: SBAlgorithm.SBAlgorithm
    :members:
    :undoc-members: 
    :show-inheritance:
    
Example
---------------

.. code-block:: python
	:emphasize-lines: 2,7
	
	import sys
	import lib.snap as snap
	import SBAlgorithm.SBAlgorithm as SBAlgorithm
	import numpy
	
	minq = -10
	maxq = 10	
	percentOfSandBoxes = 0.6
	repetitionsSB = 50
	Rnd = snap.TRnd(1,0)
	graph = snap.GenPrefAttach(10000, 10,Rnd)  #ScaleFree with 10 edges per node
	
	logRB, IndexzeroB,TqB, DqB, lnMrqB = SBAlgorithm.SBAlgorithm(graph,minq,maxq,percentOfSandBoxes,repetitionsSB)

