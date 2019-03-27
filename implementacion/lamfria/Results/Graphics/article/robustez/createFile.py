#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties
import sys

archivo = sys.argv[1]
#Random
fileInput = open(archivo,"r")
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="RandomAttack\n":
		break
	cadena+=aux
percentNodes = cadena

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureGC\n":
		break
	cadena+=aux
TqRandom = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureAPL\n":
		break
	cadena+=aux
	
GCRandom = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Degree\n":
		break
	cadena+=aux

APLRandom = cadena

#Degree
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureGC\n":
		break
	cadena+=aux
TqDegree = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureAPL\n":
		break
	cadena+=aux
	
GCDegree = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Centrality\n":
		break
	cadena+=aux

APLDegree= cadena

#Centrality

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureGC\n":
		break
	cadena+=aux
TqCentrality = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureAPL\n":
		break
	cadena+=aux
	
GCCentrality = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Genetic\n":
		break
	cadena+=aux

APLCentrality = cadena
#Genetic

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureGC\n":
		break
	cadena+=aux
TqGenetic= cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureAPL\n":
		break
	cadena+=aux
	
GCGenetic = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Simulated\n":
		break
	cadena+=aux

APLGenetic = cadena
#Simulated
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureGC\n":
		break
	cadena+=aux
TqSimulated = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="measureAPL\n":
		break
	cadena+=aux
	
GCSimulated = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=='':
		break
	cadena+=aux

APLSimulated = cadena

fileInput.close()

fileOutput= open("generarGraficas.py","w")
fileOutput.write("#!/usr/bin/python\n")
fileOutput.write("# -*- coding: utf-8 -*- \n")
fileOutput.write("import numpy\n")
fileOutput.write("numpy.set_printoptions(threshold=numpy.nan)\n")
fileOutput.write("import matplotlib.pyplot as plt\n")



fileOutput.write("import time\n")
fileOutput.write("import math\n")
fileOutput.write("from matplotlib.font_manager import FontProperties\n")
fileOutput.write("minq = -10\n")
fileOutput.write("maxq = 10\n")
fileOutput.write("IndexZero = 10\n")
fileOutput.write("symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']\n")
fileOutput.write("nan=float('nan')\n")
percentNodes = numpy.array2string(numpy.array(range(0,91,10)),separator=',')

fileOutput.write("percentNodes="+percentNodes+"\n")



fileOutput.write("DqRandom=numpy.array("+TqRandom+")\n")
fileOutput.write("GCRandom=numpy.array("+GCRandom+")\n")
fileOutput.write("APLRandom=numpy.array("+APLRandom+")\n")

fileOutput.write("DqDegree=numpy.array("+TqDegree+")\n")
fileOutput.write("GCDegree=numpy.array("+GCDegree+")\n")
fileOutput.write("APLDegree=numpy.array("+APLDegree+")\n")

fileOutput.write("DqCentrality=numpy.array("+TqCentrality+")\n")
fileOutput.write("GCCentrality=numpy.array("+GCCentrality+")\n")
fileOutput.write("APLCentrality=numpy.array("+APLCentrality+")\n")

fileOutput.write("DqGenetic=numpy.array("+TqGenetic+")\n")
fileOutput.write("GCGenetic=numpy.array("+GCGenetic+")\n")
fileOutput.write("APLGenetic=numpy.array("+APLGenetic+")\n")

fileOutput.write("DqSimulated=numpy.array("+TqSimulated+")\n")
fileOutput.write("GCSimulated=numpy.array("+GCSimulated+")\n")
fileOutput.write("APLSimulated=numpy.array("+APLSimulated+")\n")

fileOutput.write("fileOutput = '"+archivo+"'\n")
#fileOutput.write("timestr = time.strftime('%Y%m%d_%H%M%S')\n")
fileOutput.write("timestr = 'grafica'\n")

fileOutput.write("font = {'weight': 'normal', 'size': 8}\n")


