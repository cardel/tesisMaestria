#!/bin/sh

#SmallWorld 3000 nodos, 100 grado de salida
for Nodes in 50 60 100
do
	for Edges in 150 200
	do
		python main.py --type SmallWorld --output "SmallWorld"$Nodes"d"$Edges --message "SmallWorld"$Nodes"d"$Edges --node $Nodes --desired $Edges &
	done
done


for Nodes in 50 60 100
do
	for Edges in 150 200
	do
		python main.py --type ScaleFreePowerLaw --output "ScaelFreePowerLaw"$Nodes"d"$Edges --message "ScaelFreePowerLaw"$Nodes"d"$Edges --node $Nodes --desired $Edges  &
	done
done
