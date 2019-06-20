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
ax = fig3.add_subplot(111)
deltaA = numpy.array([])
deltaB = numpy.array([])
deltaC = numpy.array([])
deltaD = numpy.array([])
deltaE = numpy.array([])
deltaF = numpy.array([])
for i in range(0,9):
	if i < DqRandom.shape[0]:
		deltaA = numpy.append(deltaA, numpy.max(DqRandom[i][IndexZero:-1])-numpy.min(DqRandom[i][IndexZero:-1]))
	if i < DqDegree.shape[0]:
		deltaB = numpy.append(deltaB, numpy.max(DqDegree[i][IndexZero:-1])-numpy.min(DqDegree[i][IndexZero:-1]))
	if i < DqCentrality.shape[0]:
		deltaC = numpy.append(deltaC, numpy.max(DqCentrality[i][IndexZero:-1])-numpy.min(DqCentrality[i][IndexZero:-1]))
plt.plot(range(0,10*deltaA.shape[0],10),deltaA,'r-' , label = r'$\Delta D_q$ ataque aleatorio')
plt.plot(range(0,10*deltaB.shape[0],10),deltaB,'g-' , label = r'$\Delta D_q$ ataque por grado')
plt.plot(range(0,10*deltaC.shape[0],10),deltaC,'b-' , label = r'$\Delta D_q$ ataque centralidad')
fontP = FontProperties()
fontP.set_size('small')
plt.xlabel('% Nodos perdidos', fontdict=font)
plt.ylabel(r'Diferencia maximo y minimo $\Delta D_q$', fontdict=font)
plt.title(u'Multifractalidad y robustez', fontdict=font)
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('multirobus'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