fileOutput.write("fig1 = plt.figure()\n")
fileOutput.write("plt.xlabel('Porcentaje de nodos eliminados (%)', fontdict=font)\n")
fileOutput.write("plt.ylabel(u'Tamaño',fontdict=font)\n")	
fileOutput.write("plt.title(u'Tamaño componente gigante', fontdict=font)\n")
fileOutput.write("plt.plot(percentNodes[0:GCRandom.shape[0]], GCRandom,'b<-' ,label='Aleatorio R='+\"{0:.2f}\".format(numpy.sum(GCRandom)))\n")
fileOutput.write("plt.plot(percentNodes[0:GCDegree.shape[0]], GCDegree,'g<-' ,label='Grado R='+\"{0:.2f}\".format(numpy.sum(GCDegree)))\n")
fileOutput.write("plt.plot(percentNodes[0:GCCentrality.shape[0]], GCCentrality,'r<-' ,label='Centralidad R='\"{0:.2f}\".format(numpy.sum(GCCentrality)))\n")
#fileOutput.write("plt.plot(percentNodes[0:GCGenetic.shape[0]], GCGenetic,'m<-' ,label='Genetico R='+str(numpy.sum(GCGenetic)))\n")
#fileOutput.write("plt.plot(percentNodes[0:GCSimulated.shape[0]], GCSimulated,'k<-' ,label='Recocido R='+str(numpy.sum(GCSimulated)))\n")
fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig('GC'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")


fileOutput.write("fig2 = plt.figure()\n")
fileOutput.write("plt.xlabel('Porcentaje de nodos eliminados (%)', fontdict=font)\n")
fileOutput.write("plt.ylabel(u'Diámetro camino', fontdict=font)\n")
fileOutput.write("plt.title(u'Distancia promedio', fontdict=font)\n")
fileOutput.write("plt.plot(percentNodes[0:APLRandom.shape[0]], APLRandom,'b<-' ,label='Aleatorio R='+\"{0:.2f}\".format(numpy.sum(APLRandom)))\n")
fileOutput.write("plt.plot(percentNodes[0:APLDegree.shape[0]], APLDegree,'g<-' ,label='Grado R='+\"{0:.2f}\".format(numpy.sum(APLDegree)))\n")
fileOutput.write("plt.plot(percentNodes[0:APLCentrality.shape[0]], APLCentrality,'r<-' ,label='Centralidad R='+\"{0:.2f}\".format(numpy.sum(APLCentrality)))\n")
#fileOutput.write("plt.plot(percentNodes[0:APLGenetic.shape[0]], APLGenetic,'m<-' ,label='Genetico R='+str(numpy.sum(APLGenetic)))\n")
#fileOutput.write("plt.plot(percentNodes[0:APLSimulated.shape[0]], APLSimulated,'k<-' ,label='Recocido R='+str(numpy.sum(APLSimulated)))\n")
fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig('APL'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")


#fileOutput.write("fig3 = plt.figure()\n")
#fileOutput.write("for i in range(0,9):\n")
#fileOutput.write("	if i < DqRandom.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqRandom[i]))) == 1:\n")
#fileOutput.write("		plt.plot(range(0,maxq),DqRandom[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')\n")	
#fileOutput.write("fontP = FontProperties()\n")
#fileOutput.write("fontP.set_size('small')\n")
#fileOutput.write("plt.legend(prop=fontP)\n")
#fileOutput.write("plt.xlabel('Escalado q', fontdict=font)\n")
#fileOutput.write("plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)\n")
#fileOutput.write("plt.title(u'Multifractalidad ataque aleatorio', fontdict=font)\n")
#fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))\n")
#fileOutput.write("plt.grid(True)\n")
#fileOutput.write("plt.savefig('DqRandom'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")
	
#fileOutput.write("fig4 = plt.figure()\n")
#fileOutput.write("for i in range(0,9):\n")
#fileOutput.write("	if i < DqDegree.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqDegree[i]))) == 1:\n")
#fileOutput.write("		plt.plot(range(0,maxq),DqDegree[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')\n")	
#fileOutput.write("fontP = FontProperties()\n")
#fileOutput.write("fontP.set_size('small')\n")
#fileOutput.write("plt.legend(prop=fontP)\n")
#fileOutput.write("plt.xlabel('Escalado q', fontdict=font)\n")
#fileOutput.write("plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)\n")
#fileOutput.write("plt.title(u'Multifractalidad ataque por grado', fontdict=font)\n")
#fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
#fileOutput.write("plt.grid(True)\n")
#fileOutput.write("plt.savefig('DqDegree'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")


#fileOutput.write("fig5 = plt.figure()\n")
#fileOutput.write("for i in range(0,9):\n")
#fileOutput.write("	if i < DqCentrality.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqCentrality[i]))) == 1:\n")
#fileOutput.write("		plt.plot(range(0,maxq),DqCentrality[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')\n")	
#fileOutput.write("fontP = FontProperties()\n")
#fileOutput.write("fontP.set_size('small')\n")
#fileOutput.write("plt.legend(prop=fontP)\n")
#fileOutput.write("plt.xlabel('Escalado (q)', fontdict=font)\n")
#fileOutput.write("plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)\n")
#fileOutput.write("plt.title(u'Multifractalidad ataque por centralidad', fontdict=font)\n")
#fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))\n")
#fileOutput.write("plt.grid(True)\n")
#fileOutput.write("plt.savefig(timestr+'_'+'DqCentrality'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")


#fileOutput.write("fig6 = plt.figure()\n")
#fileOutput.write("for i in range(0,9):\n")
#fileOutput.write("	if i < DqGenetic.shape[0]:\n")
#fileOutput.write("		plt.plot(range(0,maxq),DqGenetic[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')\n")	
#fileOutput.write("fontP = FontProperties()\n")
#fileOutput.write("fontP.set_size('small')\n")
#fileOutput.write("plt.legend(prop=fontP)\n")
#fileOutput.write("plt.xlabel('q')\n")
#fileOutput.write("plt.ylabel('D(q)')\n")
#fileOutput.write("plt.title(u'Dimensión fractal ataque aleatorio Genetico')\n")
#fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
#fileOutput.write("plt.grid(True)\n")
#fileOutput.write("plt.savefig(timestr+'_'+'DqGenetic'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")

#fileOutput.write("fig6 = plt.figure()\n")
#fileOutput.write("for i in range(0,9):\n")
#fileOutput.write("	if i < DqSimulated.shape[0]:\n")
#fileOutput.write("		plt.plot(range(0,maxq),DqSimulated[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')\n")	
#fileOutput.write("fontP = FontProperties()\n")
#fileOutput.write("fontP.set_size('small')\n")
#fileOutput.write("plt.legend(prop=fontP)\n")
#fileOutput.write("plt.xlabel('q')\n")
#fileOutput.write("plt.ylabel('D(q)')\n")
#fileOutput.write("plt.title(u'Dimensión fractal ataque aleatorio Recocido')\n")
#fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
#fileOutput.write("plt.grid(True)\n")
#fileOutput.write("plt.savefig(timestr+'_'+'DqSimulated'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")


fileOutput.close()
