#!/bin/sh

#SmallWorld 3000 nodos, 100 grado de salida
for Nodes in 50 100
do
	for Edges in 150 250
	do
		python main.py --type SmallWorld --output "SmallWorldDegree"$Nodes"d"$Edges --message "SmallWorldn"$Nodes"d"$Edges --node $Nodes --desired $Edges&
	done
done
