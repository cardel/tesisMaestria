#!/bin/bash
for filename in 20*; do
 	echo $filename
    python createFile.py $filename
	python generarGraficas.py
done

