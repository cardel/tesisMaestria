import lib.snap as snap

Rnd = snap.TRnd()
G1 = snap.GenSmallWorld(500, 25, 0.05, Rnd)
snap.SaveEdgeList(G1, 'smallWorld5500-2515.txt')


G2 = snap.GenPrefAttach(500, 50,Rnd)
snap.SaveEdgeList(G2, 'paperScaleFree500-499.txt')

G3 =snap.GenRndGnm(snap.PUNGraph, 449, 610)
snap.SaveEdgeList(G3, 'paperRandom449-610.txt')
