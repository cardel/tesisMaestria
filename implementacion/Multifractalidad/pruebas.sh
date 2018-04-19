#!/bin/sh
python main.py --file ../datos/football.net --type Pajek --output footballDegree --message "football" --attack degree &

python main.py --file ../datos/karate.net --type Pajek --output karateDegree --message "karate" --attack degree &


python main.py --file ../datos/cellular.dat --type Edge --output cellularDegree --message "cellular" --attack degree &

#(2,2)-flower 7th generation

python main.py --type Flower --output FlowerDegree --message "flower" --attack degree &

#Scalefree 3000 nodos, 100 grado de salida


