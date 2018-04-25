#!/bin/sh
cd ..
python pruebasFractalidad.py --type SmallWorld --output SmallWorld2000-20000 --message SmallWorld2000-20000 -node 2000 --desired 20000 

python pruebasFractalidad.py --file ../datos/dolphins.net --type Pajek --output dolphins --message "dolphins"
