#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties
import sys

archivo = sys.argv[1]
#FBCS algorithm
fileInput = open(archivo,"r")
fileInput.readline() 
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRA = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqA = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqA = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="FSBCAlgorithm\n":
		break
	cadena+=aux
lnMrqA = cadena

#BCC algorithm

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRB = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqB = cadena

cadena = ""

while True:
	aux = fileInput.readline()

	if aux=="lnMrq\n" :
		break
	cadena+=aux

DqB = cadena


cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="SBAlgorithm\n":
		break
	cadena+=aux
lnMrqB = cadena
#SandBox Algorithm


fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRC = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqC = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqC = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="SandBox Genetic\n":
		break
	cadena+=aux
lnMrqC = cadena


#SandBox Genetic

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRD = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqD = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqD = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessAverage\n":
		break
	cadena+=aux
lnMrqD = cadena


cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessMax\n":
		break
	cadena+=aux
fitNessAverageD = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="fitNessMin\n":
		break
	cadena+=aux
fitNessMaxD = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="SandBox Simulated Annealing\n":
		break
	cadena+=aux
fitNessMinD = cadena


#SandBox simulated
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRE = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqE = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqE = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="BoxCounting Genetic\n":
		break
	cadena+=aux
lnMrqE= cadena

#BoxCounting Genetic

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRF = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqF = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqF = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessAverage\n":
		break
	cadena+=aux
lnMrqF = cadena


cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessMax\n":
		break
	cadena+=aux
fitNessAverageF = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="fitNessMin\n":
		break
	cadena+=aux
fitNessMaxF = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="BoxCounting Simulated Annealing\n":
		break
	cadena+=aux
fitNessMinF = cadena

#BoxCounting Simulated Annealing
fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRG = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqG = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqG = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="Fixed Size Genetic\n":
		break
	cadena+=aux
lnMrqG= cadena

#Fixed size Genetic

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRH = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqH = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqH = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessAverage\n":
		break
	cadena+=aux
lnMrqH = cadena


cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="fitNessMax\n":
		break
	cadena+=aux
fitNessAverageH = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="fitNessMin\n":
		break
	cadena+=aux
fitNessMaxH = cadena
cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Genetic fixed size Simulated Annealing\n":
		break
	cadena+=aux
fitNessMinH = cadena

#Genetic fixed size Simulated Annealing

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="IndexZero\n":
		break
	cadena+=aux
logRI = cadena


indexZero=fileInput.readline()

fileInput.readline() 

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="Dq\n":
		break
	cadena+=aux
	
TqI = cadena

cadena = ""
while True:
	aux = fileInput.readline()
	if aux=="lnMrq\n":
		break
	cadena+=aux

DqI = cadena

cadena = ""

while True:
	aux = fileInput.readline()
	if aux=="end\n" or aux=="Execution time\n":
		break
	cadena+=aux
lnMrqI= cadena

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
fileOutput.write("symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']\n")

fileOutput.write("IndexZero="+indexZero+"\n")

fileOutput.write("logRA=numpy.array("+logRA+")\n")
fileOutput.write("TqA=numpy.array("+TqA+")\n")
fileOutput.write("DqA=numpy.array("+DqA+")\n")
fileOutput.write("lnMrqA=numpy.array("+lnMrqA+")\n")

fileOutput.write("logRB=numpy.array("+logRB+")\n")
fileOutput.write("TqB=numpy.array("+TqB+")\n")
fileOutput.write("DqB=numpy.array("+DqB+")\n")
fileOutput.write("lnMrqB=numpy.array("+lnMrqB+")\n")

fileOutput.write("logRC=numpy.array("+logRC+")\n")
fileOutput.write("TqC=numpy.array("+TqC+")\n")
fileOutput.write("DqC=numpy.array("+DqC+")\n")
fileOutput.write("lnMrqC=numpy.array("+lnMrqC+")\n")


fileOutput.write("logRD=numpy.array("+logRD+")\n")
fileOutput.write("TqD=numpy.array("+TqD+")\n")
fileOutput.write("DqD=numpy.array("+DqD+")\n")
fileOutput.write("lnMrqE=numpy.array("+lnMrqD+")\n")
fileOutput.write("fitNessAverageD=numpy.array("+fitNessAverageD+")\n")
fileOutput.write("fitNessMaxD=numpy.array("+fitNessMaxD+")\n")
fileOutput.write("fitNessMinD=numpy.array("+fitNessMinD+")\n")


