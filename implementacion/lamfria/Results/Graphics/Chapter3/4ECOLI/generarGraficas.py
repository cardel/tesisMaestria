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
symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
IndexZero=10

logRA=numpy.array([-2.19722458,-1.5040774 ,-1.09861229,-0.81093022,-0.58778666,-0.40546511,
 -0.25131443,-0.11778304, 0.        ]
)
TqA=numpy.array([ -4.43718683e+00, -4.43669267e+00, -4.43570605e+00, -4.43374062e+00,
  -4.42984412e+00, -4.42219674e+00, -4.40749925e+00, -4.38045027e+00,
  -4.33496303e+00, -4.27011426e+00, -3.43263048e+00, -4.04746061e-18,
   2.73334990e+00,  4.54127229e+00,  6.01821732e+00,  7.36629013e+00,
   8.63806845e+00,  9.85612311e+00,  1.10338550e+01,  1.21805952e+01,
   1.33033607e+01]
)
DqA=numpy.array([ 0.40338062, 0.44366927, 0.49285623, 0.55421758, 0.63283487, 0.73703279,
  0.88149985, 1.09511257, 1.44498768, 2.13505713, 3.43263048, 3.41397347,
  2.7333499 , 2.27063614, 2.00607244, 1.84157253, 1.72761369, 1.64268719,
  1.576265  , 1.52257439, 1.47815119]
)
lnMrqA=numpy.array([[  8.51996078e+01,  8.36451396e+01,  8.31163677e+01,  8.21765824e+01,
    8.14118340e+01,  7.99493755e+01,  7.82157258e+01,  7.64249820e+01,
    7.45992351e+01],
 [  7.73607912e+01,  7.58064815e+01,  7.52776207e+01,  7.43378468e+01,
    7.35730577e+01,  7.21109271e+01,  7.03779068e+01,  6.85872360e+01,
    6.67614731e+01],
 [  6.95222931e+01,  6.79683059e+01,  6.74392649e+01,  6.64995145e+01,
    6.57346430e+01,  6.42731726e+01,  6.25414078e+01,  6.07508776e+01,
    5.89250762e+01],
 [  6.16844386e+01,  6.01311140e+01,  5.96017047e+01,  5.86620041e+01,
    5.78969645e+01,  5.64368262e+01,  5.47075582e+01,  5.29172925e+01,
    5.10913955e+01],
 [  5.38478917e+01,  5.22959479e+01,  5.17657772e+01,  5.08261847e+01,
    5.00607967e+01,  4.86033531e+01,  4.68790206e+01,  4.50892329e+01,
    4.32630895e+01],
 [  4.60140209e+01,  4.44650171e+01,  4.39332482e+01,  4.29938961e+01,
    4.22277688e+01,  4.07757830e+01,  3.90610857e+01,  3.72720996e+01,
    3.54453033e+01],
 [  3.81856868e+01,  3.66431545e+01,  3.61079549e+01,  3.51691522e+01,
    3.44013883e+01,  3.29604245e+01,  3.12640591e+01,  2.94762227e+01,
    2.76476751e+01],
 [  3.03689876e+01,  2.88414362e+01,  2.82986610e+01,  2.73611274e+01,
    2.65894879e+01,  2.51704323e+01,  2.35071427e+01,  2.17203787e+01,
    1.98871772e+01],
 [  2.25772954e+01,  2.10870433e+01,  2.05271229e+01,  1.95923820e+01,
    1.88106277e+01,  1.74329201e+01,  1.58231225e+01,  1.40357061e+01,
    1.21906405e+01],
 [  1.48412057e+01,  1.34527262e+01,  1.28552294e+01,  1.19250105e+01,
    1.11134456e+01,  9.80232581e+00,  8.26111912e+00,  6.46954718e+00,
    4.60538036e+00],
 [  7.23670024e+00,  6.15105431e+00,  5.50162160e+00,  4.57235327e+00,
    3.67519633e+00,  2.47969873e+00,  1.23807725e+00,  3.40334520e-01,
    5.76814361e-02],
 [  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.11022302e-16,
   -1.11022302e-16,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -6.01709428e+00, -3.18162416e+00, -1.41155625e+00, -4.69276247e-01,
   -1.29686158e-01, -3.22144687e-02, -6.96215479e-03, -1.16181373e-03,
   -1.41948830e-04],
 [ -1.02321687e+01, -4.94970828e+00, -2.05715831e+00, -6.87046291e-01,
   -1.91171321e-01, -4.79005762e-02, -1.03952811e-02, -1.73831264e-03,
   -2.12726814e-04],
 [ -1.36821388e+01, -6.39384807e+00, -2.55931636e+00, -8.64493611e-01,
   -2.43768981e-01, -6.15619006e-02, -1.34387191e-02, -2.27912778e-03,
   -2.82309504e-04],
 [ -1.68540196e+01, -7.68026609e+00, -2.98912433e+00, -1.01999892e+00,
   -2.91459693e-01, -7.41331677e-02, -1.62757045e-02, -2.80090809e-03,
   -3.51232473e-04],
 [ -1.98683208e+01, -8.86055474e+00, -3.37362179e+00, -1.16064279e+00,
   -3.35759542e-01, -8.59658164e-02, -1.89719796e-02, -3.30668736e-03,
   -4.19516219e-04],
 [ -2.27743484e+01, -9.96057751e+00, -3.72676744e+00, -1.29018327e+00,
   -3.77477172e-01, -9.72419283e-02, -2.15611105e-02, -3.79803813e-03,
   -4.87171940e-04],
 [ -2.56008133e+01, -1.09968464e+01, -4.05672633e+00, -1.41093469e+00,
   -4.17116261e-01, -1.08072270e-01, -2.40633658e-02, -4.27622102e-03,
   -5.54210424e-04],
 [ -2.83674447e+01, -1.19815973e+01, -4.36867146e+00, -1.52446293e+00,
   -4.55021258e-01, -1.18531174e-01, -2.64922998e-02, -4.74233600e-03,
   -6.20642234e-04],
 [ -3.10888694e+01, -1.29246216e+01, -4.66608247e+00, -1.63189957e+00,
   -4.91442998e-01, -1.28671926e-01, -2.88576168e-02, -5.19735648e-03,
   -6.86477716e-04]]
)
logRB=numpy.array([-2.19722458,-1.5040774 ,-1.09861229,-0.81093022,-0.58778666,-0.40546511,
 -0.25131443,-0.11778304, 0.        ]
)
TqB=numpy.array([ -4.75767234e+01, -4.31738234e+01, -3.87711252e+01, -3.43688364e+01,
  -2.99673850e+01, -2.55676654e+01, -2.11715886e+01, -1.67833782e+01,
  -1.24128547e+01, -8.08463155e+00, -3.85907339e+00, -2.48317518e-17,
   2.25043806e+00,  3.73395849e+00,  5.07744792e+00,  6.39433871e+00,
   7.70153042e+00,  9.00343627e+00,  1.03019039e+01,  1.15979825e+01,
   1.28923661e+01]
)
DqB=numpy.array([ 4.32515668, 4.31738234, 4.30790279, 4.29610455, 4.281055  , 4.26127756,
  4.23431772, 4.19584456, 4.13761822, 4.04231577, 3.85907339, 3.02916024,
  2.25043806, 1.86697925, 1.69248264, 1.59858468, 1.54030608, 1.50057271,
  1.47170055, 1.44974781, 1.43248512]
)
lnMrqB=numpy.array([[  8.51118505e+01,  8.35334691e+01,  8.29558598e+01,  8.09565768e+01,
    7.94902542e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  7.72730343e+01,  7.56948303e+01,  7.51169252e+01,  7.31177665e+01,
    7.16514480e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  6.94345370e+01,  6.78566916e+01,  6.72781916e+01,  6.52792986e+01,
    6.38129667e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  6.15966839e+01,  6.00195685e+01,  5.94398685e+01,  5.74415572e+01,
    5.59751346e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  5.37601393e+01,  5.21845227e+01,  5.16023934e+01,  4.96053939e+01,
    4.81385970e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  4.59262720e+01,  4.43537760e+01,  4.37667024e+01,  4.17727565e+01,
    4.03046333e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  3.80979432e+01,  3.65320872e+01,  3.59348746e+01,  3.39482431e+01,
    3.24757582e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  3.02812628e+01,  2.87300340e+01,  2.81117998e+01,  2.61429270e+01,
    2.46568292e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  2.24897162e+01,  2.09725122e+01,  2.03099963e+01,  1.83830675e+01,
    1.68569183e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  1.47547577e+01,  1.33232397e+01,  1.25653382e+01,  1.07248855e+01,
    9.09200741e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  7.15851400e+00,  5.96870756e+00,  4.99721227e+00,  3.29583687e+00,
    1.60943791e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  0.00000000e+00,  2.22044605e-16, -2.22044605e-16, -2.22044605e-16,
   -1.11022302e-16,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -5.51348898e+00, -1.90267722e+00, -2.56680484e-01, -3.89718062e-02,
   -3.94290554e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -9.27676176e+00, -2.92402645e+00, -3.85433993e-01, -5.84860166e-02,
   -5.91599414e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -1.26534438e+01, -3.90484093e+00, -5.13913295e-01, -7.79813836e-02,
   -7.88799309e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -1.59547215e+01, -4.88177980e+00, -6.42391624e-01, -9.74767295e-02,
   -9.85999136e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -1.92280292e+01, -5.85823008e+00, -7.70869949e-01, -1.16972075e-01,
   -1.18319896e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -2.24859908e+01, -6.83461442e+00, -8.99348273e-01, -1.36467421e-01,
   -1.38039879e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -2.57339532e+01, -7.81098964e+00, -1.02782660e+00, -1.55962767e-01,
   -1.57759862e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -2.89749653e+01, -8.78736358e+00, -1.15630492e+00, -1.75458113e-01,
   -1.77479845e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -3.22110455e+01, -9.76373735e+00, -1.28478325e+00, -1.94953459e-01,
   -1.97199827e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00]]
)
logRC=numpy.array([-2.07944154,-1.38629436,-0.98082925,-0.69314718,-0.47000363,-0.28768207,
 -0.13353139, 0.        ]
)
TqC=numpy.array([-38.28804506,-34.90607108,-31.50931806,-28.0912758 ,-24.65101221,
 -21.19511433,-17.73300548,-14.27137299,-10.80278151, -7.23910439,
  -3.51176844,  0.        ,  2.67296913,  4.6219822 ,  6.24644917,
   7.72794534,  9.1258365 , 10.46806653, 11.77121574, 13.04606441,
  14.29995699]
)
DqC=numpy.array([ 3.48073137, 3.49060711, 3.50103534, 3.51140947, 3.52157317, 3.53251906,
  3.5466011 , 3.56784325, 3.60092717, 3.6195522 , 3.51176844, 3.12815495,
  2.67296913, 2.3109911 , 2.08214972, 1.93198633, 1.8251673 , 1.74467775,
  1.68160225, 1.63075805, 1.58888411]
)
lnMrqC=numpy.array([[ -8.78736652,-15.96050659,-22.90569981,-28.79513761,-39.30732821,
  -63.30732664,-84.03078879,-86.22145628],
 [ -8.09094682,-14.84351338,-21.27855582,-26.81284397,-36.36446643,
  -58.18990867,-76.83850623,-78.38343225],
 [ -7.39282535,-13.71941129,-19.64622529,-24.82464593,-33.42004589,
  -53.07188647,-69.55277323,-70.54532793],
 [ -6.6920832 ,-12.58515523,-18.00659272,-22.82792025,-30.4737184 ,
  -47.95271983,-62.13221149,-62.70715273],
 [ -5.98726789,-11.43619364,-16.35630875,-20.81847205,-27.52497703,
  -42.83073038,-54.5645417 ,-54.86891488],
 [ -5.27603905,-10.26555915,-14.68983029,-18.78919007,-24.57292791,
  -37.70035566,-46.87768365,-47.03062157],
 [ -4.5545179 , -9.06221771,-12.99751527,-16.72726816,-21.6156017 ,
  -32.54471728,-39.11601383,-39.19227911],
 [ -3.81599605, -7.80772876,-11.26156321,-14.6083661 ,-18.64771719,
  -27.31995005,-31.31497748,-31.353893  ],
 [ -3.04806186, -6.46822108, -9.44617916,-12.38374382,-15.65134256,
  -21.86203272,-23.49514569,-23.51546806],
 [ -2.2250319 , -4.9694082 , -7.46417701, -9.93835798,-12.49421234,
  -15.38198892,-15.66668728,-15.67700852],
 [ -1.28221335, -3.08791731, -4.91480723, -6.52629083, -7.50370483,
   -7.79769193, -7.83427495, -7.83851809],
 [  0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
    0.        ,  0.        ,  0.        ],
 [  2.30709107,  5.09697066,  6.74929192,  7.50424256,  7.75219844,
    7.81898782,  7.83520177,  7.83854289],
 [  5.99232015, 11.15212737, 13.89526388, 15.1161328 , 15.52811984,
   15.64211782, 15.67090386, 15.67710808],
 [ 10.35022636, 17.5286634 , 21.19595421, 22.76827087, 23.31297453,
   23.46707587, 23.50690475, 23.51569337],
 [ 14.99195566, 24.06809715, 28.58252025, 30.44409936, 31.10302413,
   31.29317724, 31.34310385, 31.35429682],
 [ 19.79351069, 30.71506405, 36.02275274, 38.13623463, 38.89667554,
   39.120095  , 39.17944716, 39.19291674],
 [ 24.6973887 , 37.44233994, 43.49928528, 45.84058955, 46.69306403,
   46.94763742, 47.01590312, 47.03155162],
 [ 29.66968931, 44.23320991, 51.00200642, 53.55460712, 54.49165003,
   54.77567996, 54.85245166, 54.87020012],
 [ 34.68883943, 51.07569618, 58.52464288, 61.27654693, 62.29206519,
   62.60413644, 62.68907897, 62.70886109],
 [ 39.74072316, 57.96034594, 66.06307443, 69.00514863, 70.09404194,
   70.43294441, 70.52577502, 70.54753348]]
)
fileOutput = 'ecoli'
timestr = 'a'
fig1 = plt.figure()
ax1 = plt.subplot(311)
i = 0
for q in range(minq,maxq+1):
	if q%2==0 and q>-6 and q<=6:
		plt.plot(logRA,lnMrqA[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))
	i+=1
