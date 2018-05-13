#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties





fileInput = open("data","r")
fileInput.readline() 
fileInput.readline() 

logR = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 
indexZero=fileInput.readline()

fileInput.readline() 

Tq = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

Dq = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

cadena = ""
for i in range(0,127):
	cadena+=fileInput.readline()
	
lnMrq = cadena

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

fileOutput.write("logR=numpy.array("+logR+")\n")
fileOutput.write("Tq=numpy.array("+Tq+")\n")
fileOutput.write("Dq=numpy.array("+Dq+")\n")
fileOutput.write("lnMrq=numpy.array("+lnMrq+")\n")


fileOutput.write("fileOutput = 'scaleFree4000Nodes'\n")
fileOutput.write("timestr = time.strftime('%Y%m%d_%H%M%S')\n")


fileOutput.write("fig1 = plt.figure()\n")
fileOutput.write("i = 0\n")
fileOutput.write("for q in range(minq,maxq+1):\n")
fileOutput.write("	if q%2==0:\n")
fileOutput.write("		plt.plot(logR,lnMrq[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))\n")
fileOutput.write("	i+=1\n")
fileOutput.write("plt.ylabel('ln(<Z(r)>)^q')\n")
fileOutput.write("plt.title(u'Regresión lineal para red libre de escala 4000 nodos')\n")
fileOutput.write("plt.xlabel('ln(r/d)')\n")

fileOutput.write("fontP = FontProperties()\n")
fileOutput.write("fontP.set_size('small')\n")
fileOutput.write("plt.legend(prop=fontP)\n")
fileOutput.write("plt.savefig(timestr+'_'+'TqLnrBC'+fileOutput+'.png')\n")

fileOutput.write("fig2 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('T(q)')\n")	
fileOutput.write("plt.title('Exponentes de masa')\n")
fileOutput.write("plt.plot(range(0,maxq), Tq[IndexZero:-1],'b<-')\n")
fileOutput.write("fontP = FontProperties()\n")
fileOutput.write("fontP.set_size('small')\n")
fileOutput.write("plt.legend(prop=fontP)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Tq'+fileOutput+'.png')\n")

fileOutput.write("fig3 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('D(q)')\n")	
fileOutput.write("plt.title(u'Dimensión fractal generalizada')\n")
fileOutput.write("plt.plot(range(0,maxq), Dq[IndexZero:-1],'b<-')\n")
fileOutput.write("fontP = FontProperties()\n")
fileOutput.write("fontP.set_size('small')\n")
fileOutput.write("plt.legend(prop=fontP)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Dq'+fileOutput+'.png')\n")

fileOutput.close()
