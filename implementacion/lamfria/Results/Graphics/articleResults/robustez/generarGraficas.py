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
percentNodes=[ 0,10,20,30,40,50,60,70,80,90]
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
fig1 = plt.figure()
plt.xlabel('Porcentaje de nodos eliminados (%)', fontdict=font)
plt.ylabel(u'Tamaño',fontdict=font)
plt.title(u'Tamaño componente gigante', fontdict=font)
plt.plot(percentNodes[0:GCRandom.shape[0]], GCRandom,'b<-' ,label='Aleatorio R='+"{0:.2f}".format(numpy.sum(GCRandom)))
plt.plot(percentNodes[0:GCDegree.shape[0]], GCDegree,'g<-' ,label='Grado R='+"{0:.2f}".format(numpy.sum(GCDegree)))
plt.plot(percentNodes[0:GCCentrality.shape[0]], GCCentrality,'r<-' ,label='Centralidad R='"{0:.2f}".format(numpy.sum(GCCentrality)))
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('GC'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
fig2 = plt.figure()
plt.xlabel('Porcentaje de nodos eliminados (%)', fontdict=font)
plt.ylabel(u'Diámetro camino', fontdict=font)
plt.title(u'Distancia promedio', fontdict=font)
plt.plot(percentNodes[0:APLRandom.shape[0]], APLRandom,'b<-' ,label='Aleatorio R='+"{0:.2f}".format(numpy.sum(APLRandom)))
plt.plot(percentNodes[0:APLDegree.shape[0]], APLDegree,'g<-' ,label='Grado R='+"{0:.2f}".format(numpy.sum(APLDegree)))
plt.plot(percentNodes[0:APLCentrality.shape[0]], APLCentrality,'r<-' ,label='Centralidad R='+"{0:.2f}".format(numpy.sum(APLCentrality)))
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('APL'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
