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
Arabidopsis=snap.LoadPajek(snap.PUNGraph, "cerevisiae.net")
saveResults(Arabidopsis, "Cerevisiae")

Celengs=snap.LoadPajek(snap.PUNGraph, "Celengs.net")
saveResults(Celengs, "Celengs")

Arabidopsis=snap.LoadPajek(snap.PUNGraph, "EColi.net")
saveResults(Arabidopsis, "EColi")

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