fileOutput.write("logRE=numpy.array("+logRE+")\n")
fileOutput.write("TqE=numpy.array("+TqE+")\n")
fileOutput.write("DqE=numpy.array("+DqE+")\n")
fileOutput.write("lnMrqE=numpy.array("+lnMrqE+")\n")

fileOutput.write("logRF=numpy.array("+logRF+")\n")
fileOutput.write("TqF=numpy.array("+TqF+")\n")
fileOutput.write("DqF=numpy.array("+DqF+")\n")
fileOutput.write("lnMrqF=numpy.array("+lnMrqF+")\n")
fileOutput.write("fitNessAverageF=numpy.array("+fitNessAverageF+")\n")
fileOutput.write("fitNessMaxF=numpy.array("+fitNessMaxF+")\n")
fileOutput.write("fitNessMinF=numpy.array("+fitNessMinF+")\n")


fileOutput.write("logRG=numpy.array("+logRG+")\n")
fileOutput.write("TqG=numpy.array("+TqG+")\n")
fileOutput.write("DqG=numpy.array("+DqG+")\n")
fileOutput.write("lnMrqG=numpy.array("+lnMrqG+")\n")

fileOutput.write("logRH=numpy.array("+logRH+")\n")
fileOutput.write("TqH=numpy.array("+TqH+")\n")
fileOutput.write("DqH=numpy.array("+DqH+")\n")
fileOutput.write("lnMrqH=numpy.array("+lnMrqH+")\n")
fileOutput.write("fitNessAverageH=numpy.array("+fitNessAverageH+")\n")
fileOutput.write("fitNessMaxH=numpy.array("+fitNessMaxH+")\n")
fileOutput.write("fitNessMinH=numpy.array("+fitNessMinH+")\n")

fileOutput.write("logRI=numpy.array("+logRI+")\n")
fileOutput.write("TqI=numpy.array("+TqI+")\n")
fileOutput.write("DqI=numpy.array("+DqI+")\n")
fileOutput.write("lnMrqI=numpy.array("+lnMrqI+")\n")

fileOutput.write("fileOutput = '"+archivo+"'\n")
#fileOutput.write("timestr = time.strftime('%Y%m%d_%H%M%S')\n")
fileOutput.write("timestr = 'grafica'\n")

fileOutput.write("fig2 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('T(q)')\n")	
fileOutput.write("plt.title(u'Función de evaluación por iteración Genético')\n")
fileOutput.write("plt.plot(range(0,fitNessMaxD.shape[0]), fitNessMaxD,'b<-' ,label='Mejor individuo')\n")
fileOutput.write("plt.plot(range(0,fitNessAverageD.shape[0]), fitNessAverageD,'g<-' ,label='Primedio')\n")
fileOutput.write("plt.plot(range(0,fitNessMinD.shape[0]), fitNessMinD,'r<-' ,label='Peor individuo')\n")
fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Fitness'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")

fileOutput.write("fig3 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('D(q)')\n")	
fileOutput.write("plt.title(u'Dimensión fractal generalizada')\n")
fileOutput.write("plt.plot(range(0,maxq), DqA[IndexZero:-1],'g<-' ,label='BCC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqB[IndexZero:-1],'b<-' ,label='FSBC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqC[IndexZero:-1],'r<-' ,label='SB')\n")
fileOutput.write("plt.plot(range(0,maxq), DqD[IndexZero:-1],'m<-' ,label='Evolutivo SB')\n")
fileOutput.write("plt.plot(range(0,maxq), DqE[IndexZero:-1],'y<-' ,label='Recocido SB')\n")
fileOutput.write("plt.plot(range(0,maxq), DqF[IndexZero:-1],'k<-' ,label='Evolutivo BCC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqG[IndexZero:-1],'c<-' ,label='Recocido BCC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqH[IndexZero:-1],'r*-' ,label='Evolutivo FSBC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqI[IndexZero:-1],'b*-' ,label='Recocido FSBC')\n")
fileOutput.write("plt.xticks(range(0,maxq))\n")

fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Dq'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")

fileOutput.close()
