#include "Snap.h"
#include "gnuplot.h"
#include "bd.h"
#include <set>
#include <algorithm> 
#include <ctime> 
#include <cstdlib>  
#include <cmath>

int main(int argc, char* argv[]) {
	
	srand (time(NULL));
	typedef PUNGraph PGraph; //Grafo no dirigido
	//PGraph G2 = TSnap::LoadPajek<PGraph>(argv[1]);
	PGraph G2 = TSnap::LoadEdgeList<PGraph>(argv[1], 0, 1);
	//.GenPrefAttach(30, 3, snap.TRnd())
	//Get lbmax (max distance in the network)
	int lbMax = TSnap::GetBfsFullDiam(G2,1000,false);
	
	//Number of nodes in the graph
	const int numNodes = G2->GetNodes();
	//printf("%i\n", lbMax);
	//printf("%d",numNodes);
	//The rank of the nodes is implicit, because iterator of the line 15

	int colorNodeForBox[numNodes][lbMax];
	
	//In ID = 0 assign for all lb values color 0
	
	for(int i=0; i<lbMax; i++){
		colorNodeForBox[0][i] = 0;	
	}
	
	
	//For i = 1 until i = numNodes
	int i = 1;
	int color[lbMax];
	
	for(int i=0; i<lbMax; i++){
		color[i] = 0;		
	}
	
	for (TUNGraph::TNodeI NI = G2->BegNI(); NI < G2->EndNI(); NI++){
		if(NI != G2->BegNI()){
		//for(int i=2; i<=numNodes; i++){
			//Calculate distance lij from i to all the nodes in the network with id j less than i
			//i is the index of the node
			
			//Calculate distance lij fron i to all nodes j
			//with j < i, all nodes j < i
			TVec<TInt> lij;
			
			for(TUNGraph::TNodeI NJ=G2->BegNI(); NJ<NI; NJ++){
				int distance = TSnap::GetShortPath(G2,NI.GetId(),NJ.GetId());
				lij.Add(distance);
			}		
			int lb = 1;
			
			//Repeat lb = 1 until lb = lbmax
			while(lb<=lbMax){
				//Select on of the unused colors C[j][lij] para todos los nodos j< i for
				//which lij >= lb. This is color cilb of node i the given lb value
				
				for(int k=0; k<lij.Len(); k++){
					//int colorBox = color[lij[k]];
					if(lij[k]>=lb){
						color[lij[k]]+=1;
						colorNodeForBox[i][lij[k]] = color[lij[k]];
					}
				}
				lb++;
			}
			i++;
		}
	}
	
	
	//Number of boxes
	TVec<TInt> boxes;
	for(int lb = 0; lb<lbMax; lb++){
		//if lb = 0, then each node is a box
		if(lb == 0){
			boxes.Add(numNodes);
		}
		else{
			std::set<int> numColors;
			for(int i=0; i<numNodes; i++){
				numColors.insert(colorNodeForBox[i][lb]);
			}
			boxes.Add(numColors.size());  		
		}
	}
	int minimumBox = numNodes;
	int lbPosition = 0;
	for(int i=0; i<boxes.Len(); i++){
		if(boxes[i].Val<minimumBox){
			lbPosition = i;
			minimumBox = boxes[i].Val;
		}
		printf("%i\n", boxes[i].Val);
	}
	//lb + 1 due to the assumpsion of position
	double db = log2(minimumBox)/log2(lbPosition+1);
	printf("%f,%i",db,lbMax);
}



	
