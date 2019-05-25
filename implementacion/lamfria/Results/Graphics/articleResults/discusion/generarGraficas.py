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


DqRandom=numpy.array([[ 5.56843009, 5.56711845, 5.5654536 , 5.56333482, 5.56062892, 5.55715763,
   5.55267701, 5.54683556, 5.539059  , 5.52809143, 5.50914291, 5.4454491 ,
   5.00513686, 4.05793526, 3.54244744, 3.27611305, 3.11134733, 2.99732783,
   2.91256539, 2.8464087 , 2.79296807],
 [ 5.28143631, 5.28088001, 5.28008915, 5.27899088, 5.27748423, 5.27542612,
   5.27260666, 5.26869803, 5.2631182 , 5.25451279, 5.23767093, 5.17470113,
   4.75231275, 3.84434371, 3.33383336, 3.06857005, 2.90383673, 2.78959764,
   2.70475851, 2.63879864, 2.58582709],
 [ 5.06774161, 5.07159509, 5.07520054, 5.07851466, 5.08148627, 5.08404483,
   5.08607758, 5.08737831, 5.08750596, 5.08525071, 5.07555601, 5.02219747,
   4.63809777, 3.77448698, 3.26984561, 3.00810997, 2.84655288, 2.73504155,
   2.65249243, 2.58843703, 2.53704941],
 [ 4.6620829 , 4.66704144, 4.67187748, 4.67649964, 4.680789  , 4.6845861 ,
   4.6876672 , 4.68969047, 4.69003881, 4.68720198, 4.67527259, 4.61567082,
   4.24664216, 3.45166536, 2.96929742, 2.72035973, 2.56886859, 2.46569761,
   2.39029348, 2.33245398, 2.28650078],
 [ 4.47155614, 4.47339609, 4.47515029, 4.47676169, 4.47814571, 4.47917476,
   4.47964904, 4.47923112, 4.47726096, 4.47204833, 4.45702008, 4.39215519,
   4.03732364, 3.30292919, 2.84196848, 2.60041289, 2.45277034, 2.35176573,
   2.27760395, 2.22048801, 2.17496629],
 [ 4.16842853, 4.16905496, 4.16965407, 4.17017101, 4.17051463, 4.17053544,
   4.16998685, 4.16844378, 4.16507967, 4.1578237 , 4.13895294, 4.06560422,
   3.71953377, 3.04875031, 2.61106834, 2.37860833, 2.23678476, 2.13991537,
   2.06887362, 2.01422857, 1.97073123],
 [ 3.69759307, 3.69761103, 3.69747144, 3.69709348, 3.69635582, 3.69507213,
   3.69294466, 3.68945947, 3.68359001, 3.67270397, 3.64735014, 3.56238457,
   3.24165078, 2.67586291, 2.28179481, 2.06472494, 1.93213986, 1.84170181,
   1.7753348 , 1.72421856, 1.6834838 ],
 [ 3.05500542, 3.05599906, 3.05712407, 3.05838792, 3.05977864, 3.06123778,
   3.06260105, 3.0634585 , 3.06277416, 3.05761832, 3.03801063, 2.96428433,
   2.71420635, 2.2786317 , 1.93887236, 1.73898864, 1.61658115, 1.53450641,
   1.47535269, 1.4304994 , 1.39523704],
 [ 2.40950859, 2.40953487, 2.40947309, 2.40927462, 2.40886152, 2.40810186,
   2.40675461, 2.40433268, 2.39971432, 2.38987432, 2.36523331, 2.29334932,
   2.10082357, 1.81474865, 1.60003272, 1.47349139, 1.39652553, 1.3460157 ,
   1.3106033 , 1.28443881, 1.26429116],
 [ 1.78395645, 1.78161669, 1.7787572 , 1.77518375, 1.7705929 , 1.76448644,
   1.75599903, 1.74353694, 1.72401373, 1.69136058, 1.63473526, 1.5422762 ,
   1.42258851, 1.31281087, 1.23493288, 1.18436353, 1.15111293, 1.1282343 ,
   1.11171679, 1.09928465, 1.08960402]]
)
GCRandom=numpy.array([ 1.   , 0.729, 0.596, 0.387, 0.3  , 0.207, 0.122, 0.059, 0.027, 0.007]
)
APLRandom=numpy.array([ 1.        , 1.00177736, 1.00833322, 1.01294382, 1.00393039, 0.99506119,
  0.99135358, 0.98187327, 0.94728916, 0.58732804]

)
DqDegree=numpy.array([[ 5.04053981, 5.04747717, 5.05462097, 5.06191832, 5.06928587, 5.07659845,
   5.08367648, 5.09027448, 5.09607356, 5.10063096, 5.10217879, 5.07278371,
   4.65365554, 3.90104766, 3.75681434, 3.72681382, 3.70472856, 3.68352094,
   3.66307863, 3.64365667, 3.62543798],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan]]
)
GCDegree=numpy.array([ 1.   , 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
)
APLDegree=numpy.array([ 1.        , 0.34612411, 0.34612411, 0.34612411, 0.34612411, 0.34612411,
  0.34612411, 0.34612411, 0.34612411, 0.34612411]

)
DqCentrality=numpy.array([[ 5.56829067, 5.56695965, 5.5652722 , 5.56312686, 5.56038947, 5.55688049,
   5.5523542 , 5.54645628, 5.53860685, 5.52753412, 5.50837314, 5.44370353,
   4.99621763, 4.04580781, 3.53290338, 3.26796753, 3.10402288, 2.99053876,
   2.90614552, 2.84024925, 2.78699164],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan]]
)
GCCentrality=numpy.array([ 1.   , 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
)
APLCentrality=numpy.array([ 1.        , 0.34618603, 0.34618603, 0.34618603, 0.34618603, 0.34618603,
  0.34618603, 0.34618603, 0.34618603, 0.34618603])
fileOutput = '20190524_213455RedJoshua1'
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
