#!/bin/sh
cd ..
python pruebasFractalidad.py --type Random --output Random2000-20000 --message Random2000-20000 --node 2000 --desired 20000 

python pruebasFractalidad.py --file ../datos/cellular.dat --type Edge --output cellularDegree --message "cellular"  
