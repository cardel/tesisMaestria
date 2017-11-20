#include "Snap.h"
#include "gnuplot.h"
#include "bd.h"

int main(int argc, char* argv[]) {
	//typedef PUNGraph PGraph; //Grafo no dirigido
	typedef PNGraph PGraph; //Grafo dirigido
	
	PGraph Graph =  PGraph::TObj::New();
	Graph->AddNode(1);
	Graph->AddNode(5);
	Graph->AddEdge(1,5);
	
	//Iterar por nodos
	for (PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++){
		printf("%d %d %d\n", NI.GetId(), NI.GetOutDeg(), NI.GetInDeg());
	}
	
	//Iterar por aristas
	for (TNGraph::TEdgeI EI = Graph->BegEI(); EI < Graph->EndEI(); EI++){
		printf("edge (%d, %d)\n", EI.GetSrcNId(), EI.GetDstNId());
	}
	
	//Guardar grafo
	TIntStrH name;  //node labels
	name.AddDat(1)="1";
	name.AddDat(5)="5";
	TSnap::DrawGViz<PNGraph>(Graph, gvlDot, "gviz_plot.png", "", name);
	
	//Iterar por cada arista de cada nodo
	//Hay que cambiar el iterador segun el tipo de nodo
	for (TNGraph::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++){
		for (int e = 0; e < NI.GetOutDeg(); e++){
			printf("edge (%d %d)\n", NI.GetId(), NI.GetOutNId(e));
		}
	}
	
	//Grafica dos partes ejemplo
	TVec<TPair<TFlt,TFlt> > XY1, XY2; 
	for (int i=0; i<10; ++i)
	{
		XY1.Add(TPair<TFlt,TFlt>(i+0.0,i+0.0));
		XY2.Add(TPair<TFlt,TFlt>(i+0.0,i*i+0.0));
	} 
	
	//Plot
	TGnuPlot Gp("grafica", "Ejemplo");
	Gp.AddPlot(XY1, gpwLinesPoints, "curve1");
	Gp.AddPlot(XY2, gpwPoints, "curve2");
	Gp.SetXYLabel("x", "y");
	Gp.SavePng(); //or Gp.SaveEps();
	//You can also use log-log scale via Gp.SetScale(gpsLog10XY);	
	
	
	//Obtener grado de centralidad
	TVec<TPair<TInt, TInt> > CntV;
	TSnap::GetOutDegCnt(Graph, CntV);
	
	TGnuPlot GpX("centralida", "Grado centralidad");
	GpX.AddPlot(CntV, gpwLinesPoints, "grado centralida");
	GpX.SetXYLabel("x", "y");
	GpX.SavePng(); 
}


  //// what type of graph do you want to use?
  //typedef PUNGraph PGraph; // undirected graph
  //typedef PNGraph PGraph;  //   directed graph
  //typedef PNEGraph PGraph;  //   directed multigraph

//TUNGraph: undirected graph
//TNGraph: directed graph
// TNEANet: directed multi-graphwith attributes
