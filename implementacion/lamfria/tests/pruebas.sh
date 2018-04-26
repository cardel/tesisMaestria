#!/bin/sh

python pruebasFractalidadSencillas.py --file ../datos/Generadas/randomNetwokr-20.txt --type Edge --output Random --message "Random"  
python pruebasFractalidadSencillas.py --file ../datos/Generadas/scaleFree500-20.txt --type Edge --output ScaleFree --message "ScaleFree"  

python pruebasFractalidadSencillas.py --file ../datos/Generadas/smallWorld500-20.txt --type Edge --output SmallWorld --message "SmallWorld"  


python pruebasFractalidadSencillas.py --file ../datos/Generadas/smallWorld5500-2515.txt --type Edge --output smallWorld5500-2515.txt --message "smallWorld5500"   
python pruebasFractalidadSencillas.py --file ../datos/Generadas/paperScaleFree500-499.txt --type Edge --output paperScaleFree500-499.txt --message "paperScaleFree500-499.txt"  

python pruebasFractalidadSencillas.py --file ../datos/Generadas/paperRandom449-610.txt --type Edge --output paperRandom449-610.txt --message "paperRandom449-610.txt"  



#Othwers

python pruebasFractalidadSencillas.py --file ../datos/football.net --type Pajek --output footballDegree --message "football"  &
python pruebasFractalidadSencillas.py --file ../datos/lesmis.net --type Pajek --output lesmis --message "lesmis"  &


python pruebasFractalidad.py --file ../datos/karate.net --type Pajek --output karateDegree --message "karate"  &

python pruebasFractalidad.py --file ../datos/cellular.dat --type Edge --output cellularDegree --message "cellular"  &

#(2,2)-flower 7th generation

python pruebasFractalidad.py --file ../datos/flower.txt --type Edge --output flower --message "flower"  &

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
