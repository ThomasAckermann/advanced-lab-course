# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime
from matplotlib import rcParams
import datetime
rcParams['font.size'] = 25
rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = '\usepackage{libertine}'


#import data

dateiname = "Atmospheric_Measurements/resultoo32.dat"

file_num  = np.genfromtxt(dateiname, skip_header=1,usecols=(0))
Datum  = np.genfromtxt(dateiname, skip_header=1,usecols=(1), dtype='object')
StartZeit  = np.genfromtxt(dateiname, skip_header=1,usecols=(2), dtype='object')
SZA  = np.genfromtxt(dateiname, skip_header=1,usecols=(3))
AMF  = 1 / np.cos(2 * np.pi * SZA / 360) 
ChiSquare  = np.genfromtxt(dateiname, skip_header=1,usecols=(4))
Streulicht_midday_log  = np.genfromtxt(dateiname, skip_header=1,usecols=(5))
Streulicht_midday_log_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(6))
Ring_Streulicht_midday  = np.genfromtxt(dateiname, skip_header=1,usecols=(7))
Ring_Streulicht_midday_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(8))
result_of_convolution_O3  = np.genfromtxt(dateiname, skip_header=1,usecols=(9))
result_of_convolution_O3_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(10))
result_of_convolution_NO2  = np.genfromtxt(dateiname, skip_header=1,usecols=(11))
result_of_convolution_NO2_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(12))
result_of_convolution_O4  = np.genfromtxt(dateiname, skip_header=1,usecols=(13))
result_of_convolution_O4_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(14))

print(SZA)
# VCD = (7.9325*10**18+result_of_convolution_O3) * np.cos(2 * np.pi * SZA / 360) / (2.6 * 10**16)
VCD = (0.97*10**19+result_of_convolution_O3) * np.cos(2 * np.pi * SZA / 360) / (2.6 * 10**16)
VCD_error = np.sqrt((result_of_convolution_O3_error*np.cos(2*np.pi*SZA/360))**2 + (0.017*10**18*np.cos(2*np.pi*SZA/360))**2) / (2.6 * 10**16)

VCD_error = np.delete(VCD_error, np.argmax(VCD))
StartZeit = np.delete(StartZeit, np.argmax(VCD))
VCD = np.delete(VCD, np.argmax(VCD))

# AMF = np.delete(AMF[:416], np.argmax(result_of_convolution_O3[:416]))
# result_of_convolution_O3_error = np.delete(result_of_convolution_O3_error[:416], np.argmax(result_of_convolution_O3[:416]))
# result_of_convolution_O3 = np.delete(result_of_convolution_O3[:416], np.argmax(result_of_convolution_O3[:416]))

# VCD_error = VCD_error[200:]
# StartZeit = StartZeit[200:]
# VCD = VCD[200:]
# print(np.argmax(VCD))
# print(np.max(VCD))
# print(np.shape(VCD), np.shape(VCD_error))
# VCD = np.array([VCD.pop(np.argmax(result_of_convolution_O3))])
# VCD_error = np.array([VCD_error.pop(np.argmax(result_of_convolution_O3))])
# plot
k = np.linspace(0,3.5,500)
plot = plt.errorbar(StartZeit, VCD, yerr=VCD_error, label='Messdaten für O3',fmt='ks', markersize=4)
# plot = plt.errorbar(StartZeit, VCD, label='Messdaten für O3', fmt='.', markersize=3)
axes = plt.gca()
plt.ylabel("VCD für O3 in Moleküle/cm$^2$")
plt.xlabel("Uhrzeit UCT")

# nötig falls gegen Uhrzeit geplottet wird
a = []
for i in range(len(axes.get_xticks())):
    if (i%65 == 0):
        a.append(i)

ticks = []
for i in a:
    ticks.append(axes.get_xticks()[i])
axes.set_xticks(ticks)
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
# plt.show()
plt.savefig('VCD_O3_over_day.pdf')
