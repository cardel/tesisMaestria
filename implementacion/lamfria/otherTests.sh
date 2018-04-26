#!/bin/sh

python pruebasFractalidad.py --file ../datos/Generadas/randomNetwokr-20.txt --type Edge --output Random 
python pruebasFractalidad.py --file ../datos/Generadas/scaleFree500-20.txt --type Edge --output ScaleFree 

python pruebasFractalidad.py --file ../datos/Generadas/smallWorld500-20.txt --type Edge --output SmallWorld 

