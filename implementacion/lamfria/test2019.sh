#!/bin/sh
python pruebasRobustez2019.py --file ../datos/redesTesisJoshua/test.adjlist0  --type Edge --output RedJoshua1

python pruebasRobustez2019.py --file ../datos/yeast/YeastS.net  --type Pajek --output YeastS.net
python pruebasRobustez2019.py  --file ../datos/karate.net --type Pajek --output karate

