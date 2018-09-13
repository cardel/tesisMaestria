#!/bin/sh
python pruebasRobustezScaleFree.py --file ../datos/Generadas/ScaleFree2000Nodes.txt --type Edge  --output ScaleFree2000N  &
python pruebasRobustezScaleFree.py --file ../datos/Generadas/ScaleFree4000Nodes.txt --type Edge  --output ScaleFree4000  &
python pruebasRobustezScaleFree.py --file ../datos/Generadas/ScaleFree8000Nodes.txt --type Edge  --output ScaleFree8000  &

