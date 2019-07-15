import numpy as np
import filecmp
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, execute
backend = BasicAer.get_backend('dm_simulator')
#backend = BasicAer.get_backend('qasm_simulator')
options = {}
q = QuantumRegister(7)
c = ClassicalRegister(7)
qc = QuantumCircuit(q, c)
qc.u1(0.08114,q[1])
qc.cx(q[3],q[1])
qc.u1(0.1186,q[6])
qc.cx(q[6],q[4])
qc.u3(2.95981,6.0648,5.4253,q[1])
qc.u2(0.9981,0.07139,q[6])
qc.ccx(q[6],q[0],q[3])
qc.cx(q[2],q[6])
qc.u2(5.6449,2.4285,q[1])
qc.u1(1.09558,q[1])
qc.u3(3.02689,4.25453,6.26662,q[1])
qc.u1(4.42702,q[1])
qc.u2(4.69304,2.67086,q[6])
qc.ccx(q[5],q[4],q[0])
qc.ccx(q[2],q[3],q[6])
qc.u3(2.36137,1.1563,1.73508,q[4])
qc.u3(0.42972,4.26421,4.91091,q[0])
qc.ccx(q[2],q[1],q[5])
qc.ccx(q[6],q[1],q[2])
qc.cx(q[5],q[2])
qc.ccx(q[6],q[1],q[2])
qc.u3(2.29378,1.66182,4.94305,q[2])
qc.cx(q[2],q[3])
qc.u2(1.88824,5.7268,q[2])
qc.cx(q[4],q[6])
qc.u1(1.28328,q[6])
qc.u3(0.11366,1.19481,6.14513,q[2])
qc.u2(4.4075,1.85869,q[1])
qc.u1(3.37741,q[6])
qc.ccx(q[5],q[4],q[0])
qc.cx(q[1],q[4])
qc.u3(1.44049,0.57459,3.22416,q[6])
qc.ccx(q[3],q[6],q[2])
qc.cx(q[3],q[2])
qc.u1(4.65016,q[6])
qc.u2(3.6539,0.40275,q[3])
qc.cx(q[6],q[5])
qc.u1(0.06398,q[5])
qc.cx(q[4],q[3])
qc.ccx(q[2],q[3],q[6])
qc.u2(1.6099,4.32692,q[0])
qc.u1(3.24003,q[4])
qc.ccx(q[0],q[3],q[5])
qc.u2(2.77578,2.69482,q[6])
qc.u1(3.3346,q[6])
qc.ccx(q[1],q[2],q[6])
qc.cx(q[4],q[2])
qc.cx(q[1],q[4])
qc.u1(2.21624,q[5])
qc.u2(5.55377,3.53102,q[1])
qc.u1(6.05466,q[2])
qc.u3(1.93589,0.87644,5.13135,q[6])
qc.cx(q[6],q[5])
qc.ccx(q[6],q[2],q[1])
qc.u2(1.87312,3.43638,q[0])
qc.u3(0.96982,3.2477,0.76005,q[2])
qc.u3(2.51794,6.22101,2.70655,q[4])
qc.u1(3.76938,q[1])
qc.u3(2.48444,4.1199,5.96344,q[5])
qc.ccx(q[3],q[1],q[2])
qc.ccx(q[1],q[2],q[4])
qc.ccx(q[4],q[1],q[5])
qc.ccx(q[0],q[6],q[5])
qc.u1(0.87237,q[2])
qc.cx(q[0],q[6])
qc.cx(q[0],q[2])
qc.cx(q[3],q[2])
qc.ccx(q[6],q[1],q[3])
qc.u2(1.69687,4.11963,q[5])
qc.u3(2.89231,1.42338,2.77185,q[0])
qc.cx(q[1],q[6])
qc.cx(q[6],q[2])
qc.cx(q[6],q[0])
qc.cx(q[5],q[1])
qc.cx(q[2],q[1])
qc.u1(3.98061,q[4])
qc.ccx(q[0],q[5],q[1])
qc.cx(q[5],q[0])
qc.u1(0.59746,q[0])
qc.u3(2.22807,1.7521,4.33328,q[2])
qc.u2(0.90437,3.20216,q[6])
qc.cx(q[6],q[2])
qc.cx(q[2],q[3])
qc.u3(2.38168,2.5919,5.06642,q[2])
qc.u1(2.53859,q[0])
qc.u1(0.24169,q[1])
qc.u3(2.22853,4.75496,1.00531,q[2])
qc.u2(3.32249,1.42907,q[6])
qc.ccx(q[5],q[3],q[1])
qc.cx(q[4],q[1])
qc.u1(2.91329,q[6])
qc.u1(4.17229,q[0])
qc.u1(3.31186,q[0])
qc.cx(q[1],q[0])
qc.ccx(q[0],q[5],q[6])
qc.cx(q[2],q[5])
qc.ccx(q[0],q[1],q[5])
qc.u2(4.14797,1.38104,q[4])
qc.u3(2.12736,0.27596,0.69593,q[1])
qc.cx(q[1],q[3])
qc.cx(q[5],q[0])
qc.cx(q[4],q[6])
qc.u2(0.09354,3.97906,q[3])
qc.u3(0.32635,5.53094,1.00755,q[0])
qc.u2(2.46459,4.90918,q[2])
qc.u1(6.19628,q[6])
qc.cx(q[6],q[2])
qc.u2(5.76285,0.61732,q[2])
qc.u1(0.47862,q[2])
qc.u1(0.77816,q[0])
qc.ccx(q[5],q[6],q[2])
qc.ccx(q[6],q[1],q[4])
qc.u1(3.69236,q[6])
qc.cx(q[5],q[3])
qc.u1(1.21982,q[2])
qc.ccx(q[0],q[5],q[2])
qc.u2(2.62568,2.89943,q[0])
qc.cx(q[5],q[6])
qc.u1(5.05429,q[3])
qc.ccx(q[2],q[0],q[6])
qc.u2(3.94369,5.86585,q[0])
qc.u3(0.59252,4.80236,5.07321,q[5])
qc.u3(2.25605,2.46765,2.11621,q[1])
qc.u2(5.58504,4.67379,q[5])
qc.ccx(q[0],q[3],q[1])
qc.cx(q[2],q[1])
qc.u3(1.86851,0.71929,0.97843,q[4])
qc.u1(4.23607,q[4])
qc.u3(2.16959,0.35964,0.56578,q[3])
qc.u1(5.93075,q[4])
qc.u3(0.86039,3.88269,4.43536,q[3])
qc.u2(5.18633,0.68683,q[6])
qc.u2(5.55672,2.21722,q[0])
qc.cx(q[6],q[5])
qc.ccx(q[5],q[2],q[3])
qc.u2(1.35985,5.14171,q[1])
qc.u2(2.69445,5.53706,q[2])
qc.u1(0.66426,q[1])
qc.cx(q[0],q[1])
qc.ccx(q[3],q[5],q[2])
qc.u2(3.57443,0.45137,q[6])
qc.u2(3.64725,3.03678,q[6])
qc.cx(q[3],q[5])
qc.cx(q[2],q[3])
qc.u2(1.56375,6.00566,q[2])
qc.u2(2.39537,5.29865,q[4])
qc.ccx(q[2],q[5],q[3])
qc.ccx(q[0],q[6],q[1])
qc.u1(0.38842,q[3])
qc.u3(2.59595,4.77315,2.71481,q[5])
qc.u1(2.09187,q[4])
qc.ccx(q[2],q[0],q[6])
qc.u1(2.25653,q[6])
qc.ccx(q[0],q[1],q[3])
qc.u3(2.55028,3.38093,2.76843,q[1])
qc.u2(4.9524,0.87725,q[2])
qc.u2(5.01355,0.10528,q[6])
qc.u1(2.22315,q[3])
qc.ccx(q[1],q[4],q[0])
qc.u2(3.38503,2.75052,q[0])
qc.cx(q[1],q[4])
qc.u2(3.46048,1.10886,q[1])
qc.u2(0.88987,3.21719,q[2])
qc.ccx(q[0],q[2],q[5])
qc.cx(q[4],q[2])
qc.cx(q[0],q[4])
qc.u3(1.16226,0.20637,4.708,q[3])
qc.cx(q[4],q[5])
qc.u1(2.66704,q[2])
qc.cx(q[2],q[3])
qc.cx(q[5],q[3])
qc.u2(6.01449,3.53035,q[1])
qc.u3(1.17363,3.27027,0.36328,q[1])
qc.u1(4.01972,q[3])
qc.u1(0.5922,q[1])
qc.u2(4.30066,3.27488,q[1])
qc.cx(q[0],q[2])
qc.cx(q[1],q[6])
qc.ccx(q[1],q[3],q[4])
qc.ccx(q[6],q[3],q[4])
qc.ccx(q[2],q[1],q[4])
qc.u3(0.67075,6.14059,5.32363,q[3])
qc.cx(q[3],q[5])
qc.u2(1.01975,1.79681,q[5])
qc.cx(q[4],q[0])
qc.cx(q[0],q[6])
qc.cx(q[0],q[1])
qc.u2(4.84553,0.35278,q[0])
qc.u2(4.34825,4.23275,q[1])
qc.ccx(q[0],q[6],q[3])
qc.ccx(q[0],q[1],q[3])
qc.ccx(q[1],q[2],q[4])
qc.cx(q[2],q[0])
qc.cx(q[3],q[6])
qc.cx(q[6],q[5])
qc.ccx(q[1],q[2],q[4])
qc.cx(q[0],q[2])
qc.u3(2.1921,2.97145,5.3063,q[4])
qc.u1(1.97846,q[3])
qc.u3(2.71162,5.00413,5.76876,q[3])
qc.u3(0.86089,6.25644,4.22898,q[3])
qc.ccx(q[4],q[5],q[3])
qc.cx(q[0],q[4])
qc.u3(0.63269,2.09789,3.37504,q[3])
qc.u2(4.89656,0.29657,q[6])
qc.cx(q[0],q[3])
qc.u2(5.47457,0.33805,q[5])
qc.u1(3.18437,q[6])
qc.ccx(q[6],q[5],q[3])
qc.cx(q[4],q[6])
qc.u2(0.555,0.01039,q[6])
qc.cx(q[5],q[6])
qc.ccx(q[6],q[4],q[1])
qc.cx(q[0],q[6])
qc.cx(q[5],q[1])
qc.u1(2.18019,q[6])
qc.u2(1.70689,0.16303,q[6])
qc.u2(4.60711,4.7709,q[0])
qc.cx(q[4],q[3])
qc.u1(0.60315,q[6])
qc.u3(1.79008,4.37681,2.31877,q[1])
qc.cx(q[4],q[6])
qc.u2(0.99092,3.38465,q[3])
qc.cx(q[3],q[6])
qc.cx(q[3],q[1])
qc.u2(2.83364,0.22069,q[5])
qc.u1(5.675,q[4])
qc.ccx(q[1],q[4],q[3])
qc.cx(q[3],q[1])
qc.ccx(q[0],q[5],q[1])
qc.u2(2.4727,5.37412,q[1])
qc.u3(1.0056,2.05572,0.58851,q[4])
qc.ccx(q[6],q[5],q[1])
qc.cx(q[6],q[3])
qc.cx(q[0],q[6])
qc.u3(1.18413,6.05859,0.34418,q[4])
qc.u1(3.41992,q[1])
qc.u3(1.16095,1.68371,3.73734,q[3])
qc.u1(0.84837,q[6])
qc.u1(5.44305,q[5])
qc.u2(1.5253,3.34471,q[3])
qc.ccx(q[6],q[3],q[0])
qc.u2(3.50865,1.31805,q[4])
qc.cx(q[4],q[1])
qc.cx(q[5],q[3])
qc.cx(q[6],q[2])
qc.cx(q[0],q[1])
qc.u2(0.16788,4.71874,q[2])
qc.ccx(q[4],q[5],q[1])
qc.u3(0.0295,0.69116,0.50113,q[1])
qc.u3(1.82074,4.47561,4.30395,q[0])
qc.u2(3.21231,2.81048,q[6])
qc.u3(2.51692,2.50497,5.00914,q[3])
qc.u3(3.12799,3.61707,3.96091,q[3])
qc.u2(0.12001,3.6595,q[1])
qc.ccx(q[1],q[2],q[6])
qc.u1(3.87952,q[5])
qc.ccx(q[0],q[3],q[6])
qc.ccx(q[3],q[2],q[0])
qc.u2(5.92228,4.8336,q[6])
qc.u1(2.86023,q[2])
qc.u3(0.406,4.91436,3.23734,q[4])
qc.u1(1.34901,q[5])
qc.cx(q[4],q[1])
qc.u1(4.13704,q[2])
qc.u3(2.69741,6.2272,3.75657,q[0])
qc.u1(5.71003,q[4])
qc.u1(2.39466,q[4])
qc.u3(2.63546,4.02353,2.16717,q[5])
qc.u3(2.04241,1.05653,6.14126,q[2])
qc.ccx(q[4],q[6],q[1])
qc.u1(5.5243,q[3])
qc.u3(1.65219,3.50841,2.81803,q[0])
qc.cx(q[6],q[1])
qc.u2(1.33849,2.13292,q[6])
qc.ccx(q[0],q[3],q[6])
qc.cx(q[6],q[0])
qc.u3(2.24413,5.89821,4.84872,q[0])
qc.u2(3.38392,5.17205,q[3])
qc.u3(1.5574,2.20352,1.79723,q[1])
qc.cx(q[4],q[1])
qc.u3(0.28016,0.30523,5.81999,q[4])
qc.cx(q[2],q[6])
qc.u1(0.86869,q[5])
qc.u3(1.93659,5.78022,1.76054,q[1])
qc.cx(q[6],q[4])
qc.cx(q[2],q[5])
qc.u1(1.29492,q[0])
qc.u3(1.188,1.12663,1.54622,q[5])
qc.u1(3.50522,q[5])
qc.cx(q[6],q[1])
qc.ccx(q[2],q[6],q[1])
qc.u1(0.72395,q[5])
qc.u1(3.80759,q[3])
qc.u3(0.68953,3.36531,2.05344,q[4])
qc.u3(2.77782,5.73462,4.48238,q[5])
qc.cx(q[3],q[6])
qc.u2(1.996,0.83687,q[3])
qc.u2(3.07204,4.5158,q[4])
qc.cx(q[3],q[4])
qc.u1(4.54603,q[3])
qc.cx(q[2],q[0])
qc.u2(3.06255,5.68054,q[0])
qc.u3(0.93959,1.20464,3.4914,q[0])
qc.u1(4.79798,q[3])
qc.u2(1.14557,3.40938,q[4])
qc.u2(0.24988,0.47986,q[6])
qc.u2(5.93603,1.2794,q[5])
qc.u1(0.13454,q[0])
qc.u2(1.03888,1.39259,q[3])
qc.ccx(q[0],q[1],q[4])
qc.u3(1.37527,5.76636,6.28154,q[2])
qc.cx(q[1],q[3])
qc.u1(4.84353,q[3])
qc.u2(2.20721,0.8205,q[5])
qc.ccx(q[5],q[2],q[6])
qc.u1(4.17501,q[4])
qc.u1(3.49335,q[6])
qc.u3(2.44598,4.29584,5.5993,q[1])
qc.u3(1.77731,2.56375,5.05391,q[2])
qc.ccx(q[4],q[6],q[1])
qc.cx(q[0],q[6])
qc.cx(q[4],q[0])
qc.u3(0.21006,1.62636,2.10549,q[3])
qc.ccx(q[4],q[2],q[1])
qc.u1(3.28297,q[4])
qc.cx(q[2],q[6])
qc.u3(0.37029,1.33394,0.09025,q[3])
qc.u2(3.32218,0.15953,q[0])
qc.u1(2.68027,q[3])
qc.u3(2.24485,0.76989,5.52657,q[5])
qc.u2(1.69339,5.4546,q[6])
qc.ccx(q[4],q[6],q[2])
qc.u3(1.40834,0.73433,1.69139,q[6])
qc.u2(3.33684,1.27355,q[6])
qc.cx(q[1],q[5])
qc.cx(q[0],q[1])
qc.u2(3.7166,4.08421,q[6])
qc.u2(5.52943,4.5582,q[5])
qc.cx(q[3],q[5])
qc.u1(6.14029,q[3])
qc.cx(q[5],q[0])
qc.cx(q[6],q[4])
qc.ccx(q[4],q[1],q[6])
qc.cx(q[1],q[3])
qc.u2(4.9093,3.14252,q[6])
qc.u3(2.35935,4.70053,1.91036,q[0])
qc.u3(1.86373,0.86456,2.57327,q[3])
qc.u1(4.90081,q[4])
qc.u1(4.75864,q[1])
qc.u3(1.23492,1.00355,3.86044,q[3])
qc.u3(0.15065,0.91576,3.869,q[0])
qc.u3(1.03543,1.87867,1.89681,q[3])
qc.ccx(q[1],q[3],q[6])
qc.u3(0.04871,2.04223,5.29329,q[1])
qc.u3(0.12222,2.35582,0.50426,q[1])
qc.u3(1.44636,0.76622,5.11985,q[3])
qc.u2(5.94785,0.37362,q[0])
qc.u3(1.70024,5.75474,1.50208,q[4])
qc.u2(2.83154,0.58593,q[6])
qc.ccx(q[6],q[3],q[5])
qc.ccx(q[2],q[6],q[1])
qc.ccx(q[0],q[2],q[1])
qc.u2(3.6452,2.23033,q[3])
qc.ccx(q[2],q[6],q[4])
qc.cx(q[4],q[3])
qc.ccx(q[2],q[1],q[6])
qc.u2(5.73669,3.87937,q[5])
qc.u1(0.25795,q[3])
qc.cx(q[0],q[6])
qc.u1(2.75446,q[2])
qc.cx(q[6],q[5])
qc.u2(0.03101,0.85697,q[5])
qc.u3(1.22585,4.13468,1.51573,q[5])
qc.u3(0.21733,5.48483,5.78136,q[5])
qc.ccx(q[0],q[5],q[6])
qc.ccx(q[5],q[4],q[2])
qc.u2(6.1741,6.05367,q[5])
qc.u1(2.55065,q[6])
qc.u1(3.38869,q[0])
qc.ccx(q[0],q[5],q[6])
qc.ccx(q[3],q[2],q[6])
qc.u3(1.21839,2.1262,2.28127,q[6])
qc.ccx(q[0],q[2],q[3])
qc.u1(5.28439,q[0])
qc.u2(5.66766,0.48067,q[5])
qc.u1(5.35951,q[2])
qc.ccx(q[1],q[0],q[2])
qc.u1(4.44136,q[5])
qc.u3(2.56538,5.17451,5.09548,q[0])
qc.u3(0.02454,1.07135,1.6338,q[4])
qc.u2(1.26671,1.51715,q[6])
qc.u2(5.58833,4.13817,q[1])
qc.cx(q[6],q[3])
qc.ccx(q[6],q[1],q[5])
qc.ccx(q[3],q[2],q[5])
qc.u1(1.70564,q[2])
qc.u3(0.77234,1.68789,2.80092,q[3])
qc.u2(5.71929,4.16156,q[0])
qc.cx(q[0],q[1])
qc.u1(4.71936,q[4])
qc.u1(2.55312,q[6])
qc.u3(1.30623,0.68612,2.46454,q[4])
qc.u3(1.09624,4.00031,0.69411,q[4])
qc.u2(2.55065,0.71763,q[1])
qc.u1(2.07722,q[5])
qc.u2(5.47585,3.73475,q[4])
qc.u3(0.36635,3.46387,1.84693,q[3])
qc.u1(0.34088,q[6])
qc.u1(5.60384,q[0])
qc.cx(q[4],q[3])
qc.u1(4.75638,q[4])
qc.u1(6.23369,q[4])
qc.u3(2.58068,5.51704,1.82827,q[1])
qc.u1(5.30153,q[4])
qc.ccx(q[5],q[2],q[4])
qc.u1(4.92287,q[5])
qc.cx(q[6],q[3])
qc.ccx(q[3],q[6],q[5])
qc.ccx(q[4],q[0],q[1])
qc.cx(q[3],q[1])
qc.u1(0.71379,q[1])
qc.u2(0.43723,4.13064,q[2])
qc.u2(5.05762,4.61388,q[3])
qc.u2(6.08591,0.11434,q[0])
qc.cx(q[3],q[6])
qc.u2(3.07783,5.36598,q[0])
qc.cx(q[5],q[4])
qc.u3(0.5774,0.23372,0.35943,q[4])
qc.u3(2.02551,3.3552,0.79619,q[2])
qc.u2(2.24351,0.06234,q[1])
qc.u2(1.13875,4.99123,q[5])
qc.u1(1.45344,q[1])
qc.cx(q[4],q[1])
qc.u2(0.68494,3.56547,q[2])
qc.u3(2.96365,1.06275,4.13761,q[4])
qc.u3(0.18411,3.16175,5.04487,q[3])
qc.cx(q[1],q[6])
qc.u2(0.30286,3.65485,q[1])
qc.cx(q[1],q[3])
qc.cx(q[4],q[1])
qc.u2(0.246,1.18707,q[2])
qc.u3(1.32765,0.77541,6.24382,q[0])
qc.u2(5.99401,5.25131,q[6])
qc.u1(2.98494,q[0])
qc.ccx(q[4],q[2],q[0])
qc.ccx(q[0],q[6],q[2])
qc.ccx(q[4],q[2],q[5])
qc.u2(1.91506,5.07522,q[3])
qc.u1(1.0406,q[4])
qc.u1(0.32941,q[4])
qc.u3(2.46226,5.7578,4.10154,q[0])
qc.u3(0.67843,1.13811,5.50759,q[3])
qc.u3(3.13352,0.70962,2.52175,q[2])
qc.u1(3.30009,q[0])
qc.cx(q[5],q[3])
qc.cx(q[2],q[6])
qc.u2(5.14195,6.19736,q[5])
qc.u3(2.97185,1.58426,5.30026,q[2])
qc.ccx(q[6],q[5],q[0])
qc.cx(q[0],q[2])
qc.u2(0.65034,5.54204,q[1])
qc.u2(1.78409,2.33095,q[5])
qc.u3(0.92945,2.43681,6.13385,q[3])
qc.cx(q[1],q[5])
qc.u2(4.21529,5.44288,q[2])
qc.u3(1.65823,5.60172,4.44615,q[4])
qc.u1(4.2821,q[5])
qc.u3(0.30546,1.78568,2.01589,q[1])
qc.u1(0.63549,q[2])
qc.ccx(q[4],q[5],q[3])
qc.u3(2.57652,1.03255,6.14623,q[6])
qc.u1(4.85118,q[1])
qc.ccx(q[0],q[6],q[1])
qc.cx(q[5],q[1])
qc.ccx(q[4],q[5],q[1])
qc.u3(1.16322,2.00232,2.09629,q[4])
qc.ccx(q[1],q[2],q[3])
qc.u3(1.53462,1.56125,2.18908,q[5])
qc.cx(q[5],q[2])
qc.u3(0.58501,3.41414,4.02458,q[4])
qc.cx(q[6],q[3])
qc.cx(q[4],q[3])
qc.ccx(q[6],q[1],q[4])
qc.u2(0.1496,1.19281,q[4])
qc.u1(3.08762,q[0])
qc.ccx(q[6],q[5],q[1])
qc.u3(3.00114,3.9324,6.02038,q[0])
qc.u2(4.47116,3.63406,q[5])
qc.u3(1.73459,4.00958,3.75562,q[6])
qc.u1(3.90013,q[3])
qc.cx(q[5],q[6])
qc.ccx(q[4],q[2],q[3])
qc.u2(0.67472,5.21132,q[6])
qc.u2(5.25679,3.50902,q[6])
qc.ccx(q[6],q[1],q[3])
qc.ccx(q[1],q[5],q[2])
qc.cx(q[3],q[4])
qc.cx(q[2],q[0])
qc.u3(1.38176,4.73731,1.6459,q[2])
qc.u2(4.08898,0.72903,q[3])
qc.u2(2.78959,4.7843,q[0])
qc.u2(1.63323,4.81755,q[2])
qc.u2(0.76385,1.03,q[6])
qc.ccx(q[4],q[5],q[0])
qc.cx(q[0],q[4])
qc.u1(5.39448,q[6])
qc.u2(1.63705,0.54765,q[5])
qc.u2(0.16126,3.15494,q[6])
qc.u1(2.96708,q[0])
qc.cx(q[5],q[4])
qc.u1(5.3095,q[5])
qc.u1(5.82119,q[6])
qc.u2(2.81619,0.27652,q[5])
qc.u2(2.80906,3.88926,q[1])
qc.u1(0.64133,q[3])
qc.ccx(q[3],q[4],q[6])
qc.u1(1.40169,q[1])
qc.ccx(q[3],q[1],q[0])
qc.ccx(q[5],q[2],q[3])
qc.ccx(q[1],q[4],q[2])
qc.u2(1.74477,3.68597,q[3])
qc.u2(5.0509,5.90445,q[1])
qc.ccx(q[3],q[6],q[5])
qc.u3(0.25635,2.81802,2.29124,q[6])
qc.u2(1.81329,4.09565,q[5])
qc.u2(1.33986,4.81134,q[3])
qc.ccx(q[1],q[6],q[2])
qc.u1(1.13555,q[2])
qc.u3(0.71214,3.72261,2.87981,q[1])
qc.u1(0.96128,q[2])
qc.u2(5.33592,1.70843,q[1])
qc.cx(q[4],q[5])
qc.u1(1.30914,q[0])
qc.ccx(q[2],q[6],q[3])
qc.cx(q[1],q[2])
qc.u1(0.25276,q[1])
qc.u2(3.3188,1.61573,q[5])
qc.u1(3.88818,q[5])
qc.cx(q[5],q[2])
qc.u2(3.34386,4.2991,q[1])
qc.u2(1.48465,4.66018,q[0])
qc.u1(5.26068,q[0])
qc.cx(q[5],q[3])
qc.ccx(q[5],q[3],q[1])
qc.cx(q[0],q[3])
qc.u2(0.17939,2.10013,q[6])
qc.u2(3.12609,2.49238,q[4])
qc.u1(3.44039,q[4])
qc.u2(2.73912,2.89089,q[5])
qc.u3(3.02095,4.0899,1.33392,q[3])
qc.cx(q[6],q[1])
qc.u1(4.95777,q[1])
qc.u1(1.23067,q[1])
qc.ccx(q[0],q[2],q[4])
qc.u2(2.37547,6.22371,q[2])
qc.cx(q[3],q[0])
qc.u3(2.18082,2.71584,2.59006,q[4])
qc.u3(1.47386,6.20183,5.76277,q[4])
qc.u3(3.12601,5.70324,6.12419,q[5])
qc.cx(q[4],q[0])
qc.u3(2.81388,5.21547,4.99059,q[3])
qc.cx(q[6],q[3])
qc.u2(1.02287,4.04086,q[1])
qc.ccx(q[5],q[1],q[3])
qc.u1(2.73395,q[0])
qc.u1(5.22759,q[3])
qc.cx(q[6],q[2])
qc.u2(5.77836,5.17948,q[2])
qc.u3(0.45871,1.74055,2.12043,q[6])
qc.ccx(q[3],q[6],q[4])
qc.cx(q[2],q[4])
qc.u1(3.57712,q[1])
qc.cx(q[2],q[1])
qc.cx(q[1],q[6])
qc.cx(q[5],q[2])
qc.u1(5.56704,q[5])
qc.cx(q[6],q[4])
qc.u1(1.982,q[5])
qc.cx(q[2],q[0])
qc.u1(1.54713,q[2])
qc.ccx(q[0],q[4],q[6])
qc.u1(4.00938,q[3])
qc.u2(1.61433,3.84108,q[3])
qc.cx(q[3],q[6])
qc.cx(q[4],q[3])
qc.cx(q[6],q[3])
qc.u3(0.82358,3.43203,3.8688,q[6])
qc.u2(5.12682,5.99073,q[6])
qc.u3(1.18299,0.88552,0.90114,q[3])
qc.ccx(q[1],q[5],q[6])
qc.u2(0.79181,3.36517,q[6])
qc.u3(2.17411,3.33639,1.74885,q[5])
qc.u3(2.82485,4.32845,3.43803,q[4])
qc.u1(5.98516,q[4])
qc.u1(2.44474,q[4])
qc.u1(5.76602,q[5])
qc.u3(1.86217,0.96104,1.92212,q[4])
qc.u2(2.25112,2.15256,q[0])
qc.cx(q[6],q[4])
qc.ccx(q[5],q[1],q[6])
qc.cx(q[5],q[0])
qc.cx(q[1],q[0])
qc.u2(2.97668,5.42237,q[2])
qc.cx(q[3],q[1])
qc.u3(1.28908,3.06685,2.49885,q[4])
qc.u2(1.86383,3.10818,q[1])
qc.u3(0.86099,0.26759,5.9855,q[5])
qc.u2(3.51205,0.31251,q[3])
qc.u1(1.96109,q[2])
qc.cx(q[1],q[4])
qc.u1(2.42514,q[0])
qc.u1(5.97459,q[1])
qc.ccx(q[0],q[6],q[1])
qc.u2(0.09697,3.06359,q[2])
qc.u2(2.83118,4.37504,q[6])
qc.u3(2.20308,1.98044,0.034,q[1])
qc.u2(0.5996,6.11151,q[4])
qc.ccx(q[2],q[4],q[6])
qc.ccx(q[3],q[0],q[2])
qc.cx(q[0],q[1])
qc.u3(0.09819,2.31937,2.99136,q[5])
qc.u1(4.44883,q[1])
qc.u2(1.50328,2.65304,q[6])
qc.u3(1.5483,3.64231,2.36717,q[4])
qc.u2(2.25128,1.16919,q[6])
qc.cx(q[0],q[4])
qc.cx(q[4],q[0])
qc.u3(2.24491,2.76839,4.05553,q[4])
qc.ccx(q[3],q[6],q[4])
qc.u2(5.98938,2.54854,q[3])
qc.cx(q[1],q[2])
qc.u1(5.4626,q[4])
qc.ccx(q[6],q[5],q[0])
qc.u2(0.61541,1.95265,q[1])
qc.u3(2.76032,5.03734,1.44215,q[2])
qc.ccx(q[3],q[1],q[4])
qc.u2(4.344,3.39108,q[5])
qc.u3(0.72338,4.11654,4.44874,q[4])
qc.u2(6.2169,1.12834,q[1])
qc.cx(q[1],q[4])
qc.u2(5.3398,0.68252,q[4])
qc.u1(0.53866,q[4])
qc.ccx(q[1],q[4],q[6])
qc.ccx(q[3],q[5],q[2])
qc.cx(q[1],q[0])
qc.u1(5.2907,q[1])
qc.ccx(q[3],q[4],q[2])
qc.u3(0.60884,5.04791,4.38398,q[1])
qc.ccx(q[4],q[5],q[2])
qc.ccx(q[5],q[4],q[0])
qc.u3(0.77214,4.2058,0.35852,q[5])
qc.u1(0.79471,q[0])
qc.u3(1.88131,5.50463,5.6144,q[1])
qc.u3(2.13645,1.1659,5.1014,q[0])
qc.cx(q[5],q[2])
qc.u2(3.38178,6.25999,q[2])
qc.u2(5.93455,0.18637,q[6])
qc.u1(2.74116,q[0])
qc.u3(2.85943,1.84014,1.24961,q[2])
qc.ccx(q[5],q[4],q[2])
qc.u3(1.35045,4.51432,4.63457,q[2])
qc.u1(0.4475,q[0])
qc.ccx(q[5],q[1],q[0])
qc.u3(0.25933,5.07646,3.77304,q[6])
qc.u3(0.15383,3.86846,3.48877,q[2])
qc.ccx(q[0],q[1],q[6])
qc.u3(2.30911,4.52663,4.43949,q[3])
qc.ccx(q[3],q[1],q[0])
qc.cx(q[3],q[2])
qc.u3(0.67216,3.53212,5.90279,q[6])
qc.u3(2.85989,0.15059,0.7554,q[5])
qc.u3(1.71223,3.94229,6.13516,q[0])
qc.cx(q[1],q[3])
qc.ccx(q[0],q[4],q[1])
qc.cx(q[4],q[6])
qc.ccx(q[2],q[6],q[1])
qc.ccx(q[4],q[5],q[2])
qc.u2(3.87037,5.13798,q[1])
qc.ccx(q[5],q[0],q[3])
qc.cx(q[4],q[2])
qc.u3(1.36309,4.31125,0.31953,q[1])
qc.u3(0.63511,0.65529,1.12683,q[6])
qc.cx(q[5],q[0])
qc.u1(0.40623,q[1])
qc.u1(6.03535,q[4])
qc.u3(2.92216,3.36488,3.84702,q[3])
qc.cx(q[0],q[3])
qc.u2(0.45229,4.2454,q[3])
qc.u1(1.99819,q[0])
qc.u3(0.19055,2.91376,3.93718,q[3])
qc.u3(2.90492,4.73678,1.13372,q[0])
qc.ccx(q[5],q[3],q[6])
qc.ccx(q[6],q[1],q[5])
qc.cx(q[1],q[5])
qc.u1(2.0954,q[4])
qc.cx(q[6],q[4])
qc.u2(1.39324,4.65002,q[0])
qc.ccx(q[3],q[5],q[1])
qc.cx(q[5],q[4])
qc.u3(2.92776,3.74179,3.7035,q[2])
qc.u3(0.27299,5.53355,5.61253,q[6])
qc.u3(1.94271,3.24375,5.09162,q[6])
qc.ccx(q[6],q[4],q[2])
qc.u2(1.58712,5.41481,q[4])
qc.u3(2.62508,4.43228,5.78141,q[0])
qc.u1(4.18259,q[1])
qc.ccx(q[1],q[6],q[4])
qc.u3(0.01558,5.27876,3.43576,q[3])
qc.u3(0.27183,5.26069,6.08262,q[6])
qc.ccx(q[6],q[5],q[2])
qc.u3(2.89896,1.09351,4.13561,q[3])
qc.ccx(q[1],q[4],q[5])
qc.cx(q[2],q[3])
qc.ccx(q[3],q[4],q[0])
qc.ccx(q[3],q[4],q[2])
qc.cx(q[4],q[1])
qc.u1(4.74122,q[5])
qc.u2(2.76822,3.22508,q[6])
qc.ccx(q[4],q[1],q[3])
qc.ccx(q[1],q[2],q[6])
qc.u2(0.60877,3.71146,q[1])
qc.u1(3.80164,q[5])
qc.cx(q[0],q[4])
qc.u1(5.70489,q[2])
qc.u3(1.76071,0.40447,5.70378,q[1])
qc.ccx(q[2],q[3],q[0])
qc.ccx(q[0],q[5],q[2])
qc.u3(1.29766,1.70792,0.54918,q[5])
qc.u3(1.57734,5.94977,4.17904,q[0])
qc.u1(3.6328,q[2])
qc.u2(4.58958,6.11856,q[5])
qc.u2(5.29029,0.25686,q[2])
qc.cx(q[1],q[2])
qc.u3(2.81355,3.56925,2.08217,q[3])
qc.u3(1.28425,2.03912,0.31105,q[1])
qc.cx(q[1],q[6])
qc.u2(2.42066,4.03648,q[3])
qc.ccx(q[0],q[3],q[1])
qc.u1(2.14576,q[5])
qc.u1(3.78736,q[1])
qc.u2(5.7087,0.25602,q[2])
qc.cx(q[2],q[1])
qc.u3(0.84252,2.27146,0.11389,q[4])
qc.u3(0.93706,0.62703,5.16949,q[0])
qc.u1(0.87605,q[2])
qc.u2(1.70473,5.20663,q[6])
qc.cx(q[5],q[4])
qc.u1(2.32327,q[5])
qc.u1(1.15597,q[6])
qc.u3(2.66419,5.87521,5.94877,q[5])
qc.u1(2.52999,q[4])
qc.ccx(q[4],q[5],q[3])
qc.u2(0.53945,0.21534,q[1])
qc.u1(0.8999,q[1])
qc.u1(1.36094,q[1])
qc.cx(q[3],q[0])
qc.cx(q[5],q[2])
qc.u2(6.25074,0.16417,q[5])
qc.cx(q[2],q[6])
qc.ccx(q[2],q[6],q[1])
qc.cx(q[1],q[0])
qc.u3(0.97276,4.78131,5.93737,q[2])
qc.cx(q[5],q[4])
qc.cx(q[3],q[2])
qc.cx(q[3],q[2])
qc.ccx(q[6],q[0],q[5])
qc.u3(0.25782,5.41406,3.40002,q[1])
qc.ccx(q[2],q[4],q[1])
qc.u3(2.35491,0.24473,0.9711,q[2])
qc.cx(q[3],q[6])
qc.ccx(q[5],q[2],q[0])
qc.u2(4.46753,5.55801,q[5])
qc.u2(1.08005,5.28248,q[4])
qc.cx(q[5],q[4])
qc.u3(0.04303,3.54431,5.16325,q[6])
qc.u3(0.74404,0.34316,1.29178,q[4])
qc.u3(0.90023,1.42992,4.97508,q[3])
qc.u3(2.91384,0.37992,2.90066,q[1])
qc.ccx(q[4],q[0],q[1])
qc.ccx(q[6],q[3],q[2])
qc.ccx(q[6],q[5],q[3])
qc.u3(0.05138,4.24199,0.6209,q[2])
qc.cx(q[4],q[5])
qc.u2(5.30939,5.10238,q[5])
qc.cx(q[6],q[0])
qc.cx(q[4],q[1])
qc.u1(5.70898,q[3])
qc.u2(1.24265,1.20075,q[4])
qc.cx(q[6],q[1])
qc.cx(q[4],q[5])
qc.u3(1.20912,2.68089,5.76902,q[2])
qc.cx(q[1],q[3])
qc.cx(q[5],q[4])
qc.cx(q[1],q[6])
qc.u2(3.46015,4.6497,q[5])
qc.u2(1.09575,5.17264,q[2])
qc.ccx(q[6],q[1],q[2])
qc.u1(4.45261,q[6])
qc.u3(2.00542,5.96974,0.4366,q[0])
qc.u1(3.52971,q[2])
qc.u2(4.15552,0.69649,q[3])
qc.cx(q[0],q[5])
qc.u1(5.54793,q[2])
qc.u1(3.9721,q[3])
qc.u1(4.99622,q[5])
qc.u3(1.6972,6.17121,5.25118,q[4])
qc.u1(0.3483,q[5])
qc.ccx(q[0],q[3],q[6])
qc.u2(4.84815,2.60112,q[2])
qc.u1(0.71693,q[6])
qc.ccx(q[0],q[1],q[6])
qc.cx(q[1],q[3])
qc.u2(5.89614,5.19565,q[4])
qc.ccx(q[0],q[5],q[1])
qc.u3(1.93576,3.80632,0.51976,q[1])
qc.u2(4.86373,6.19345,q[2])
qc.u3(2.01302,5.38609,2.78517,q[4])
qc.cx(q[3],q[5])
qc.u3(2.7293,2.72719,0.01292,q[5])
qc.u1(3.7566,q[2])
qc.cx(q[0],q[2])
qc.cx(q[5],q[6])
qc.ccx(q[2],q[5],q[4])
qc.u3(1.30094,3.23576,2.20965,q[6])
qc.cx(q[5],q[0])
qc.u3(2.79676,5.87745,5.82071,q[1])
qc.u1(1.71246,q[5])
qc.u3(2.51302,5.78484,5.13317,q[1])
qc.u1(4.54118,q[4])
qc.u3(1.91766,1.92315,0.69345,q[5])
qc.u3(0.69689,2.11379,0.51656,q[2])
qc.ccx(q[5],q[6],q[2])
qc.u2(6.2246,2.44059,q[3])
qc.u3(1.81588,3.98208,5.01067,q[2])
qc.u1(0.23898,q[4])
qc.u3(2.68858,0.42183,1.26817,q[4])
qc.u1(3.17426,q[0])
qc.u1(6.14057,q[1])
qc.u3(1.58874,1.33534,3.00956,q[3])
qc.cx(q[0],q[5])
qc.u1(4.69024,q[5])
qc.u3(2.27375,5.22569,4.67783,q[3])
qc.u2(1.8725,2.61889,q[2])
qc.cx(q[5],q[3])
qc.ccx(q[3],q[5],q[6])
qc.u3(0.15163,3.30463,1.21494,q[2])
qc.u3(1.22848,1.89266,2.88452,q[2])
qc.u3(3.01141,0.77929,4.99197,q[4])
qc.cx(q[6],q[5])
qc.ccx(q[4],q[0],q[6])
qc.u3(2.42519,3.75323,3.46149,q[1])
qc.cx(q[1],q[5])
qc.cx(q[2],q[5])
qc.u3(2.28268,1.67639,1.59872,q[2])
qc.cx(q[5],q[3])
qc.cx(q[0],q[6])
qc.u1(0.6801,q[5])
qc.ccx(q[5],q[6],q[1])
qc.ccx(q[3],q[5],q[1])
qc.cx(q[1],q[0])
qc.u2(5.77662,4.00061,q[6])
qc.u2(0.89073,0.38079,q[4])
qc.u1(5.07889,q[1])
qc.u3(1.60851,5.63674,6.02136,q[2])
qc.ccx(q[0],q[1],q[6])
qc.u3(1.87152,5.06739,6.24983,q[6])
qc.u2(0.61148,4.26799,q[0])
qc.cx(q[4],q[3])
qc.u2(2.8951,2.8991,q[1])
qc.u2(1.09515,5.32552,q[1])
qc.u1(2.53825,q[6])
qc.u1(2.35514,q[2])
qc.u1(5.12719,q[3])
qc.u3(1.09669,3.56136,2.72403,q[4])
qc.ccx(q[1],q[5],q[2])
qc.cx(q[1],q[3])
qc.u1(0.12032,q[4])
qc.u2(0.60845,3.68209,q[1])
qc.ccx(q[3],q[1],q[4])
qc.u2(1.46953,3.05809,q[3])
qc.cx(q[2],q[3])
qc.u1(2.90096,q[3])
qc.cx(q[5],q[1])
qc.u2(4.81386,1.64558,q[1])
qc.cx(q[4],q[6])
qc.cx(q[0],q[1])
qc.cx(q[2],q[0])
qc.ccx(q[1],q[0],q[6])
qc.u3(1.2311,3.17856,2.90523,q[6])
qc.u3(2.68303,3.76334,4.33513,q[4])
qc.u1(5.94466,q[3])
qc.u3(0.20529,3.12987,4.67914,q[6])
qc.ccx(q[2],q[4],q[6])
qc.u2(3.76444,2.56744,q[2])
qc.ccx(q[1],q[6],q[3])
qc.u3(0.18808,1.00243,5.79709,q[5])
qc.ccx(q[1],q[2],q[0])
qc.u3(1.52816,0.49914,4.99226,q[3])
qc.cx(q[5],q[1])
qc.cx(q[6],q[3])
qc.u1(5.32134,q[1])
qc.u1(5.98122,q[6])
qc.u2(2.19801,2.17193,q[5])
qc.cx(q[1],q[6])
qc.ccx(q[5],q[2],q[4])
qc.ccx(q[6],q[3],q[5])
qc.u3(0.8473,5.02193,5.37456,q[1])
qc.cx(q[5],q[4])
qc.ccx(q[2],q[1],q[5])
qc.u2(2.09625,3.46651,q[4])
qc.ccx(q[5],q[4],q[2])
qc.u1(0.62711,q[3])
qc.u2(5.13362,0.59025,q[6])
qc.u3(1.91339,1.22541,4.52531,q[4])
qc.u3(2.24521,0.41319,3.88032,q[1])
qc.cx(q[2],q[5])
qc.u3(2.19873,2.81297,0.40162,q[5])
qc.u2(4.64386,0.75958,q[3])
qc.u1(4.1753,q[1])
qc.u1(5.25025,q[0])
qc.ccx(q[3],q[0],q[2])
qc.ccx(q[5],q[3],q[1])
qc.u2(2.99385,1.80059,q[6])
qc.u3(1.10086,5.51983,2.80593,q[4])
qc.u2(2.38896,3.23831,q[2])
qc.ccx(q[5],q[4],q[1])
qc.u3(2.17355,3.3842,4.60762,q[3])
qc.u2(1.20954,3.12331,q[0])
qc.u3(2.21237,5.0213,4.93746,q[0])
qc.u2(2.37823,1.97362,q[0])
qc.cx(q[5],q[3])
qc.u3(2.42414,5.70682,2.54188,q[1])
qc.ccx(q[0],q[1],q[3])
qc.cx(q[3],q[1])
qc.u1(3.97323,q[2])
qc.cx(q[1],q[4])
qc.u1(5.8933,q[4])
qc.u3(2.70403,3.28002,6.25251,q[4])
qc.u3(1.49031,0.98404,4.84558,q[6])
qc.u2(1.30754,1.52805,q[4])
qc.u1(2.76263,q[6])
qc.ccx(q[5],q[1],q[6])
qc.u3(2.16922,3.46194,0.53543,q[5])
circuits = [qc]
job = execute(circuits, backend, **options)
result = job.result()
print(result)
#job = execute(circuits, backend2, **options)
#result = job.result()
#print(result)
#a = np.loadtxt('a.txt',dtype=complex)
#b = np.loadtxt('a1.txt',dtype=complex)
#p = a.real
#q = a.imag
#c = b.real
#d = b.imag
#if(np.allclose(p,c) and np.allclose(q,d)):
#    print('Your result is right.')
#else:
#    print('Your result is wrong') 