plt.ylabel(r'$\ln(Z(r)^q)$')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.grid(True)
lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))
ax2 = plt.subplot(312)
i = 0
for q in range(minq,maxq+1):
	if q%2==0 and q>-6 and q<=6:
		plt.plot(logRB,lnMrqB[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))
	i+=1
plt.ylabel(r'$\ln(Z(r)^q)$')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.grid(True)
ax3 = plt.subplot(313)
i = 0
for q in range(minq,maxq+1):
	if q%2==0 and q>-6 and q<=6:
		plt.plot(logRC,lnMrqC[i],symbols[int(math.fmod(i,numpy.size(symbols)))], label='q='+str(q))
	i+=1
plt.ylabel(r'$\ln(\overline{Z(r)^q)}$')
plt.xlabel(r'$ln(\frac{r}{d})$')
plt.grid(True)
plt.suptitle(u'Regresión lineal para red aleatoria 5620 nodos', fontsize=11)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.savefig(timestr+'_'+'TqLnrBC'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
fig2 = plt.figure()
plt.xlabel('q')
plt.ylabel('T(q)')
plt.title('Exponentes de masa')
plt.plot(range(minq,maxq+1), TqA,'b<-' ,label='FSBC')
plt.plot(range(minq,maxq+1), TqB,'g<-' ,label='BCC')
plt.plot(range(minq,maxq+1), TqC,'r<-' ,label='SB')
plt.xticks(range(minq,maxq+1))
lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig(timestr+'_'+'Tq'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
fig3 = plt.figure()
plt.xlabel('q')
plt.ylabel('D(q)')
plt.title(u'Dimensión fractal generalizada')
plt.plot(range(0,maxq), DqA[IndexZero:-1],'b<-' ,label='FSBC')
plt.plot(range(0,maxq), DqB[IndexZero:-1],'g<-' ,label='BCC')
plt.plot(range(0,maxq), DqC[IndexZero:-1],'r<-' ,label='SB')
plt.xticks(range(0,maxq))
lgd = plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig(timestr+'_'+'Dq'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
