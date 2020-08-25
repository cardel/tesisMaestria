#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy
numpy.set_printoptions(threshold=numpy.inf)
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


DqRandom=numpy.array([[ 3.59515143, 3.58758035, 3.58000898, 3.57243355, 3.56483422, 3.55718533,
   3.5494658 , 3.5416669 , 3.53379619, 3.52587665, 3.51794158, 3.5100273 ,
   3.5021662 , 3.49438189, 3.48668709, 3.47908379, 3.47156518, 3.46411867,
   3.45672952, 3.449385  , 3.44207838],
 [ 3.63728945, 3.62089285, 3.60450542, 3.58860975, 3.57355909, 3.55949764,
   3.5463871 , 3.53409324, 3.52246413, 3.51137137, 3.50072044, 3.49044535,
   3.48049891, 3.47084476, 3.46145313, 3.45230012, 3.44336905, 3.43465215,
   3.42615122, 3.41787667, 3.40984469],
 [ 3.66202095, 3.6426793 , 3.6210905 , 3.59794957, 3.5743843 , 3.55162462,
   3.53051319, 3.51135238, 3.49412938, 3.4786636 , 3.46466276, 3.45181878,
   3.43987643, 3.42864869, 3.41800716, 3.40786787, 3.39817905, 3.38891138,
   3.38004984, 3.37158701, 3.36351796],
 [ 3.5800889 , 3.56078521, 3.53838453, 3.51250578, 3.48306462, 3.45073634,
   3.41730305, 3.38516082, 3.35618723, 3.33102315, 3.30920615, 3.28990766,
   3.27244833, 3.25639076, 3.24147581, 3.22755147, 3.21452431, 3.20233056,
   3.19091994, 3.18024715, 3.17026816],
 [ 3.45439066, 3.43799126, 3.41828939, 3.39496911, 3.36797812, 3.33754685,
   3.30394407, 3.26826805, 3.23216495, 3.19743315, 3.16664033, 3.139933  ,
   3.11642474, 3.0954026 , 3.0764097 , 3.05913835, 3.0433595 , 3.02889062,
   3.01558194, 3.00330916, 2.99196814],
 [ 3.1976543 , 3.18965514, 3.18014548, 3.16856357, 3.15396761, 3.13527628,
   3.1120046 , 3.0839459 , 3.04926807, 3.0064713 , 2.96086005, 2.92062545,
   2.88667632, 2.8574999 , 2.83194344, 2.80928568, 2.78904595, 2.77087226,
   2.7544874 , 2.73966314, 2.72620685],
 [ 2.34458203, 2.35604985, 2.37006186, 2.38723018, 2.40843756, 2.43553595,
   2.4722    , 2.52417326, 2.60009561, 2.69804759, 2.74746772, 2.72472831,
   2.69058468, 2.65929138, 2.63172364, 2.60734958, 2.58562319, 2.56611889,
   2.5485137 , 2.53255785, 2.5180522 ],
 [ 2.25133006, 2.2536233 , 2.25613202, 2.25897493, 2.26237695, 2.26675252,
   2.27297217, 2.28280004, 2.29903061, 2.32004535, 2.31729339, 2.27857335,
   2.23474654, 2.19586151, 2.16225003, 2.13301926, 2.10735652, 2.08465617,
   2.06447493, 2.0464746 , 2.0303812 ],
 [ 1.5920628 , 1.58531218, 1.57724256, 1.56752502, 1.55574407, 1.54139106,
   1.52388867, 1.50269376, 1.47754546, 1.44886409, 1.41805872, 1.38726308,
   1.35845111, 1.33271137, 1.3102377 , 1.29072572, 1.27372099, 1.2587917 ,
   1.24558216, 1.23381414, 1.22327243],
 [ 0.98357739, 0.97873242, 0.97282973, 0.96555368, 0.9564813 , 0.94505667,
   0.93058192, 0.91226814, 0.88943799, 0.86196062, 0.83071882, 0.79755933,
   0.76462597, 0.73370529, 0.70594043, 0.68181027, 0.66127634, 0.64399599,
   0.62950496, 0.6173327 , 0.60705803]]
)
GCRandom=numpy.array([ 1.    , 0.9   , 0.8   , 0.7   , 0.6   , 0.4998, 0.396 , 0.2762, 0.0916,
  0.0044]
)
APLRandom=numpy.array([ 1.        , 1.04460568, 1.07963951, 1.18568494, 1.26970132, 1.46419647,
  1.82397297, 2.6243821 , 6.4636686 , 0.74097075]

)
DqDegree=numpy.array([[ 3.71713961, 3.71355869, 3.71013326, 3.70678494, 3.7034038 , 3.69987482,
   3.69610626, 3.69204813, 3.68769541, 3.68307873, 3.67824928, 3.673264  ,
   3.6681747 , 3.66302184, 3.65783234, 3.65262019, 3.64738863, 3.64213327,
   3.63684577, 3.63151787, 3.62614547],
 [ 3.45647623, 3.44696633, 3.43725141, 3.42736267, 3.41730915, 3.4071094 ,
   3.39682164, 3.38654384, 3.37638693, 3.36644856, 3.35680269, 3.34750073,
   3.33857561, 3.33004534, 3.3219159 , 3.31418403, 3.30683992, 3.29986962,
   3.29325706, 3.28698542, 3.28103813],
 [ 3.36629168, 3.35076376, 3.33475305, 3.31885124, 3.30360081, 3.28928075,
   3.27585267, 3.26311971, 3.25092117, 3.23920219, 3.22797551, 3.21726661,
   3.20708762, 3.19743491, 3.18829458, 3.17964772, 3.1714736 , 3.16375139,
   3.15646086, 3.14958264, 3.14309816],
 [ 3.15735373, 3.15125301, 3.14517935, 3.13941561, 3.13416431, 3.12941516,
   3.1246663 , 3.11892729, 3.11168451, 3.10335829, 3.09458703, 3.0857834 ,
   3.07716445, 3.0688477 , 3.06090075, 3.05336064, 3.04624235, 3.03954434,
   3.03325339, 3.0273489 , 3.02180635],
 [ 2.83705447, 2.83488305, 2.83235907, 2.82996099, 2.82891861, 2.83111592,
   2.83856089, 2.85169222, 2.86428825, 2.86666121, 2.8600922 , 2.85027202,
   2.83973533, 2.82929322, 2.81923511, 2.8096794 , 2.80067538, 2.79223878,
   2.78436624, 2.77704197, 2.7702416 ],
 [ 1.99066745, 2.00348117, 2.01967367, 2.04057812, 2.0681453 , 2.10516085,
   2.15543873, 2.22371119, 2.31066608, 2.39169668, 2.42190312, 2.41582003,
   2.40038853, 2.38384804, 2.36811182, 2.35359814, 2.34033944, 2.32825919,
   2.31725185, 2.30720871, 2.29802716],
 [ 1.26884478, 1.26677895, 1.26411987, 1.26067551, 1.25617814, 1.25025662,
   1.24241684, 1.23206962, 1.21867751, 1.20206913, 1.18280606, 1.16225093,
   1.14206476, 1.12347905, 1.10700103, 1.09261386, 1.08007841, 1.06911576,
   1.05947684, 1.05095689, 1.043391  ],
 [ 0.62867495, 0.62676178, 0.62438315, 0.62144987, 0.61787318, 0.61357935,
   0.60853241, 0.60276298, 0.59639453, 0.58965129, 0.58283285, 0.57625643,
   0.57019128, 0.56481629, 0.56021277, 0.55638184, 0.55326996, 0.55079298,
   0.548855  , 0.54736132, 0.54622606],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan],
 [        nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan,        nan,        nan,        nan,
          nan,        nan,        nan]]
)
GCDegree=numpy.array([  1.00000000e+00,  9.00000000e-01,  8.00000000e-01,  7.00000000e-01,
   5.99400000e-01,  4.84200000e-01,  2.96000000e-02,  1.40000000e-03,
   2.00000000e-04,  2.00000000e-04]
)
APLDegree=numpy.array([ 1.        , 1.08950609, 1.25948533, 1.5164151 , 1.97769533, 3.6098253 ,
  4.4009439 , 0.24479763, 0.18355279, 0.18355279]

)
DqCentrality=numpy.array([[ 3.59550275, 3.58773063, 3.58001286, 3.57234092, 3.56468551, 3.55701031,
   3.54928515, 3.54149488, 3.53364282, 3.52574912, 3.51784494, 3.50996487,
   3.50213973, 3.4943917 , 3.48673207, 3.47916139, 3.47167129, 3.46424745,
   3.45687342, 3.44953494, 3.44222439],
 [ 3.66599566, 3.64109641, 3.61197237, 3.57782059, 3.53770176, 3.49150183,
   3.44365213, 3.40380269, 3.37542167, 3.35562969, 3.34061459, 3.32795233,
   3.3166872 , 3.30641143, 3.29691023, 3.28804906, 3.27973378, 3.2718943 ,
   3.26447661, 3.25743842, 3.25074622],
 [ 3.59734039, 3.5719279 , 3.54039903, 3.50135512, 3.45373594, 3.39806076,
   3.33885376, 3.28522369, 3.24434099, 3.21549553, 3.19433245, 3.17754539,
   3.1633589 , 3.1508759 , 3.1396234 , 3.12933183, 3.11983386, 3.11101663,
   3.10279817, 3.09511506, 3.08791568],
 [ 3.27748069, 3.26417823, 3.24781529, 3.22758047, 3.20228151, 3.17039198,
   3.13087133, 3.08660303, 3.04527446, 3.00974206, 2.98006975, 2.9567565 ,
   2.93766199, 2.9212843 , 2.9068151 , 2.89379232, 2.88192663, 2.87102201,
   2.86093731, 2.85156627, 2.84282637],
 [ 2.87007466, 2.86741302, 2.86363234, 2.85825979, 2.8511517 , 2.84284707,
   2.83453441, 2.82866016, 2.82664945, 2.81716477, 2.79422389, 2.7701288 ,
   2.7493315 , 2.73152562, 2.71595656, 2.70206405, 2.68946959, 2.67791575,
   2.66722372, 2.65726703, 2.64795494],
 [ 2.5675891 , 2.56511389, 2.5618992 , 2.55767373, 2.55220067, 2.54538259,
   2.53740163, 2.5289114 , 2.51945199, 2.50235854, 2.47240949, 2.43986215,
   2.41140565, 2.3871625 , 2.36601649, 2.34706708, 2.32972345, 2.31361726,
   2.29852937, 2.28434005, 2.2709927 ],
 [ 2.13128437, 2.12804628, 2.12389273, 2.11859925, 2.11190966, 2.10354222,
   2.09314517, 2.08005906, 2.0627966 , 2.03908946, 2.00840956, 1.97450151,
   1.94211384, 1.91337953, 1.88838956, 1.8665709 , 1.84731122, 1.83012169,
   1.81464516, 1.80062647, 1.78787965],
 [ 1.63431522, 1.63062099, 1.6254681 , 1.61826026, 1.60817263, 1.59413382,
   1.57492126, 1.54950895, 1.51780105, 1.48154953, 1.44441196, 1.41017234,
   1.38074295, 1.35613201, 1.33553397, 1.3180826 , 1.30308788, 1.29004292,
   1.27857777, 1.26841686, 1.25934948],
 [ 1.20335455, 1.19738483, 1.19008333, 1.18110316, 1.17002317, 1.15635686,
   1.13959593, 1.1193218 , 1.09541249, 1.0683067 , 1.03915999, 1.00967962,
   0.98161222, 0.95618071, 0.93386736, 0.91459382, 0.89801832, 0.88373916,
   0.87138362, 0.86063326, 0.85122458],
 [ 0.72416371, 0.72135298, 0.71807418, 0.71423553, 0.70973214, 0.7044492 ,
   0.69826999, 0.69109195, 0.68285437, 0.67357904, 0.66341671, 0.65267517,
   0.64179248, 0.63124065, 0.62140453, 0.61250801, 0.60461577, 0.5976819 ,
   0.59160484, 0.58626726, 0.58155782]]
)
GCCentrality=numpy.array([ 1.    , 0.9   , 0.8   , 0.7   , 0.599 , 0.492 , 0.3662, 0.1   , 0.0162,
  0.0032]

)
APLCentrality=numpy.array([ 1.        , 1.08030181, 1.24638559, 1.46026511, 1.83008139, 2.55384114,
  4.58256549, 5.51986661, 1.79223218, 0.47088167]

)
DqGenetic=numpy.array([[ 3.59366457, 3.58642178, 3.57913094, 3.57178643, 3.56437056, 3.55686282,
   3.54924913, 3.54152847, 3.53371553, 3.5258391 , 3.5179367 , 3.51004764,
   3.50220655, 3.49443908, 3.48676014, 3.47917439, 3.47167826, 3.46426287,
   3.45691756, 3.44963359, 3.44240757],
 [ 3.63331287, 3.61691457, 3.60063788, 3.58503561, 3.57046   , 3.55705641,
   3.54476599, 3.53316967, 3.52194393, 3.51104987, 3.50048074, 3.49021956,
   3.48025543, 3.47058052, 3.46118323, 3.45204476, 3.44313899, 3.43443415,
   3.42589595, 3.41749197, 3.40919703],
 [ 3.518162  , 3.5015383 , 3.48339993, 3.46411539, 3.44417012, 3.42400858,
   3.40393034, 3.38419813, 3.36513864, 3.34702482, 3.32997203, 3.31397395,
   3.29897025, 3.28488486, 3.27164088, 3.25916551, 3.24739109, 3.23625502,
   3.22569943, 3.21567141, 3.20612364],
 [ 3.51753773, 3.50208289, 3.48474798, 3.46547167, 3.4443187 , 3.42160392,
   3.39799401, 3.37433507, 3.3513478 , 3.32953254, 3.3091444 , 3.29021754,
   3.2726688 , 3.25638034, 3.2412337 , 3.22711926, 3.21393846, 3.20160476,
   3.19004378, 3.17919269, 3.16899863],
 [ 3.38867725, 3.37719485, 3.36232354, 3.3434151 , 3.32038577, 3.29409635,
   3.26636055, 3.23925951, 3.21557094, 3.19272336, 3.16564484, 3.13897488,
   3.11481558, 3.09301999, 3.07321621, 3.05510586, 3.03846158, 3.0231078 ,
   3.00890726, 2.99575096, 2.98354967],
 [ 2.84563215, 2.8432586 , 2.83991464, 2.8352493 , 2.82949821, 2.82413929,
   2.82209933, 2.82650696, 2.84312554, 2.87103403, 2.85970862, 2.82002395,
   2.78405868, 2.7532242 , 2.72624325, 2.7021872 , 2.68044042, 2.66058938,
   2.64235344, 2.62554039, 2.61001481],
 [ 2.73963342, 2.74330071, 2.74748319, 2.75232272, 2.7579057 , 2.7645002 ,
   2.77319331, 2.78574353, 2.8019544 , 2.81288703, 2.80104364, 2.77164708,
   2.73979845, 2.71029019, 2.68342415, 2.65873495, 2.63582088, 2.61446443,
   2.59459187, 2.57619744, 2.55927898],
 [ 2.40703469, 2.41156969, 2.41665171, 2.42244827, 2.42916297, 2.43708817,
   2.44669644, 2.45838009, 2.4709039 , 2.47596202, 2.45777766, 2.41887247,
   2.37565685, 2.33545293, 2.29932973, 2.26675335, 2.23705437, 2.20979939,
   2.18481446, 2.16206662, 2.14153383],
 [ 1.5461482 , 1.5546761 , 1.5650248 , 1.57774937, 1.59356651, 1.61333857,
   1.63795961, 1.66798031, 1.7023774 , 1.73532633, 1.75408898, 1.74991717,
   1.72866196, 1.70065015, 1.67205814, 1.64524094, 1.62080312, 1.59877978,
   1.57906225, 1.56149902, 1.54591127],
 [ 1.03316523, 1.03403452, 1.03477018, 1.03528989, 1.03547466, 1.0351429 ,
   1.03399937, 1.03155096, 1.02701541, 1.01933032, 1.00743818, 0.99090984,
   0.97053363, 0.94818468, 0.92599493, 0.90558922, 0.88779638, 0.872771  ,
   0.86027975, 0.84994465, 0.84138004]]
)
GCGenetic=numpy.array([ 1.    , 0.9   , 0.8   , 0.7   , 0.5998, 0.4984, 0.3936, 0.2774, 0.122 ,
  0.0036]
)
APLGenetic=numpy.array([ 1.        , 1.04393748, 1.07719341, 1.17030032, 1.2646773 , 1.44487387,
  1.77056388, 2.42643916, 4.84322254, 0.58309089]

)
DqSimulated=numpy.array([[ 3.71641093, 3.71302256, 3.70975839, 3.7065384 , 3.70325327, 3.6997905 ,
   3.69606236, 3.69202404, 3.68767631, 3.68305561, 3.67821818, 3.67322488,
   3.66813006, 3.66297544, 3.6577882 , 3.65258195, 3.64735941, 3.64211573,
   3.6368424 , 3.63153133, 3.62617875],
 [ 3.60856515, 3.5980228 , 3.58720683, 3.57618234, 3.56502711, 3.55383387,
   3.54269383, 3.53167875, 3.52084278, 3.51023225, 3.49988738, 3.48983884,
   3.48010604, 3.47069796, 3.46161484, 3.45284987, 3.44439093, 3.43622258,
   3.42832841, 3.42069346, 3.41330616],
 [ 3.52634168, 3.50844118, 3.48891912, 3.46829914, 3.44727682, 3.42645669,
   3.40616949, 3.38657524, 3.3678473 , 3.3501652 , 3.33361552, 3.31817076,
   3.30373631, 3.29019805, 3.2774465 , 3.26538374, 3.25392345, 3.24299022,
   3.23252019, 3.2224628 , 3.21278254],
 [ 3.53369995, 3.51546568, 3.49455121, 3.47105893, 3.44558566, 3.4193554 ,
   3.39383561, 3.36992187, 3.34768523, 3.32705512, 3.30803528, 3.29051892,
   3.27432441, 3.25927604, 3.24523039, 3.23207521, 3.21972253, 3.20810232,
   3.19715761, 3.186841  , 3.17711239],
 [ 3.30458538, 3.29238799, 3.2767008 , 3.25701484, 3.23321184, 3.20578859,
   3.17596811, 3.14605512, 3.12447373, 3.10806558, 3.07835493, 3.04828401,
   3.02215281, 2.9991972 , 2.97866511, 2.96007935, 2.94313496, 2.92762158,
   2.91337883, 2.9002733 , 2.88818826],
 [ 3.00543401, 3.0041299 , 3.00213492, 2.99940731, 2.99631506, 2.99377947,
   2.99293594, 2.99456065, 2.99749309, 2.98981795, 2.96318518, 2.93079943,
   2.90060098, 2.8736496 , 2.84955959, 2.82784391, 2.8081093 , 2.79006034,
   2.77347688, 2.75819172, 2.74407346],
 [ 2.65780786, 2.65952075, 2.66135136, 2.66334236, 2.66545746, 2.66773091,
   2.67038916, 2.67338578, 2.67510581, 2.66716082, 2.63702092, 2.59361264,
   2.55227893, 2.51664619, 2.48596069, 2.45912443, 2.4353459 , 2.41410238,
   2.39503701, 2.37788534, 2.36243326],
 [ 1.82022928, 1.83241766, 1.8473453 , 1.86590929, 1.88933204, 1.91925196,
   1.95785921, 2.00776665, 2.06987287, 2.13394651, 2.16962167, 2.16314844,
   2.13484451, 2.10212321, 2.07138883, 2.04414393, 2.02036479, 1.99963673,
   1.98149989, 1.9655464 , 1.9514383 ],
 [ 1.36452395, 1.36734274, 1.37023327, 1.37304031, 1.37550695, 1.37724788,
   1.37773452, 1.37630697, 1.37224444, 1.36495566, 1.35431884, 1.34096738,
   1.32611712, 1.31097821, 1.29634052, 1.28257787, 1.26982622, 1.25811966,
   1.24744973, 1.23778327, 1.22906807],
 [ 0.85664705, 0.85254018, 0.84768838, 0.8419604 , 0.83522569, 0.82737372,
   0.81834229, 0.80815155, 0.79693563, 0.78495939, 0.77260442, 0.76031379,
   0.74850934, 0.73752017, 0.72754722, 0.71866126, 0.71082767, 0.7039487 ,
   0.69790467, 0.69258015, 0.68787467]]
)
GCSimulated=numpy.array([ 1.    , 0.9   , 0.8   , 0.7   , 0.6   , 0.498 , 0.392 , 0.243 , 0.0222,
  0.0022]
)
APLSimulated=numpy.array([ 1.        , 1.04489056, 1.0830393 , 1.1983598 , 1.32867904, 1.58256717,
  2.13459784, 3.630752  , 2.7851488 , 0.36069895]
)
fileOutput = '20SmallWorld5000Rewire02'
timestr = 'grafica'
font = {'weight': 'normal', 'size': 8}
fig3 = plt.figure()
ax = fig3.add_subplot(111)
RRandom = numpy.nansum(DqRandom,axis=0)/10
RDegree = numpy.nansum(DqDegree,axis=0)/10
RCentrality = numpy.nansum(DqCentrality,axis=0)/10
plt.plot(range(0,maxq),RRandom[IndexZero:-1],'r-' , label = u'R random')
plt.plot(range(0,maxq),RDegree[IndexZero:-1],'g-' , label = u'R degree')
plt.plot(range(0,maxq),RCentrality[IndexZero:-1],'b-' , label = u'R centrality')
fontP = FontProperties()
fontP.set_size('small')
plt.xlabel('q', fontdict=font)
plt.ylabel(r'R index', fontdict=font)
plt.title(u'R index MFA', fontdict=font)
lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
plt.grid(True)
plt.savefig('multirobus'+fileOutput+'.png', bbox_extra_artists=(lgd,),bbox_inches='tight')
data=numpy.array([RRandom, RDegree, RCentrality])
numpy.save('Rindex'+fileOutput+'.npy',data)
