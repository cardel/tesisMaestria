import lib.snap as snap
import numpy
numpy.set_printoptions(threshold=numpy.nan)

def saveResults(graph, nameFile):
	snap.PrintInfo(graph, "Python type PUNGraph", "descriptions/"+nameFile, False)
	result_degree = snap.TIntV()
	snap.GetDegSeqV(graph, result_degree)

	file_object = open("descriptions/"+nameFile,'a') 
	deg = numpy.array([], dtype=int)
	file_object.write("\n")
	file_object.write("Degree\n")

	for i in range(0, result_degree.Len()):
		deg = numpy.append(deg, result_degree[i])
			
	file_object.write(numpy.array2string(deg, precision=8, separator=','))
	file_object.close()



Rnd = snap.TRnd()
###Scale Free
ScaleFree2000 = snap.GenPrefAttach(2000, 1, Rnd)
saveResults(ScaleFree2000, "ScaleFree2000Nodes")
snap.SaveEdgeList(ScaleFree2000, 'ScaleFree2000Nodes.txt')

ScaleFree4000 = snap.GenPrefAttach(4000, 1, Rnd)
saveResults(ScaleFree4000, "ScaleFree4000Nodes")
snap.SaveEdgeList(ScaleFree4000, 'ScaleFree4000Nodes.txt')

ScaleFree8000 = snap.GenPrefAttach(8000,1, Rnd)
saveResults(ScaleFree8000, "ScaleFree8000Nodes")
snap.SaveEdgeList(ScaleFree8000, 'ScaleFree8000Nodes.txt')
#SmallWorld

SmallWorld1 = snap.GenSmallWorld(5000, 5, 0.05, Rnd)
snap.SaveEdgeList(SmallWorld1, 'SmallWorld5000NodesRewire005.txt')
saveResults(SmallWorld1, "SmallWorld5000NodesRewire005")

SmallWorld2 = snap.GenSmallWorld(5000, 5, 0.1, Rnd)
snap.SaveEdgeList(SmallWorld2, 'SmallWorld5000NodesRewire01.txt')
saveResults(SmallWorld2, "SmallWorld5000NodesRewire01")

SmallWorld3 = snap.GenSmallWorld(5000, 5, 0.2, Rnd)
snap.SaveEdgeList(SmallWorld3, 'SmallWorld5000NodesRewire02.txt')
saveResults(SmallWorld3, "SmallWorld5000NodesRewire02")

Random1 =snap.GenRndGnm(snap.PUNGraph, 1991, 5939)
snap.SaveEdgeList(Random1, 'Random1991Nodes5939.txt')
saveResults(Random1, "Random1991Nodes5939")

Random2 =snap.GenRndGnm(snap.PUNGraph, 3373, 5978)
snap.SaveEdgeList(Random2, 'Random3373Nodes5978.txt')
saveResults(Random2, "Random3373Nodes5978")

Random3 =snap.GenRndGnm(snap.PUNGraph, 5620, 8804)
snap.SaveEdgeList(Random3, 'Random5620Nodes8804.txt')
saveResults(Random3, "Random5620Nodes8804")
#Random

#G2 = snap.GenPrefAttach(500, 50,Rnd)
#snap.SaveEdgeList(G2, 'paperScaleFree500-499.txt')

#G3 =snap.GenRndGnm(snap.PUNGraph, 449, 610)
#snap.SaveEdgeList(G3, 'paperRandom449-610.txt')

#UGraph = snap.GenPrefAttach(8000,1, Rnd)
#print UGraph.GetNodes()
#print UGraph.GetEdges()

#result_degree = snap.TIntV()
#snap.GetDegSeqV(UGraph, result_degree)
#d = snap.GetBfsFullDiam(UGraph,1,False)

#Nodes = snap.TIntFltH()
#Edges = snap.TIntPrFltH()
#snap.GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)

#for NI in UGraph.Nodes():
    #CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
    #print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
    
#snap.PrintInfo(UGraph, "Python type PNGraph", "info-pngraph2.txt", False)
