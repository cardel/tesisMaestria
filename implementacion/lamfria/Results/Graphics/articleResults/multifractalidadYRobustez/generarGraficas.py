#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt
import time
import math
from matplotlib.font_manager import FontProperties
minq = -10
maxq = 10
IndexZero = 10
symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
nan=float('nan')
percentNodes=[ 0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


DqRandom=numpy.array([[ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan]]
)
GCRandom=numpy.array([  1.00000000e+00,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04]
)
APLRandom=numpy.array([ 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

)
DqDegree=numpy.array([[ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan]]
)
GCDegree=numpy.array([  1.00000000e+00,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04]
)
APLDegree=numpy.array([ 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

)
DqCentrality=numpy.array([[ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan],
 [ nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
   nan, nan, nan, nan, nan, nan, nan]]
)
GCCentrality=numpy.array([  1.00000000e+00,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04]
)
APLCentrality=numpy.array([ 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
fileOutput = '20190619_220318YeastS.net'
timestr = 'grafica'
font = {'weight': 'normal', 'size': 8}
fig3 = plt.figure()
for i in range(0,9):
	if i < DqRandom.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqRandom[i]))) == 1:
		plt.plot(range(0,maxq),DqRandom[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')
fontP = FontProperties()
fontP.set_size('small')
plt.legend(prop=fontP)
plt.xlabel('Escalado q', fontdict=font)
plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)
plt.title(u'Multifractalidad ataque aleatorio', fontdict=font)
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('DqRandom'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
fig4 = plt.figure()
for i in range(0,9):
	if i < DqDegree.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqDegree[i]))) == 1:
		plt.plot(range(0,maxq),DqDegree[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')
fontP = FontProperties()
fontP.set_size('small')
plt.legend(prop=fontP)
plt.xlabel('Escalado q', fontdict=font)
plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)
plt.title(u'Multifractalidad ataque por grado', fontdict=font)
lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('DqDegree'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
fig5 = plt.figure()
for i in range(0,9):
	if i < DqCentrality.shape[0] and numpy.prod(numpy.logical_not(numpy.isnan(DqCentrality[i]))) == 1:
		plt.plot(range(0,maxq),DqCentrality[i][IndexZero:-1],symbols[int(math.fmod(i,numpy.size(symbols)))], label='% nodes='+str(int(100*percentNodes[i]))+'%')
fontP = FontProperties()
fontP.set_size('small')
plt.legend(prop=fontP)
plt.xlabel('Escalado (q)', fontdict=font)
plt.ylabel(u'Dimensión fractal D(q)', fontdict=font)
plt.title(u'Multifractalidad ataque por centralidad', fontdict=font)
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('DqCentrality'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
