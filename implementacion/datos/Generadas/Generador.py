import lib.snap as snap

Rnd = snap.TRnd(1,0)
G1 = snap.GenSmallWorld(500, 25, 0.05, Rnd)
snap.SaveEdgeList(G1, 'smallWorld5500-2515.txt')


G2 = snap.GenGeoPrefAttach(500, 499,0.25,Rnd)
snap.SaveEdgeList(G2, 'paperScaleFree500-499.txt')

G3 =snap.GenRndGnm(snap.PUNGraph, 449, 610)
snap.SaveEdgeList(G3, 'paperRandom449-610.txt')
