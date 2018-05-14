#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties

#FBCS algorithm
fileInput = open("data","r")
fileInput.readline() 
fileInput.readline() 

logRA = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 
indexZero=fileInput.readline()

fileInput.readline() 

TqA = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

DqA = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

cadena = ""
for i in range(0,126):
	cadena+=fileInput.readline()
	
lnMrqA = cadena

#BCC algorithm

fileInput.readline() 
fileInput.readline() 

logRB = fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 
fileInput.readline()

fileInput.readline() 

TqB = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

DqB = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

cadena = ""
for i in range(0,84):
	cadena+=fileInput.readline()
	
lnMrqB = cadena

#SandBox Algorithm


fileInput.readline() 
fileInput.readline() 

logRC = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 
fileInput.readline()
fileInput.readline() 

TqC = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

DqC = fileInput.readline()+fileInput.readline()+fileInput.readline()+fileInput.readline()

fileInput.readline() 

cadena = ""
for i in range(0,84):
	cadena+=fileInput.readline()
	
lnMrqC = cadena


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


fileOutput.write("fileOutput = 'scaleFree4000Nodes'\n")
#fileOutput.write("timestr = time.strftime('%Y%m%d_%H%M%S')\n")
fileOutput.write("timestr = 'scaleFree4000'\n")


fileOutput.write("fig1 = plt.figure()\n")
fileOutput.write("ax1 = plt.subplot(311)\n")
fileOutput.write("i = 0\n")
fileOutput.write("for q in range(minq,maxq+1):\n")
fileOutput.write("	if q%2==0 and q>-6 and q<=6:\n")
fileOutput.write("		plt.plot(logRA,lnMrqA[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))\n")
fileOutput.write("	i+=1\n")
fileOutput.write("plt.ylabel(r'$\\ln(Z(r)^q)$')\n")
#fileOutput.write("plt.title(u'FSBC algorithm')\n")
#fileOutput.write("plt.xlabel(r'$ln(\\frac{r}{d})$')\n")
fileOutput.write("plt.setp(ax1.get_xticklabels(), visible=False)\n")
fileOutput.write("plt.grid(True)\n")

fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")

fileOutput.write("ax2 = plt.subplot(312)\n")
fileOutput.write("i = 0\n")
fileOutput.write("for q in range(minq,maxq+1):\n")
fileOutput.write("	if q%2==0 and q>-6 and q<=6:\n")
fileOutput.write("		plt.plot(logRB,lnMrqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))\n")
fileOutput.write("	i+=1\n")
fileOutput.write("plt.ylabel(r'$\\ln(Z(r)^q)$')\n")
fileOutput.write("plt.setp(ax2.get_xticklabels(), visible=False)\n")
#fileOutput.write("plt.title(u'BCC algorithm')\n")
#fileOutput.write("plt.xlabel(r'$ln(\\frac{r}{d})$')\n")

fileOutput.write("plt.grid(True)\n")

fileOutput.write("ax3 = plt.subplot(313)\n")
fileOutput.write("i = 0\n")
fileOutput.write("for q in range(minq,maxq+1):\n")
fileOutput.write("	if q%2==0 and q>-6 and q<=6:\n")
fileOutput.write("		plt.plot(logRC,lnMrqC[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))\n")
fileOutput.write("	i+=1\n")
fileOutput.write("plt.ylabel(r'$\\ln(\\overline{Z(r)^q)}$')\n")
#fileOutput.write("plt.title(u'Sandbox algorithm')\n")
fileOutput.write("plt.xlabel(r'$ln(\\frac{r}{d})$')\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.suptitle(u'Regresión lineal para red libre de escala 4000 nodos', fontsize=11)\n")

fileOutput.write("plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)\n")
fileOutput.write("plt.savefig(timestr+'_'+'TqLnrBC'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")




fileOutput.write("fig2 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('T(q)')\n")	
fileOutput.write("plt.title('Exponentes de masa')\n")
fileOutput.write("plt.plot(range(minq,maxq+1), TqA,'b<-' ,label='FSBC')\n")
fileOutput.write("plt.plot(range(minq,maxq+1), TqB,'g<-' ,label='BCC')\n")
fileOutput.write("plt.plot(range(minq,maxq+1), TqC,'r<-' ,label='SB')\n")
fileOutput.write("plt.xticks(range(minq,maxq+1))\n")

fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Tq'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")



fileOutput.write("fig3 = plt.figure()\n")
fileOutput.write("plt.xlabel('q')\n")
fileOutput.write("plt.ylabel('D(q)')\n")	
fileOutput.write("plt.title(u'Dimensión fractal generalizada')\n")
fileOutput.write("plt.plot(range(0,maxq), DqA[IndexZero:-1],'b<-' ,label='FSBC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqB[IndexZero:-1],'g<-' ,label='BCC')\n")
fileOutput.write("plt.plot(range(0,maxq), DqC[IndexZero:-1],'r<-' ,label='SB')\n")
fileOutput.write("plt.xticks(range(0,maxq))\n")

fileOutput.write("lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))\n")
fileOutput.write("plt.grid(True)\n")
fileOutput.write("plt.savefig(timestr+'_'+'Dq'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')\n")

fileOutput.close()
