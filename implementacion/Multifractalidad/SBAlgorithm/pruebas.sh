#!/bin/sh
python main.py --file ../../datos/football.net --type Pajek --output footballDegree --message "degree attack" --attack degree &
python main.py --file ../../datos/football.net --type Pajek --output footballRandom --message "random attack" --attack random &
python main.py --file ../../datos/football.net --type Pajek --output footballCnt --message "centrality attack" --attack centrality &

python main.py --file ../../datos/karate.net --type Pajek --output karateDegree --message "degree attack" --attack degree &
python main.py --file ../../datos/karate.net --type Pajek --output karateRandom --message "random attack" --attack random &
python main.py --file ../../datos/karate.net --type Pajek --output karateCnt --message "centrality attack" --attack centrality &


python main.py --file ../../datos/cellular.dat --type Edge --output cellularDegree --message "degree attack" --attack degree &
python main.py --file ../../datos/cellular.dat --type Edge --output cellularRandom --message "random attack" --attack random &
python main.py --file ../../datos/cellular.dat --type Edge --output cellularCnt --message "centrality attack" --attack centrality &

#(2,2)-flower 7th generation

python main.py --type Flower --output FlowerDegree --message "degree attack" --attack degree &
python main.py --type Flower --output FlowerRandom --message "random attack" --attack random &
python main.py --type Flower --output FlowerCnt --message "centrality attack" --attack centrality &

#Scalefree 3000 nodos, 100 grado de salida

python main.py --type ScaleFreePrefAttach --output ScaleFreePrefAttachDegree --message "degree attack" --attack degree &
python main.py --type ScaleFreePrefAttach --output ScaleFreePrefAttachRandom --message "random attack" --attack random &
python main.py --type ScaleFreePrefAttach --output ScaleFreePrefAttachCnt --message "centrality attack" --attack centrality &

#SmallWorld 3000 nodos, 100 grado de salida
python main.py --type SmallWorld --output SmallWorldDegree --message "degree attack" --attack degree &
python main.py --type SmallWorld --output SmallWorldRandom --message "random attack" --attack random &
python main.py --type SmallWorld --output SmallWorldCnt --message "centrality attack" --attack centrality &
