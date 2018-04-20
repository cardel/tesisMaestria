#!/bin/sh

#SmallWorld 3000 nodos, 100 grado de salida
for Nodes in 50 60 100
do
	for Edges in 150 200
	do
		python main.py --type ScaleFreePrefAttach --output "ScaleFree"$Nodes"d"$Edges --message "ScaleFree"$Nodes"d"$Edges --node $Nodes --desired $Edges > "Ssalida"$Nodes"-"$Edges &
	done
done
