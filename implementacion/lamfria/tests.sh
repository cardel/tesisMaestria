#!/bin/sh
#!/bin/sh

#Maquina 1 
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/ScaleFree2000Nodes.txt --type Edge  --output ScaleFree2000Nodes  COMPLETA
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/ScaleFree4000Nodes.txt --type Edge  --output ScaleFree4000Nodes  COMPLETA  --- Haciendo faltantes (Maquina 1, lado 2)

#Maquina 2
python pruebasFractalidadFaltantes.py  --file ../datos/Generadas/ScaleFree8000Nodes.txt --type Edge  --output ScaleFree8000Nodes   OK  --- Haciendo faltantes (Maquina 1, lado 2)
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/SmallWorld5000NodesRewire005.txt --type Edge  --output SmallWorld5000NodesRewire005  OK  Haciendo faltantes (Faltantes1)

#Maquina 3
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/SmallWorld5000NodesRewire01.txt --type Edge  --output SmallWorld5000NodesRewire01   COMPLETA Haciendo faltantes (Faltantes1)
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/SmallWorld5000NodesRewire02.txt --type Edge  --output SmallWorld5000NodesRewire02   OK Haciendo faltantes (Faltantes2)

#Maquina 4
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/Random1991Nodes5939.txt --type Edge --output Random1991Nodes5939   COMPLETA
python pruebasFractalidadFaltantes.py --file ../datos/Generadas/Random3373Nodes5978.txt --type Edge  --output Random3373Nodes5978 OK  Haciendo faltantes (Faltantes2)

#Maquina 5
python pruebasFractalidad.py --file ../datos/Generadas/Random5620Nodes8804.txt --type Edge  --output Random5620Nodes8804 OK
python pruebasFractalidad.py --file ../datos/RedesReales/Celengs.net  --type Pajek --output Celengs  COMPLETA

#Maquina 6
python pruebasFractalidadFaltantes.py --file ../datos/RedesReales/cerevisiae.net  --type Pajek --output cerevisiae  Haciendo faltantes en maquina 8
python pruebasFractalidadFaltantesECOLI.py --file ../datos/RedesReales/EColi.net  --type Pajek --output EColi  COMPLETA 

#Maquina 7
python pruebasFractalidadFaltantes.py --file ../datos/Fractales/floweru2v2.net  --type Pajek --output floweru2v2  OK  Faltantes terminadas
python pruebasFractalidadFaltantes.py --file ../datos/Fractales/floweru1v3.net  --type Pajek --output floweru1v3  OK   Faltantes terminadas


#Maquina 8
python pruebasRobustezCentralidad.py --file ../datos/Generadas/ScaleFree2000Nodes.txt --type Edge  --output ScaleFree2000NodesCentralidad   TOTAL COMPLETA
python pruebasRobustezCentralidad.py --file ../datos/Generadas/ScaleFree4000Nodes.txt --type Edge  --output ScaleFree4000NodesCentralidad   TOTAL COMPLETA

#Maquina 9
python pruebasRobustezCentralidad.py --file ../datos/Generadas/ScaleFree8000Nodes.txt --type Edge  --output ScaleFree8000NodesCentralidad      (Repitiendo centralidad en serverMaestrai3 lado 2)
python pruebasRobustezCentralidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire005.txt --type Edge  --output SmallWorld5000NodesRewire005Centralidad   Repitiendo centralidad en serverMaestrai3 lado 2)
 
#Maquina 10
python pruebasRobustezCentralidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire01.txt --type Edge  --output SmallWorld5000NodesRewire01Centralidad (Repitiendo centralidad en robustez1-1)
python pruebasRobustezCentralidad.py --file ../datos/Generadas/SmallWorld5000NodesRewire02.txt --type Edge  --output SmallWorld5000NodesRewire02Centralidad (Repitiendo centralidad en robustez1-1)

#Maquina 11
python pruebasRobustezCentralidad.py --file ../datos/Generadas/Random1991Nodes5939.txt --type Edge --output Random1991Nodes5939Centralidad     COMPLETA  (Repitiendo centralidad en serverMaestria11)
python pruebasRobustezCentralidad.py --file ../datos/Generadas/Random3373Nodes5978.txt --type Edge  --output Random3373Nodes5978Centralidad  COMPLETA (Repitiendo centralidad en serverMaestria11)
#Maquina 12
python pruebasRobustezCentralidad.py --file ../datos/Generadas/Random5620Nodes8804.txt --type Edge  --output Random5620Nodes8804Centralidad   (Repitiendo centralidad en serverMaestria14)
python pruebasRobustezCentralidad.py --file ../datos/RedesReales/Celengs.net  --type Pajek --output CelengsCentralidad (Repitiendo centralidad en serverMaestria14)

#Maquina 13
python pruebasRobustezCentralidad.py --file ../datos/RedesReales/cerevisiae.net  --type Pajek --output cerevisiaeCentralidad     (Repitiendo centralidad en serverMaestria3)
python pruebasRobustezCentralidad.py --file ../datos/RedesReales/EColi.net  --type Pajek --output EColiCentralidad     (Repitiendo centralidad en serverMaestria3)
#Maquina 14
python pruebasRobustezCentralidad.py --file ../datos/Fractales/floweru2v2.net  --type Pajek --output floweru2v2Centralidad  TOTAL COMPLETA
python pruebasRobustezCentralidad.py --file ../datos/Fractales/floweru1v3.net  --type Pajek --output floweru1v3Centralidad   TOTAL COMPLETA
#Maquina 14

