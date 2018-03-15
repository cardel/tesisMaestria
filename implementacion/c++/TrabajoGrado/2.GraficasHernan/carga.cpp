#include "carga.h"

int main(int argc, char* argv[]) {
	//typedef PUNGraph PGraph; //Grafo no dirigido
	typedef PNGraph PGraph; //Grafo dirigido
	PGraph G2 = TSnap::LoadPajek<PGraph>("../datos/celgans.net");

	//Iterar por nodos
	for (PGraph::TObj::TNodeI NI = G2->BegNI(); NI < G2->EndNI(); NI++){
		printf("%d %d %d\n", NI.GetId(), NI.GetOutDeg(), NI.GetInDeg());
	}

	//Obtener grado de centralidad
	TVec<TPair<TInt, TInt> > CntV;
	TSnap::GetOutDegCnt(G2, CntV);
	
	TGnuPlot GpX("distribucionGrado", "Distribucion grado");
	GpX.AddPlot(CntV, gpwLinesPoints, "Distribución grado");
	GpX.SetXYLabel("Grado", "#nodos");
	GpX.SavePng(); 	
}


