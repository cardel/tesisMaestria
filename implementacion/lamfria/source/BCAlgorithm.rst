Box Counting algorithm
========================

This package provides multifractal analysis with Box Counting Algorithm proposed in journal article: Fractal and multifractal properties of a family of fractal networks DOI: 10.1088/1742-5468/2014/02/P02020

BoxCounting algorithm:
------------------------------

.. automodule:: BCAlgorithm.BCAlgorithm
    :members:
    :undoc-members:
    :show-inheritance:


Example
---------------

.. code-block:: python
	:emphasize-lines: 2,7
	
	import sys
	import lib.snap as snap
	import BCAlgorithm.BCAlgorithm as BCAlgorithm
	import numpy
	
	minq = -10
	maxq = 10	
	percentNodesT = 2 #200% of nodes
	Rnd = snap.TRnd(1,0)
	graph = snap.GenPrefAttach(10000, 10,Rnd)  #ScaleFree with 10 edges per node
	
	logR, Indexzero,Tq, Dq, lnMrq = BCAlgorithm.BCAlgorithm(graph,minq,maxq,percentNodesT)

