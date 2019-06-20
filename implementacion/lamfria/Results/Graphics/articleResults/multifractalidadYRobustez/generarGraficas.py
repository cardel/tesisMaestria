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


DqRandom=numpy.array([[ 3.60258315, 3.58927317, 3.5733148 , 3.55386616, 3.52963607, 3.49848824,
   3.45655792, 3.3964774 , 3.30457054, 3.15417591, 2.90593304, 2.6195087 ,
   2.3688817 , 2.16378792, 2.01073254, 1.8989043 , 1.81574297, 1.7522715 ,
   1.70252595, 1.66258342, 1.62983289],
 [ 3.53314424, 3.52641352, 3.51820654, 3.50791024, 3.49431997, 3.47532451,
   3.44797835, 3.40786139, 3.34571328, 3.233823  , 3.01938984, 2.74153507,
   2.4874696 , 2.27544172, 2.11554917, 1.99875874, 1.91217434, 1.84626131,
   1.79470719, 1.75338555, 1.71955722],
 [ 3.3477483 , 3.33560116, 3.32088277, 3.30263227, 3.27931203, 3.24838872,
   3.20588216, 3.14531681, 3.05408752, 2.90434234, 2.66629839, 2.40356554,
   2.17630539, 1.98900171, 1.84779567, 1.74468888, 1.66812216, 1.6096345 ,
   1.56370697, 1.52675918, 1.49641748],
 [ 3.26119671, 3.25312206, 3.24307985, 3.23050864, 3.21455062, 3.19371343,
   3.16510032, 3.12274008, 3.05500849, 2.94141083, 2.74462368, 2.50499228,
   2.2851794 , 2.09774823, 1.95269658, 1.84528043, 1.76502024, 1.70354466,
   1.65521846, 1.61633056, 1.58439857],
 [ 3.16575626, 3.15688723, 3.14593248, 3.13222238, 3.11481819, 3.0923695 ,
   3.06256316, 3.02021927, 2.95395034, 2.84126566, 2.65250139, 2.42651893,
   2.21790186, 2.03743455, 1.8960537 , 1.79098153, 1.71252754, 1.65251378,
   1.60536235, 1.56740005, 1.53618388],
 [ 2.9181895 , 2.91046265, 2.90119798, 2.88994822, 2.8759918 , 2.85797814,
   2.83325857, 2.79734132, 2.74246773, 2.64939696, 2.48891413, 2.2873964 ,
   2.09729747, 1.93082141, 1.79746456, 1.69683555, 1.62125908, 1.56344983,
   1.51818779, 1.48193483, 1.45229639],
 [ 2.78597529, 2.78151767, 2.77569536, 2.7679643 , 2.75757963, 2.7434779 ,
   2.72390817, 2.69551718, 2.65068282, 2.57233403, 2.44255599, 2.27817722,
   2.11229085, 1.95975844, 1.83368534, 1.73731832, 1.66471045, 1.60909944,
   1.56548667, 1.53048564, 1.50181486],
 [ 2.27733126, 2.27253785, 2.26682784, 2.25991248, 2.25128267, 2.24001551,
   2.22446517, 2.20154991, 2.16486528, 2.10051515, 1.99083186, 1.85220874,
   1.71829653, 1.60134691, 1.50656436, 1.43362076, 1.37784527, 1.33446074,
   1.29995157, 1.27191493, 1.24871019],
 [ 2.14247432, 2.13630312, 2.1286942 , 2.11910058, 2.10673175, 2.0904278 ,
   2.06835123, 2.03732452, 1.99202606, 1.92540561, 1.83397492, 1.72589424,
   1.61489801, 1.51181503, 1.42512254, 1.35705525, 1.30464526, 1.26391141,
   1.23164067, 1.20554825, 1.18405109],
 [ 1.33997729, 1.33597354, 1.33097351, 1.32463643, 1.31648921, 1.30589358,
   1.29204996, 1.27411408, 1.25147585, 1.22390516, 1.19102842, 1.15180968,
   1.1058251 , 1.05611461, 1.00880309, 0.9683628 , 0.93565554, 0.90960789,
   0.88877532, 0.87191622, 0.85808251]]
)
GCRandom=numpy.array([ 1.        , 0.80897925, 0.69377382, 0.57390936, 0.45870394, 0.35154596,
  0.24311732, 0.15078357, 0.07793308, 0.01863617]
)
APLRandom=numpy.array([ 1.        , 1.01992834, 1.03105193, 1.04631924, 1.0631212 , 1.19386158,
  1.21412388, 1.37595295, 1.26409354, 1.548324  ]

)
DqDegree=numpy.array([[ 3.68718483, 3.67635212, 3.66336593, 3.647549  , 3.62782802, 3.60231675,
   3.56737563, 3.51596732, 3.43573717, 3.30276662, 3.07330159, 2.78989687,
   2.52925374, 2.31144049, 2.14795045, 2.02860163, 1.94008023, 1.87268424,
   1.8199596 , 1.77767697, 1.74303392],
 [ 2.71311089, 2.70691723, 2.69934439, 2.68987304, 2.67787998, 2.66250759,
   2.64206296, 2.61312963, 2.56936452, 2.50085567, 2.40571044, 2.29888741,
   2.19496613, 2.10315645, 2.0282105 , 1.96945498, 1.92352242, 1.88702373,
   1.85738721, 1.83281641, 1.81207255],
 [ 1.11283425, 1.10859093, 1.10355861, 1.097553  , 1.09034472, 1.08165661,
   1.07117322, 1.05857617, 1.04362312, 1.02627783, 1.00685544, 0.98608193,
   0.96496777, 0.94453171, 0.92555126, 0.90846772, 0.89342474, 0.88036093,
   0.86910095, 0.85942306, 0.85110084],
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
GCDegree=numpy.array([  1.00000000e+00,  5.29860229e-01,  2.03303685e-02,  8.47098687e-04,
   4.23549343e-04,  4.23549343e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04]
)
APLDegree=numpy.array([ 1.        , 1.7779524 , 1.80439806, 0.18729934, 0.18729934, 0.18729934,
  0.18729934, 0.18729934, 0.18729934, 0.18729934]

)
DqCentrality=numpy.array([[ 3.6038368 , 3.59055966, 3.57463124, 3.55520064, 3.53095841, 3.49972747,
   3.45759262, 3.39728178, 3.30542763, 3.15551776, 2.90794597, 2.62134124,
   2.37025229, 2.16431813, 2.01049914, 1.89821429, 1.81480886, 1.75119451,
   1.70134751, 1.66131873, 1.6284864 ],
 [ 3.00180071, 2.99353829, 2.98352987, 2.9711407 , 2.95541935, 2.93502666,
   2.90797592, 2.87065034, 2.81597429, 2.73195104, 2.60909765, 2.46303803,
   2.31807154, 2.18557786, 2.07300133, 1.98198551, 1.90931953, 1.85101404,
   1.80372824, 1.76489523, 1.73259328],
 [ 2.10538803, 2.10103548, 2.09535037, 2.08787152, 2.07795074, 2.06465637,
   2.04664218, 2.02200994, 1.98819156, 1.94215235, 1.8833889 , 1.81737028,
   1.75000747, 1.68529154, 1.62771646, 1.57991619, 1.54127626, 1.50991493,
   1.48408148, 1.46245922, 1.44410228],
 [ 1.43957072, 1.43630458, 1.43224047, 1.42713999, 1.42068182, 1.4124283 ,
   1.40177999, 1.38792338, 1.36979412, 1.34610875, 1.31556397, 1.27734956,
   1.2320722 , 1.18269557, 1.13407469, 1.09047425, 1.05368472, 1.02347409,
   0.99880582, 0.97856459, 0.96180307],
 [ 0.88891008, 0.88491822, 0.88006779, 0.87415016, 0.86691394, 0.85806846,
   0.84730103, 0.83431842, 0.81892296, 0.80112474, 0.78126762, 0.76010959,
   0.73875739, 0.718391  , 0.69990826, 0.68373992, 0.66990611, 0.65818687,
   0.64827547, 0.63986765, 0.63269789],
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
GCCentrality=numpy.array([  1.00000000e+00,  6.27700127e-01,  3.00296485e-01,  1.60948751e-02,
   4.23549343e-03,  8.47098687e-04,  4.23549343e-04,  4.23549343e-04,
   4.23549343e-04,  4.23549343e-04]
)
APLCentrality=numpy.array([ 1.        , 1.60128576, 3.14484499, 1.06063841, 0.345379  , 0.02805238,
  0.18603158, 0.18603158, 0.18603158, 0.18603158])
fileOutput = '20190620_082514YeastUND'
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
