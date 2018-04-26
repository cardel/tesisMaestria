#!/bin/sh
python pruebasRobustez.py --type SmallWorld --output SmallWorldAPL --message SmallWorldAPL --node 100 --desired 50 --measure APL --attack random&
python pruebasRobustez.py --type ScaleFreePrefAttach --output ScaleFreePrefAttachMeasureAPL --message ScaleFreePrefAttachMeasureAPL --node 100 --desired 500  --measure APL --attack random&
python pruebasRobustez.py --type Random --output RandomAPL --message RandomAPL --node 100 --desired 500 --measure APL --attack random &
