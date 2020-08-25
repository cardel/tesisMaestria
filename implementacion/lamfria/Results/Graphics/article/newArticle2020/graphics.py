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
maxq = 10
IndexZero = 10
symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
nan=float('nan')
percentNodes=[ 0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
font = {'weight': 'normal', 'size': 8}

#Generar gráficas

fig, axs = plt.subplots(2,2, sharex=True)
county = 0
countx = 0
    
fontP = FontProperties()
fontP.set_size('small')

my_suptitle= fig.suptitle('R index MFA', fontdict=font)



for i in RIndex:
	name = ""
	if "Small" in i:
		name = "Small World"
	elif "Random" in i:
		name = "Random"
	elif "Scale" in i:
		name = "Scale Free"
	elif "Cele" in i:
		name = "Celegans"
	else:
		error("No se encuentra")
	
	font = {'weight': 'normal', 'size': 8}
	
	data = RIndex[i]
	
	RRandom = data[0]
	RDegree = data[1]
	RCentrality = data[2]

	axs[countx,county].plot(range(0,maxq),RRandom[IndexZero:-1],'r-' , label = u'R random')
	axs[countx,county].plot(range(0,maxq),RDegree[IndexZero:-1],'g-' , label = u'R degree')
	axs[countx,county].plot(range(0,maxq),RCentrality[IndexZero:-1],'b-' , label = u'R centrality')	
		
	axs[countx,county].set_title(name, fontsize=10)
	

	
	axs[countx,county].grid(True)	
	
	if countx == 0 and county == 0:
		countx = 1
	elif county == 0:
		countx = 0
		county = 1
	elif countx == 0 and county == 1:
		countx = 1
	


for ax in axs.flat:
	ax.set_xlabel('R-index', fontdict=font)
	ax.set_ylabel('q', fontdict=font)
    
for ax in axs.flat:
    ax.label_outer()


lgd = axs[0,1].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))

fig.savefig('composicionRIndex.png', bbox_extra_artists=(lgd,my_suptitle),bbox_inches='tight')


##Segunda grafica

fig, axs = plt.subplots(2,2, sharex=True)
county = 0
countx = 0
    
fontP = FontProperties()
fontP.set_size('small')

my_suptitle=fig.suptitle(u'Multifractality and robustness', fontdict=font)

for i in RIndex:
	name = ""
	if "Small" in i:
		name = "Small World"
	elif "Random" in i:
		name = "Random"
	elif "Scale" in i:
		name = "Scale Free"
	elif "Cele" in i:
		name = "Celegans"
	else:
		error("No se encuentra")
	
	font = {'weight': 'normal', 'size': 8}
	
	data = RIndex[i]
	
	deltaA = data[0]
	deltaB = data[1]
	deltaC = data[2]

	axs[countx,county].plot(range(0,10*deltaA.shape[0],10),deltaA,'r-' , label = r'$\Delta D_q$ random')
	axs[countx,county].plot(range(0,10*deltaB.shape[0],10),deltaB,'g-' , label = r'$\Delta D_q$ degree')
	axs[countx,county].plot(range(0,10*deltaC.shape[0],10),deltaC,'b-' , label = r'$\Delta D_q$ centrality')
	
		
	axs[countx,county].set_title(name, fontsize=10)
	
	axs[countx,county].grid(True)	
	
	if countx == 0 and county == 0:
		countx = 1
	elif county == 0:
		countx = 0
		county = 1
	elif countx == 0 and county == 1:
		countx = 1
		
for ax in axs.flat:
	ax.set_xlabel(r'% nodes', fontdict=font)
	ax.set_ylabel(r'$\delta D_q$', fontdict=font)
    
for ax in axs.flat:
    ax.label_outer()
    

lgd = axs[0,1].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))

fig.savefig('composicionDqFractal.png', bbox_extra_artists=(lgd,my_suptitle),bbox_inches='tight')
