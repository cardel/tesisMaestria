#include "Snap.h"
#include "gnuplot.h"
#include "bd.h"
#include <set>
#include <cmath>
#include <algorithm> 
using std::set;
using std::min_element;
using std::max_element;
using std::advance;


int main(int argc, char* argv[]) {
	
	srand(NULL);
	//Parametros
	char* typeNet="";
	char* path="";
	for(int i=1; i<argc; i++){
		if (strcmp(argv[i],"--file")==0){
			path=argv[i+1];
		}
		if(strcmp(argv[i],"--type")==0){
			typeNet=argv[i+1];
		}
	}
	//typedef PUNGraph PGraph; //Grafo no dirigido
	PUNGraph G2;
	if(strcmp(typeNet,"edge")==0){
		G2 = TSnap::LoadEdgeList<PUNGraph>(path, 0, 1);
	}
	else{
		G2 = TSnap::LoadPajek<PUNGraph>(path);
		
	}
	//.GenPrefAttach(30, 3, snap.TRnd())	
	
	//Get lbmax (max distance in the network)
	int lbMax = TSnap::GetBfsFullDiam(G2,1000,false);
	lbMax++;
	//Number of nodes in the graph
	const int numNodes = G2->GetNodes();

	//Create vector of ID
	TVec<TInt> listaID;
	for (TUNGraph::TNodeI NI = G2->BegNI(); NI < G2->EndNI(); NI++){
		listaID.Add(NI.GetId());
	}

	//Colores
	int colorForNodeNbyLB[numNodes][lbMax];
	
	//Para el ID = 0, el color es 0
	for(int i=0; i<lbMax;i++){
		colorForNodeNbyLB[0][i]=0;
	}
	printf("%s%i\n","LbMax ",lbMax);

	//When the distance is lbMax all nodes have the same color
	/*for(int i=1; i<numNodes;i++){
		colorForNodeNbyLB[i][lbMax-1]=0;
	}*/		

	int maxColor = 0;
	for(int i=1; i<listaID.Len(); i++){	 //n (number of nodes)
		//printf("%s%i\n","Nodo: ",i);
		int distanceij[i];
		
        //Cost is n(n+1)/2 * O(b^d)        
		for(int j=0; j<i; j++){
            //Cost in worst case for each BFS execution O(b^d) where d is distance and b is factor
			distanceij[j]=TSnap::GetShortPath(G2,listaID[j],listaID[i]);
		}
		
		//I suppose to lb is n (worst case)
		//Distance is from 2 until lbMax, remember, lbMax is now lbMax+1
        for(int lb = 1; lb<=lbMax; lb++){
			//Cost is n(n+1)/2            
            set <int> nonValidColors;
            set <int> validColors;
           
			for(int j=0; j<i; j++){	
				if(distanceij[j]>=lb){
                    nonValidColors.insert(colorForNodeNbyLB[j][lb-1]);
				}
				else{
					validColors.insert(colorForNodeNbyLB[j][lb-1]);
				}
			}
            set<int> possibleColors;
            set_difference(validColors.begin(),validColors.end(),nonValidColors.begin(),nonValidColors.end(),std::inserter(possibleColors,possibleColors.begin()));
            if(possibleColors.size()>0){
				int randomPosition = rand() % possibleColors.size();  
				
				set<int>::const_iterator it(possibleColors.begin());
				advance(it,randomPosition);
				
				colorForNodeNbyLB[i][lb-1]=*(it);
            }
            else{
				set<int> unionColors;
				set_union(nonValidColors.begin(),nonValidColors.end(),validColors.begin(),validColors.end(),std::inserter(unionColors,unionColors.begin()));
				
				colorForNodeNbyLB[i][lb-1] = *max_element(unionColors.begin(),unionColors.end())+1;

			}
		}
	}

	
	//Number of boxes
	TVec<TInt> boxes;
	// lb = 0, then each node is a box
	boxes.Add(numNodes);
	for(int lb = 1; lb<lbMax; lb++){
		std::set<int> numColors;
		for(int i=0; i<numNodes; i++){
			numColors.insert(colorForNodeNbyLB[i][lb]);
		}
		boxes.Add(numColors.size());  		
	}
	for(int i=0; i<numNodes; i++){
		for(int j=0; j<lbMax;j++){
			printf("%i,",colorForNodeNbyLB[i][j]);
		}
		printf("\n");
	}
    printf("%s\t%s\n","Lb","Boxes");
	for(int i=0; i<boxes.Len(); i++){
		printf("%i\t%i\n", i+1,boxes[i].Val);
	}
}

	//int colorNodeForBox[numNodes][lbMax];
	
	////In ID = 0 assign for all lb values color 0
	
	//for(int i=0; i<lbMax; i++){
		//colorNodeForBox[0][i] = 0;	
	//}
	
	
	////For i = 1 until i = numNodes
	//int i = 1;
	//int color[lbMax];
	
	//for(int i=0; i<lbMax; i++){
		//color[i] = 0;		
	//}
	
	//for (TUNGraph::TNodeI NI = G2->BegNI(); NI < G2->EndNI(); NI++){
		//if(NI != G2->BegNI()){
		////for(int i=2; i<=numNodes; i++){
			////Calculate distance lij from i to all the nodes in the network with id j less than i
			////i is the index of the node
			
			////Calculate distance lij fron i to all nodes j
			////with j < i, all nodes j < i
			//TVec<TInt> lij;
			
			//for(TUNGraph::TNodeI NJ=G2->BegNI(); NJ<NI; NJ++){
				//int distance = TSnap::GetShortPath(G2,NI.GetId(),NJ.GetId());
				//lij.Add(distance);
			//}		
			//int lb = 1;
			
			////Repeat lb = 1 until lb = lbmax
			//while(lb<=lbMax){
				////Select on of the unused colors C[j][lij] para todos los nodos j< i for
				////which lij >= lb. This is color cilb of node i the given lb value
				
				//for(int k=0; k<lij.Len(); k++){
					////int colorBox = color[lij[k]];
					//if(lij[k]>=lb){
						//color[lij[k]]+=1;
						//colorNodeForBox[i][lij[k]] = color[lij[k]];
					//}
				//}
				//lb++;
			//}
			//i++;
		//}
	//}
	

	
