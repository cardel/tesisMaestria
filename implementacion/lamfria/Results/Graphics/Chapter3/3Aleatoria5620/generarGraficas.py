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

logRA=numpy.array([-2.63905733,-1.94591015,-1.54044504,-1.25276297,-1.02961942,-0.84729786,
 -0.69314718,-0.55961579,-0.44183275,-0.33647224,-0.24116206,-0.15415068,
 -0.07410797, 0.        ]
)
TqA=numpy.array([ -3.46916527, -3.46935199, -3.46973098, -3.47050577, -3.47210664,
  -3.47546561, -3.48266687, -3.49854889, -3.53472707, -3.61766542,
  -3.08332853,  0.        ,  3.33052985,  6.46299902,  9.47009734,
  12.38828201, 15.23860502, 18.03525272, 20.78858837, 23.50646142,
  26.19493814]
)
DqA=numpy.array([ 0.31537866, 0.3469352 , 0.38552566, 0.43381322, 0.49601523, 0.57924427,
  0.69653337, 0.87463722, 1.17824236, 1.80883271, 3.08332853, 3.45588226,
  3.33052985, 3.23149951, 3.15669911, 3.0970705 , 3.047721  , 3.00587545,
  2.96979834, 2.93830768, 2.91054868]
)
lnMrqA=numpy.array([[  9.24933720e+01,  9.14468100e+01,  9.09209113e+01,  9.03350989e+01,
    8.98858869e+01,  8.93881429e+01,  8.89215988e+01,  8.84596004e+01,
    8.79308300e+01,  8.72678164e+01,  8.63190719e+01,  8.51552962e+01,
    8.36806595e+01,  8.16267444e+01],
 [  8.39141847e+01,  8.28674696e+01,  8.23414280e+01,  8.17556503e+01,
    8.13064078e+01,  8.08086953e+01,  8.03421722e+01,  7.98801068e+01,
    7.93513307e+01,  7.86883127e+01,  7.77394950e+01,  7.65755623e+01,
    7.51008315e+01,  7.30469687e+01],
 [  7.53358071e+01,  7.42887861e+01,  7.37624541e+01,  7.31767450e+01,
    7.27274412e+01,  7.22297919e+01,  7.17633103e+01,  7.13011103e+01,
    7.07723226e+01,  7.01092946e+01,  6.91603273e+01,  6.79960771e+01,
    6.65211575e+01,  6.44673997e+01],
 [  6.67590820e+01,  6.57114515e+01,  6.51845257e+01,  6.45989507e+01,
    6.41495230e+01,  6.36520008e+01,  6.31856008e+01,  6.27231302e+01,
    6.21943179e+01,  6.15312667e+01,  6.05819900e+01,  5.94170946e+01,
    5.79417950e+01,  5.58882481e+01],
 [  5.81857608e+01,  5.71369261e+01,  5.66087720e+01,  5.60234554e+01,
    5.55737757e+01,  5.50765078e+01,  5.46102668e+01,  5.41472515e+01,
    5.36183860e+01,  5.29552776e+01,  5.20053500e+01,  5.08391331e+01,
    4.93630666e+01,  4.73099445e+01],
 [  4.96195375e+01,  4.85683740e+01,  4.80376397e+01,  4.74528036e+01,
    4.70026057e+01,  4.65058441e+01,  4.60399052e+01,  4.55757939e+01,
    4.50468100e+01,  4.43835467e+01,  4.34322159e+01,  4.22632626e+01,
    4.07856408e+01,  3.87333770e+01],
 [  4.10683369e+01,  4.00129366e+01,  3.94766638e+01,  3.88926539e+01,
    3.84413670e+01,  3.79455924e+01,  3.74801997e+01,  3.70138920e+01,
    3.64846319e+01,  3.58209044e+01,  3.48664363e+01,  3.36917314e+01,
    3.22109291e+01,  3.01604103e+01],
 [  3.25493623e+01,  3.14877032e+01,  3.09392471e+01,  3.03563537e+01,
    2.99026739e+01,  2.94087087e+01,  2.89441838e+01,  2.84735403e+01,
    2.79435910e+01,  2.72782903e+01,  2.63164420e+01,  2.51294096e+01,
    2.36420118e+01,  2.15950708e+01],
 [  2.40994316e+01,  2.30367795e+01,  2.24615132e+01,  2.18786200e+01,
    2.14191350e+01,  2.09278335e+01,  2.04641126e+01,  1.99852663e+01,
    1.94533342e+01,  1.87819335e+01,  1.78015148e+01,  1.65874683e+01,
    1.50860643e+01,  1.30465156e+01],
 [  1.57904261e+01,  1.47801371e+01,  1.41575165e+01,  1.35669925e+01,
    1.30903962e+01,  1.25988261e+01,  1.21322654e+01,  1.16390522e+01,
    1.10988673e+01,  1.04002489e+01,  9.36928612e+00,  8.09525172e+00,
    6.56391435e+00,  4.54852244e+00],
 [  7.72943237e+00,  6.99883696e+00,  6.42285263e+00,  5.86015592e+00,
    5.35548528e+00,  4.84642521e+00,  4.35148295e+00,  3.82310557e+00,
    3.22641309e+00,  2.43918980e+00,  1.43826361e+00,  5.79540470e-01,
    1.45608341e-01,  2.10025376e-02],
 [  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00,  0.00000000e+00],
 [ -7.40940088e+00, -6.30420399e+00, -5.24409511e+00, -4.15880954e+00,
   -3.07478866e+00, -2.01098867e+00, -1.07123259e+00, -4.32581758e-01,
   -1.34366208e-01, -3.32728291e-02, -6.51052769e-03, -1.07788989e-03,
   -1.55885538e-04, -1.92650452e-05],
 [ -1.45720035e+01, -1.21860537e+01, -9.92551274e+00, -7.67666171e+00,
   -5.47973803e+00, -3.40897611e+00, -1.70814441e+00, -6.58547706e-01,
   -2.01026984e-01, -4.96534035e-02, -9.73788077e-03, -1.61562135e-03,
   -2.33775607e-04, -2.88973000e-05],
 [ -2.15542571e+01, -1.78069802e+01, -1.43047560e+01, -1.08827205e+01,
   -7.58935846e+00, -4.57578351e+00, -2.22398967e+00, -8.42983325e-01,
   -2.56920105e-01, -6.39288506e-02, -1.26926142e-02, -2.11815794e-03,
   -3.08584523e-04, -3.84289521e-05],
 [ -2.83994137e+01, -2.32458459e+01, -1.84821866e+01, -1.38844864e+01,
   -9.51111984e+00, -5.60618541e+00, -2.67646046e+00, -1.00656990e+00,
   -3.07288357e-01, -7.71091246e-02, -1.55045087e-02, -2.60269733e-03,
   -3.81837108e-04, -4.79102122e-05],
 [ -3.51353315e+01, -2.85474534e+01, -2.25111224e+01, -1.67368760e+01,
   -1.12973352e+01, -6.54155088e+00, -3.08679076e+00, -1.15637616e+00,
   -3.53927917e-01, -8.95140431e-02, -1.82077041e-02, -3.07441752e-03,
   -4.53759512e-04, -5.73425019e-05],
 [ -4.17813088e+01, -3.37415872e+01, -2.64266852e+01, -1.94756198e+01,
   -1.29811483e+01, -7.40533444e+00, -3.46562666e+00, -1.29592637e+00,
   -3.97752682e-01, -1.01307370e-01, -2.08197257e-02, -3.53591543e-03,
   -5.24465194e-04, -6.67265317e-05],
 [ -4.83516353e+01, -3.88498980e+01, -3.02540832e+01, -2.21263917e+01,
   -1.45861995e+01, -8.21301983e+00, -3.81934237e+00, -1.42733806e+00,
   -4.39321795e-01, -1.12593644e-01, -2.33523110e-02, -3.98877774e-03,
   -5.94049064e-04, -7.60629903e-05],
 [ -5.48574744e+01, -4.38887203e+01, -3.40117828e+01, -2.47081895e+01,
   -1.61300497e+01, -8.97579732e+00, -4.15221210e+00, -1.55202774e+00,
   -4.79014836e-01, -1.23447293e-01, -2.58142526e-02, -4.43408585e-03,
   -6.62596725e-04, -8.53525553e-05],
 [ -6.13079394e+01, -4.88705447e+01, -3.77133593e+01, -2.72351563e+01,
   -1.76258677e+01, -9.70217226e+00, -4.46733133e+00, -1.67101038e+00,
   -5.17106989e-01, -1.33924570e-01, -2.82125218e-02, -4.87262987e-03,
   -7.30186021e-04, -9.45958940e-05]]
)
logRB=numpy.array([-2.56494936,-1.87180218,-1.46633707,-1.178655  ,-0.95551145,-0.77318989,
 -0.61903921,-0.48550782,-0.36772478,-0.26236426,-0.16705408,-0.08004271,
  0.        ]
)
TqB=numpy.array([ -3.71540202e+01, -3.37237435e+01, -3.02938408e+01, -2.68647027e+01,
  -2.34371457e+01, -2.00129089e+01, -1.65957993e+01, -1.31944238e+01,
  -9.82884405e+00, -6.54603763e+00, -3.42923625e+00, -1.78177666e-17,
   3.41046868e+00,  6.62866791e+00,  9.72466066e+00,  1.27369802e+01,
   1.56893471e+01,  1.85979922e+01,  2.14745581e+01,  2.43275202e+01,
   2.71630516e+01]
)
DqB=numpy.array([ 3.3776382 , 3.37237435, 3.36598231, 3.35808784, 3.34816367, 3.33548482,
  3.31915986, 3.29860595, 3.27628135, 3.27301882, 3.42923625, 3.53262155,
  3.41046868, 3.31433395, 3.24155355, 3.18424505, 3.13786942, 3.09966537,
  3.06779402, 3.04094003, 3.01811685]
)
lnMrqB=numpy.array([[  9.24153535e+01,  9.12558462e+01,  9.06982027e+01,  9.01045064e+01,
    8.95614638e+01,  8.91325349e+01,  8.87445032e+01,  8.77462771e+01,
    8.74092431e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  8.38362086e+01,  8.26765993e+01,  8.21187910e+01,  8.15251720e+01,
    8.09819532e+01,  8.05530889e+01,  8.01647912e+01,  7.91668691e+01,
    7.88292697e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  7.52579173e+01,  7.40981058e+01,  7.35399629e+01,  7.29464960e+01,
    7.24029285e+01,  7.19741882e+01,  7.15853588e+01,  7.05880470e+01,
    7.02493098e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  6.66813698e+01,  6.55211615e+01,  6.49623334e+01,  6.43691637e+01,
    6.38249088e+01,  6.33964012e+01,  6.30065101e+01,  6.20104239e+01,
    6.16693906e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  5.81084174e+01,  5.69474475e+01,  5.63871993e+01,  5.57946020e+01,
    5.52490057e+01,  5.48209134e+01,  5.44289056e+01,  5.34352797e+01,
    5.30895933e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  4.95429708e+01,  4.83806128e+01,  4.78173696e+01,  4.72258482e+01,
    4.66776803e+01,  4.62502529e+01,  4.58540370e+01,  4.48653374e+01,
    4.45101615e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  4.09934267e+01,  3.98288984e+01,  3.92591832e+01,  3.86695865e+01,
    3.81166661e+01,  3.76900079e+01,  3.72854676e+01,  3.63065683e+01,
    3.59318247e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  3.24780002e+01,  3.13119597e+01,  3.07278911e+01,  3.01413223e+01,
    2.95803301e+01,  2.91532752e+01,  2.87324126e+01,  2.77728053e+01,
    2.73567586e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  2.40354773e+01,  2.28798242e+01,  2.22642048e+01,  2.16802800e+01,
    2.11083721e+01,  2.06738792e+01,  2.02216077e+01,  1.92998906e+01,
    1.87913772e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  1.57405605e+01,  1.46635500e+01,  1.39953128e+01,  1.34028062e+01,
    1.28246916e+01,  1.23554518e+01,  1.18454472e+01,  1.10007667e+01,
    1.02539919e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  7.70165236e+00,  6.94697599e+00,  6.34388043e+00,  5.76205138e+00,
    5.20948615e+00,  4.66343909e+00,  4.06044301e+00,  3.36729583e+00,
    1.94591015e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.11022302e-16,
    0.00000000e+00, -2.22044605e-16, -1.11022302e-16, -2.22044605e-16,
   -1.11022302e-16,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -7.37615765e+00, -6.28895678e+00, -5.22591956e+00, -4.15341196e+00,
   -2.88036113e+00, -1.50491433e+00, -5.90140000e-01, -8.40901983e-01,
   -3.00702396e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -1.44953391e+01, -1.21804868e+01, -9.89696117e+00, -7.79813614e+00,
   -5.18428880e+00, -2.48900417e+00, -9.21004981e-01, -1.60818018e+00,
   -4.51127883e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -2.14209309e+01, -1.78285339e+01, -1.42813073e+01, -1.12255538e+01,
   -7.30538543e+00, -3.37964440e+00, -1.23218444e+00, -2.37023738e+00,
   -6.01503873e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -2.81982974e+01, -2.33093748e+01, -1.85055378e+01, -1.45202845e+01,
   -9.33168527e+00, -4.24355341e+00, -1.54080262e+00, -3.12957696e+00,
   -7.51879841e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -3.48610802e+01, -2.86676066e+01, -2.26365486e+01, -1.77279034e+01,
   -1.13036528e+01, -5.09865459e+00, -1.84904512e+00, -3.88640044e+00,
   -9.02255809e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -4.14355024e+01, -3.39345833e+01, -2.67106139e+01, -2.08781565e+01,
   -1.32447703e+01, -5.95067053e+00, -2.15723126e+00, -4.64078763e+00,
   -1.05263178e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -4.79421597e+01, -3.91342321e+01, -3.07479769e+01, -2.39905024e+01,
   -1.51685612e+01, -6.80156997e+00, -2.46540892e+00, -5.39281943e+00,
   -1.20300775e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -5.43970666e+01, -4.42848059e+01, -3.47604862e+01, -2.70775092e+01,
   -1.70825960e+01, -7.65205837e+00, -2.77358529e+00, -6.14258422e+00,
   -1.35338371e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00],
 [ -6.08125286e+01, -4.93998211e+01, -3.87554694e+01, -3.01473127e+01,
   -1.89910699e+01, -8.50239415e+00, -3.08176148e+00, -6.89017691e+00,
   -1.50375968e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
    0.00000000e+00]]
)
logRC=numpy.array([-2.56494936,-1.87180218,-1.46633707,-1.178655  ,-0.95551145,-0.77318989,
 -0.61903921,-0.48550782,-0.36772478,-0.26236426,-0.16705408,-0.08004271,
  0.        ]
)
TqC=numpy.array([-37.94067526,-34.51373948,-31.08615164,-27.65373735,-24.2112209 ,
 -20.7593099 ,-17.30513978,-13.8451948 ,-10.36596011, -6.85645339,
  -3.36287973,  0.        ,  3.22546871,  6.34413721,  9.37930893,
  12.34684747, 15.25858424, 18.12413061, 20.95152098, 23.74741407,
  26.51723763]
)
DqC=numpy.array([ 3.4491523 , 3.45137395, 3.45401685, 3.45671717, 3.45874584, 3.45988498,
  3.46102796, 3.4612987 , 3.45532004, 3.42822669, 3.36287973, 3.28908942,
  3.22546871, 3.17206861, 3.12643631, 3.08671187, 3.05171685, 3.02068843,
  2.99307443, 2.96842676, 2.94635974]
)
lnMrqC=numpy.array([[ -9.59526345,-16.00669799,-21.27462241,-26.57007293,-31.65095033,
  -39.74662405,-49.96780286,-62.03555208,-73.89283818,-84.82880149,
  -92.24395774,-94.35944053,-94.37881207],
 [ -8.89210594,-14.87934896,-19.8259405 ,-24.76816719,-29.47284908,
  -36.84902184,-46.14067721,-57.10869257,-67.88448046,-77.80191751,
  -84.22666088,-85.78485973,-85.79893678],
 [ -8.18361644,-13.74097023,-18.35993769,-22.94819402,-27.28713694,
  -33.94791405,-42.3106291 ,-52.17878689,-61.87298688,-70.75029236,
  -76.17161428,-77.20869032,-77.21905721],
 [ -7.46683153,-12.58682802,-16.87099093,-21.10369836,-25.09013112,
  -31.04131392,-38.47618636,-47.24428822,-55.85631945,-63.64731244,
  -68.03495841,-68.63144555,-68.63917372],
 [ -6.73705901,-11.40975278,-15.35090056,-19.22531695,-22.87545381,
  -28.12544646,-34.63450609,-42.30218766,-49.82991658,-56.45301858,
  -59.7630215 ,-60.05347456,-60.05928667],
 [ -5.9868629 ,-10.19851258,-13.78694583,-17.29882625,-20.63116663,
  -25.1925654 ,-30.77958023,-37.34602966,-43.78156966,-49.13227674,
  -51.34853857,-51.47501324,-51.47939635],
 [ -5.20457774, -8.9347586 ,-12.15766501,-15.30076829,-18.3328005 ,
  -22.2253394 ,-26.89745033,-32.36028282,-37.67258796,-41.64999867,
  -42.84113393,-42.89622034,-42.89950305],
 [ -4.37247711, -7.587246  ,-10.42295676,-13.18694386,-15.92479573,
  -19.18022161,-22.95153884,-27.30060955,-31.38149663,-33.85199306,
  -34.29092969,-34.31720238,-34.31960702],
 [ -3.4654674 , -6.10227352, -8.50107765,-10.85823189,-13.26649701,
  -15.92545646,-18.82288595,-22.00282337,-24.59577828,-25.59318192,
  -25.72415098,-25.73803081,-25.7397085 ],
 [ -2.4525348 , -4.39609605, -6.23242667, -8.07456772, -9.98968566,
  -11.99634741,-14.00214773,-15.81197304,-16.82510106,-17.10237613,
  -17.15127748,-17.15875354,-17.1598077 ],
 [ -1.30356058, -2.37525412, -3.4131473 , -4.46377973, -5.53228128,
   -6.58228455, -7.5170858 , -8.17150672, -8.47003168, -8.55729784,
   -8.57610988, -8.57940273, -8.57990481],
 [  0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
    0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
    0.        ,  0.        ,  0.        ],
 [  1.45873472,  2.68672681,  3.85233331,  4.98895767,  6.08190193,
    7.07192905,  7.84356363,  8.30367673,  8.4997593 ,  8.56148275,
    8.57656   ,  8.57944006,  8.57990657],
 [  3.05897369,  5.61171149,  7.99341203, 10.28323079, 12.45451496,
   14.3784307 , 15.82683473, 16.66170203, 17.01304775, 17.12517023,
   17.15337929, 17.15890755, 17.15981475],
 [  4.78156431,  8.71728851, 12.33944174, 15.78610712, 19.01818974,
   21.82993709, 23.89029918, 25.05012972, 25.53435692, 25.69031851,
   25.73037539, 25.73839573, 25.73972441],
 [  6.60809592, 11.9654155 , 16.84376751, 21.44848631, 25.72480172,
   29.38533802, 32.00790076, 33.45861472, 34.06110297, 34.2565408 ,
   34.30750694, 34.31789997, 34.31963544],
 [  8.52298178, 15.32923526, 21.47461586, 27.23813614, 32.5444864 ,
   37.02116177, 40.16555412, 41.88166534, 42.59185474, 42.82359835,
   42.88474966, 42.89741704, 42.89954772],
 [ 10.51341006, 18.78758163, 26.20668481, 33.12977237, 39.45511409,
   44.72181572, 48.35458797, 50.31595363, 51.12572795, 51.39133012,
   51.46208734, 51.47694468, 51.47946116],
 [ 12.56877576, 22.32296147, 31.01903091, 39.10244313, 46.4388634 ,
   52.47580703, 56.56918789, 58.75927645, 59.66213122, 59.95962143,
   60.0395081 , 60.05648126, 60.05937567],
 [ 14.68015334, 25.92098729, 35.89476739, 45.13907277, 53.48116568,
   60.27410374, 64.80520804, 67.21008197, 68.20064512, 68.52838744,
   68.61700278, 68.63602561, 68.63929117],
 [ 16.83990326, 29.57007769, 40.82078324, 51.22621603, 60.57028267,
   68.10937021, 73.05954929, 75.66722616, 76.74095867, 77.09756344,
   77.19456398, 77.21557684, 77.21920757]]
)
fileOutput = 'random5620'
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
