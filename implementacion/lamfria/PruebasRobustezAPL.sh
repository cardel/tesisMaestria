#!/bin/sh 
 
 python pruebasRobustez.py  --file ../datos/karate.net --type Pajek --output Randomkarate --measure APL --attack random
 
 python pruebasRobustez.py  --file ../datos/football.net --type Pajek --output Randomfootball --measure APL --attack random

python pruebasFractalidad.py --file ../datos/cellular.dat --type Edge --output Randomcellular --measure APL --attack random


 python pruebasRobustez.py  --file ../datos/karate.net --type Pajek --output degreekarate --measure APL --attack degree
 
 python pruebasRobustez.py  --file ../datos/football.net --type Pajek --output degreefootball --measure APL --attack degree

python pruebasRobustez.py --file ../datos/cellular.dat --type Edge --output degreecellular --measure APL --attack degree

 python pruebasRobustez.py  --file ../datos/karate.net --type Pajek --output centralitykarate --measure APL --attack centrality
 
 python pruebasRobustez.py  --file ../datos/football.net --type Pajek --output centralityfootball --measure APL --attack centrality

python pruebasRobustez.py --file ../datos/cellular.dat --type Edge --output centralitycellular --measure APL --attack centrality


for Nodes in 300 500 800
do
	for Edges in 2000 4000
	do
		python pruebasRobustez.py --type SmallWorld --output "randomSmallWorld"$Nodes"d"$Edges --message "SmallWorld"$Nodes"d"$Edges --node $Nodes --desired $Edges --measure APL --attack random
		
		python pruebasRobustez.py --type SmallWorld --output "degreeSmallWorld"$Nodes"d"$Edges --message "SmallWorld"$Nodes"d"$Edges --node $Nodes --desired $Edges --measure APL --attack degree	
			
		python pruebasRobustez.py --type SmallWorld --output "centralitySmallWorld"$Nodes"d"$Edges --message "SmallWorld"$Nodes"d"$Edges --node $Nodes --desired $Edges--measure APL --attack centrality
	done
done

#ScaleFree
for Nodes in 300 500 800
do
	for Edges in 2000 4000
	do
		python pruebasRobustez.py --type ScaleFreePowerLaw --output "randomScaleFreePowerLaw"$Nodes"d"$Edges --message "ScaleFreePowerLaw"$Nodes"d"$Edges --node $Nodes --desired $Edges --measure APL --attack random	 

		python pruebasRobustez.py --type ScaleFreePowerLaw --output "degreeScaleFreePowerLaw"$Nodes"d"$Edges --message "ScaleFreePowerLaw"$Nodes"d"$Edges --node $Nodes --desired $Edges --measure APL --attack degree	
		
		python pruebasRobustez.py --type ScaleFreePowerLaw --output "centralityScaleFreePowerLaw"$Nodes"d"$Edges --message "ScaleFreePowerLaw"$Nodes"d"$Edges --node $Nodes --desired $Edges --measure APL --attack centrality	 
	done
done

#Random
for Nodes in 300 500 800
do
	for Edges in 2000 4000
	do
		python pruebasRobustez.py --type Random --output "RandomRandom"$Nodes"d"$Edges --message "Random"$Nodes"d"$Edges --node $Nodes --desired $Edges  --measure APL --attack random	 

		python pruebasRobustez.py --type Random --output "degreeRandom"$Nodes"d"$Edges --message "Random"$Nodes"d"$Edges --node $Nodes --desired $Edges  --measure APL --attack degree	
		
		python pruebasRobustez.py --type Random --output "centralityRandom"$Nodes"d"$Edges --message "Random"$Nodes"d"$Edges --node $Nodes --desired $Edges  --measure APL --attack centrality	
	done
done
