#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import math
from matplotlib.font_manager import FontProperties

Robust = {}
for filename in os.listdir('.'):
	if filename.startswith('Robust') and filename.endswith('.npy'):
		Robust[filename] = np.load(filename)
		

RIndex = {}
for filename in os.listdir('.'):
	if filename.startswith('Rindex') and filename.endswith('.npy'):
		RIndex[filename] = np.load(filename)
		
minq = -10
maxq = 11
IndexZero = 9
symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
nan=float('nan')
percentNodes=[0, 10, 20, 30, 40, 50, 60, 70, 80]
font = {'weight': 'normal', 'size': 8}

#Generar gráficas


#my_suptitle= fig.suptitle('R index MFA', fontdict=font)



for i in RIndex:
	
	plt.figure()
		
	fontP = FontProperties()
	fontP.set_size('small')

	name = ""
	if "Small" in i:
		name = "Small-World"
	elif "Random" in i:
		name = "Random"
	elif "Scale" in i:
		name = "Scale-Free"
	elif "Cele" in i:
		name = "Celegans"
	else:
		error("No se encuentra")
	
	font = {'weight': 'normal', 'size': 8}
	
	data = RIndex[i]
	
	RRandom = data[0]
	RDegree = data[1]
	RCentrality = data[2]

	plt.plot(range(0,maxq),RRandom[IndexZero:-1],'r-' , label = u'Random')
	plt.plot(range(0,maxq),RDegree[IndexZero:-1],'g-' , label = u'Degree')
	plt.plot(range(0,maxq),RCentrality[IndexZero:-1],'b-' , label = u'Centrality')		

	
	#plt.grid(True)	
	plt.xlabel('q', fontdict=font)
	plt.ylabel('R-index', fontdict=font)
	plt.xlim(right=10)
	plt.xlim(left=0)
	#lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	lgd = plt.legend(loc='best',prop={'size':8})

	#fig.savefig('composicionRIndex.png', bbox_extra_artists=(lgd,my_suptitle),bbox_inches='tight')
	plt.savefig(name+'composicionRIndex.png', bbox_extra_artists=(lgd,),bbox_inches='tight')



##Segunda grafica

fig, axs = plt.subplots(2,2, sharex=True)
county = 0
countx = 0
    
fontP = FontProperties()
fontP.set_size('small')

#my_suptitle=fig.suptitle(u'Differential fractal', fontdict=font)



for i in Robust:
	
	plt.figure()
		
	fontP = FontProperties()
	fontP.set_size('small')

	name = ""
	if "Small" in i:
		name = "Small-World"
	elif "Random" in i:
		name = "Random"
	elif "Scale" in i:
		name = "Scale-Free"
	elif "Cele" in i:
		name = "Celegans"
	else:
		error("No se encuentra")
	
	font = {'weight': 'normal', 'size': 8}
	
	data = Robust[i]
	
	deltaA = data[0]
	deltaB = data[1]
	deltaC = data[2]
	
	plt.xlim(right=80)
	plt.xlim(left=0)

	plt.plot(percentNodes,deltaA,'r-' , label = r'Random')
	plt.plot(percentNodes,deltaB,'g-' , label = r'Degree')
	plt.plot(percentNodes,deltaC,'b-' , label = r'Centrality')
	
	#plt.grid(True)	
	plt.xlabel('% removed nodes', fontdict=font)
	plt.ylabel(r'$\Delta D_q$', fontdict=font)

	#lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	lgd = plt.legend(loc='best',prop={'size':8})

	#fig.savefig('composicionRIndex.png', bbox_extra_artists=(lgd,my_suptitle),bbox_inches='tight')
	plt.savefig(name+'composicionDqFractal.png', bbox_extra_artists=(lgd,),bbox_inches='tight')

