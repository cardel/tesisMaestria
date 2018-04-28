import numpy
import lib.snap as snap
numpy.set_printoptions(threshold=numpy.nan)

def generateFlowerUV2_2(generations, output):	

	#First generation
	a = numpy.array([[0,1],[1,0]])
	for generation in range(2,generations+1):
		
		rows = a.shape[0]
		cols = a.shape[1]
		currentIndex = rows
		for i in range(0, rows):
			for j in range(i, cols):
				#Per each edge we add two vertices and four edges. We destroy current edge
				if a[i][j] == 1:
					#Add two vertex to Graph
					#Add two rows
					a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
					a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
					#Add two columns
					a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
					a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
					
					#Delete current edge
					a[i][j] = 0
					a[j][i] = 0
					
					#Add four edges for two vertex
					a[i][currentIndex] = 1
					a[i][currentIndex+1] = 1
					a[currentIndex][j] = 1
					a[currentIndex+1][j] = 1
					
					#Due to the graph is indirect, we must to put 1 in simetric places
					a[currentIndex][i] = 1
					a[currentIndex+1][i] = 1
					a[j][currentIndex] = 1
					a[j][currentIndex+1] = 1
					
					#Our matrix
					currentIndex+=2
	
	
	size = a.shape[0]
	G1 = snap.TUNGraph.New()
	#numpy.savetxt("grafo.csv",a,"%i",delimiter=",")
	#Add nodes
	for i in range(0,size):
		G1.AddNode(i)
	#Add edges
	for i in range(0,size):
		for j in range(i, size):
			if(a[i][j]==1):
				G1.AddEdge(i,j)
	
	snap.SavePajek(G1, output)
	
	snap.PrintInfo(G1, "Python type PUNGraph", "descriptions/"+output, False)
	result_degree = snap.TIntV()
	snap.GetDegSeqV(G1, result_degree)

	file_object = open("descriptions/"+output,'a') 
	deg = numpy.array([], dtype=int)
	file_object.write("\n")
	file_object.write("Degree\n")

	for i in range(0, result_degree.Len()):
		deg = numpy.append(deg, result_degree[i])
			
	file_object.write(numpy.array2string(deg, precision=8, separator=','))
	file_object.close()



#Generate fractal network (u,v)->flower with u = 1 and v = 3
def generateFlowerUV1_3(generations, output):	
	#First generation
	a = numpy.array([[0,1],[1,0]])
	for generation in range(2,generations+1):
		rows = a.shape[0]
		cols = a.shape[1]
		currentIndex = rows
		for i in range(0, rows):
			for j in range(i, cols):
				#Per each edge we add two vertices connected between them. We connect vertex in the current edge with new vertez
				if a[i][j] == 1:		
					#Add two rows
					a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
					a=numpy.append(a,numpy.zeros([1,a.shape[1]]),axis=0)
					#Add two columns
					a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
					a=numpy.append(a,numpy.zeros([a.shape[0],1]),axis=1)
					
					#Create an edge between new nodes					
					#Add four edges for two vertex
					a[currentIndex][currentIndex+1] = 1
					a[currentIndex+1][currentIndex] = 1

					#Connect i with current index
					a[i][currentIndex] = 1
					a[currentIndex][i] = 1					
					
					#Connect j with current index + 1
					a[j][currentIndex+1] = 1
					a[currentIndex+1][j] = 1
					
					#Our matrix
					currentIndex+=2					
								
	size = a.shape[0]
		
	G1 = snap.TUNGraph.New()
	#Add nodes
	for i in range(0,size):
		G1.AddNode(i)
	#Add edges	
	#Add edges
	for i in range(0,size):
		for j in range(i, size):
			if(a[i][j]==1):
				G1.AddEdge(i,j)
	
	snap.SavePajek(G1, output)
	
	snap.PrintInfo(G1, "Python type PUNGraph", "descriptions/"+output, False)
	result_degree = snap.TIntV()
	snap.GetDegSeqV(G1, result_degree)

	file_object = open("descriptions/"+output,'a') 
	deg = numpy.array([], dtype=int)
	file_object.write("\n")
	file_object.write("Degree\n")

	for i in range(0, result_degree.Len()):
		deg = numpy.append(deg, result_degree[i])
			
	file_object.write(numpy.array2string(deg, precision=8, separator=','))
	file_object.close()

	
if __name__ == "__main__":
	generateFlowerUV2_2(7, "floweru2v2.net")
	generateFlowerUV1_3(7, "floweru1v3.net")
