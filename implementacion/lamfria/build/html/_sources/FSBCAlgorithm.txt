FSBCAlgorithm package
=====================

This package provides multifractal analysis with Box Counting Fixed Size Algorithm proposed in journal article: Multifractal analysis of complex networks DOI: 10.1088/1674-1056/21/8/080504


Box Counting Fixed Size module
----------------------------------

.. automodule:: FSBCAlgorithm.FSBCAlgorithm
    :members:
    :undoc-members:
    :show-inheritance:


Example
---------------

.. code-block:: python
	:emphasize-lines: 2,7
	
	import sys
	import lib.snap as snap
	import FSBCAlgorithm.FSBCAlgorithm as FSBCAlgorithm
	import numpy
	
	minq = -10
	maxq = 10	
	percentNodesT = 2 #200% of nodes
	Rnd = snap.TRnd(1,0)
	graph = snap.GenPrefAttach(10000, 10,Rnd)  #ScaleFree with 10 edges per node
	
	logR, Indexzero,Tq, Dq, lnMrq = FSBCAlgorithm.FSBCAlgorithm(graph,minq,maxq,percentNodesT)
