#!/bin/sh
python pruebasFractalidad.py --file ../datos/football.net --type Pajek --output footballDegree --message "football"  &

python pruebasFractalidad.py --file ../datos/karate.net --type Pajek --output karateDegree --message "karate"  &

python pruebasFractalidad.py --file ../datos/cellular.dat --type Edge --output cellularDegree --message "cellular"  &

#(2,2)-flower 7th generation

python pruebasFractalidad.py --type Flower --output FlowerDegree --message "flower" &

#Scalefree 3000 nodos, 100 grado de salida


#SmallWorld 3000 nodos, 100 grado de salida
for Nodes in 300 500 1000
do
	for Edges in 1200 2000
	do
		python pruebasFractalidad.py --type SmallWorld --output "SmallWorld"$Nodes"d"$Edges --message "SmallWorld"$Nodes"d"$Edges --node $Nodes --desired $Edges &
	done
done

#ScaleFree
for Nodes in 300 500 1000
do
	for Edges in 1200 2000
	do
		python pruebasFractalidad.py --type ScaleFreePowerLaw --output "ScaelFreePowerLaw"$Nodes"d"$Edges --message "ScaleFreePowerLaw"$Nodes"d"$Edges --node $Nodes --desired $Edges  &
	done
done

#Random
for Nodes in 300 500 1000
do
	for Edges in 1200 2000
	do
		python pruebasFractalidad.py --type Random --output "Random"$Nodes"d"$Edges --message "Random"$Nodes"d"$Edges --node $Nodes --desired $Edges  &
	done
done
