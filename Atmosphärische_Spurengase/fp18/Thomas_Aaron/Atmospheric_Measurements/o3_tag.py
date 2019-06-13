import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime
from matplotlib import rcParams
rcParams['font.size'] = 23
rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = '\usepackage{libertine}'


#import data

dateiname = "resultoo32.dat"

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


#plot
plot = plt.errorbar(StartZeit, result_of_convolution_O3, yerr=result_of_convolution_O3_error, label='Messdaten für NO2',fmt = 'ks', markersize=3)
axes = plt.gca()
plt.ylabel("$\Delta$SCD für NO2 Molkeüle/cm$^2$")
plt.xlabel("Messzeit in UTC")

#nötig falls gegen Uhrzeit geplottet wird

a = []
for i in range(len(axes.get_xticks())):
    if (i%60 == 0):
        a.append(i)

ticks = []
for i in a:
    ticks.append(axes.get_xticks()[i])
axes.set_xticks(ticks)

f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
# plt.show()
plt.savefig('o3_tag.pdf')
