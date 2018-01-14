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

//Lb is calculated with potencial regression
double calculateLb(TVec<TInt> boxes){
	double lb = 0;
	
	//Calculate others
	double sumLogX = 0;
	double sumLogY = 0;
	double sumLogXLogY = 0;
	double sumQuadLogX = 0;
	int N = boxes.Len();
	
	for(int i=0; i<boxes.Len(); i++){
		int x = i+1;
		int y = boxes[i].Val;
		
		sumLogX+=log10(x);
		sumLogY+=log10(y);
		sumLogXLogY+=(log10(x)*log10(y));
		sumQuadLogX+=(log10(x)*log10(x));
	}	
	
	lb = (-1)*(N*sumLogXLogY - sumLogX*sumLogY)/(N*sumQuadLogX-sumLogX*sumLogX);
	
	return lb;	
}

int main(int argc, char* argv[]) {
	
	srand(NULL);
	//Parameters
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

	//Get lbmax
	int lbMax = TSnap::GetBfsFullDiam(G2,1000,false);
	lbMax++;
	

	for(int i=1; i<=lbMax; i++){
		//Create set of nodes
		//Create vector of ID
		set<TUNGraph::TNodeI> nodes;
		for (TUNGraph::TNodeI NI = G2->BegNI(); NI < G2->EndNI(); NI++){
			nodes.insert(NI);
		}	
				

		
		while(!nodes.empty()){
			//Select a random node
			int nodeRand = rand() % nodes.size(); 
			TUNGraph::TNodeI startNode = G2-> GetNI(nodeRand);
			
			//Remove this node
			nodes.erase (nodes.find(startNode));	
			
			//Remove all nodes whose distance is 
			
			set<TUNGraph::TNodeI>::iterator it;
			
			for(it=nodes.begin(); it!=nodes.end(); ++it){
				int distance = TSnap::GetShortPath(G2,startNode.GetId(),(*it).GetId());	
				
			}
			
		}
		
		
			
	}
	
	
}
