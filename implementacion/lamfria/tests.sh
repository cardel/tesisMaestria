#!/bin/sh
#!/bin/sh

#Maquina 1 
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/ScaleFree2000Nodes.txt --type Edge  --output ScaleFree2000Nodes  Haciendo faltantes
python pruebasFractalidad.py --file ../datos/Generadas/ScaleFree4000Nodes.txt --type Edge  --output ScaleFree4000Nodes 

#Maquina 2
python pruebasFractalidad.py --file ../datos/Generadas/ScaleFree8000Nodes.txt --type Edge  --output ScaleFree8000Nodes 
python pruebasFractalidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire005.txt --type Edge  --output SmallWorld5000NodesRewire005

#Maquina 3
python pruebasFractalidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire01.txt --type Edge  --output SmallWorld5000NodesRewire01
python pruebasFractalidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire02.txt --type Edge  --output SmallWorld5000NodesRewire02  

#Maquina 4
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/Random1991Nodes5939.txt --type Edge --output Random1991Nodes5939  Haciendo faltantes en maquina 8
python pruebasFractalidad.py --file ../datos/Generadas/Random3373Nodes5978.txt --type Edge  --output Random3373Nodes5978

#Maquina 5
python pruebasFractalidad.py --file ../datos/Generadas/Random5620Nodes8804.txt --type Edge  --output Random5620Nodes8804
python pruebasFractalidad.py --file ../datos/RedesReales/Celengs.net  --type Pajek --output Celengs  Haciendo faltantes

#Maquina 6
python pruebasFractalidad.py --file ../datos/RedesReales/cerevisiae.net  --type Pajek --output cerevisiae
python pruebasFractalidad.py --file ../datos/RedesReales/EColi.net  --type Pajek --output EColi

#Maquina 7
python pruebasFractalidad.py --file ../datos/Fractales/floweru2v2.net  --type Pajek --output floweru2v2
python pruebasFractalidad.py --file ../datos/Fractales/floweru1v3.net  --type Pajek --output floweru1v3

#Maquina 8
python pruebasRobustez.py --file ../datos/Generadas/ScaleFree2000Nodes.txt --type Edge  --output ScaleFree2000Nodes  
python pruebasRobustez.py --file ../datos/Generadas/ScaleFree4000Nodes.txt --type Edge  --output ScaleFree4000Nodes  

#Maquina 9
python pruebasRobustez.py --file ../datos/Generadas/ScaleFree8000Nodes.txt --type Edge  --output ScaleFree8000Nodes  
python pruebasRobustez.py --file ../datos/Generadas/SmallWorld5000NodesRewire005.txt --type Edge  --output SmallWorld5000NodesRewire005 

#Maquina 10
python pruebasRobustez.py --file ../datos/Generadas/SmallWorld5000NodesRewire01.txt --type Edge  --output SmallWorld5000NodesRewire01 
python pruebasRobustez.py --file ../datos/Generadas/SmallWorld5000NodesRewire02.txt --type Edge  --output SmallWorld5000NodesRewire02 

#Maquina 11
python pruebasRobustez.py --file ../datos/Generadas/Random1991Nodes5939.txt --type Edge --output Random1991Nodes5939   
python pruebasRobustez.py --file ../datos/Generadas/Random3373Nodes5978.txt --type Edge  --output Random3373Nodes5978  
#Maquina 12
python pruebasRobustez.py --file ../datos/Generadas/Random5620Nodes8804.txt --type Edge  --output Random5620Nodes8804 
python pruebasRobustez.py --file ../datos/RedesReales/Celengs.net  --type Pajek --output Celengs 

#Maquina 13
python pruebasRobustez.py --file ../datos/RedesReales/cerevisiae.net  --type Pajek --output cerevisiae  
python pruebasRobustez.py --file ../datos/RedesReales/EColi.net  --type Pajek --output EColi  
#Maquina 14
python pruebasRobustez.py --file ../datos/Fractales/floweru2v2.net  --type Pajek --output floweru2v2 
python pruebasRobustez.py --file ../datos/Fractales/floweru1v3.net  --type Pajek --output floweru1v3 

