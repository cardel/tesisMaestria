#!/bin/sh


python pruebasRobustez.py --type SmallWorld --output SmallWorldGC --message SmallWorldGC --node 500 --desired 10 --measure GC --attack random&
python pruebasRobustez.py --type ScaleFreePrefAttach --output ScaleFreePrefAttachMeasureGC --message ScaleFreePrefAttachMeasureGC --node 80 --desired 500  --measure GC --attack random&
python pruebasRobustez.py --type Random --output RandomGC --message RandomGC --node 100 --desired 500 --measure GC --attack random &
