#!/bin/bash
for filename in *.txt; do
 	echo $filename
    python createFile.py $filename
	python generarGraficas.py
done
