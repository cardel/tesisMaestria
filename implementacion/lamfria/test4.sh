#!/bin/sh
python pruebasFractalidad.py --file ../datos/RedesReales/Celengs.net  --type Pajek --output Celengs
python pruebasFractalidad.py --file ../datos/RedesReales/cerevisiae.net  --type Pajek --output cerevisiae
python pruebasFractalidad.py --file ../datos/RedesReales/EColi.net  --type Pajek --output EColi




