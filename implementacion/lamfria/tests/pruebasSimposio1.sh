#!/bin/sh


python pruebasFractalidad.py --type SmallWorld --output SmallWorld2 --message SmallWorld --node 500 --desired 10 &
python pruebasFractalidad.py --type ScaleFreePrefAttach --output ScaleFreePrefAttach --message ScaleFreePrefAttach50d100 --node 100 --desired 10  &
python pruebasFractalidad.py --type Random --output Random50d100 --message Random --node 100 --desired 10  &
