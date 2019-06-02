import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime

#import data

dateiname = "Atmospheric_Measurements/resultno2.dat"

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
result_of_convolution_H20  = np.genfromtxt(dateiname, skip_header=1,usecols=(11))
result_of_convolution_H20_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(12))
result_of_convolution_NO2  = np.genfromtxt(dateiname, skip_header=1,usecols=(13))
result_of_convolution_NO2_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(14))
result_of_convolution_O4  = np.genfromtxt(dateiname, skip_header=1,usecols=(15))
result_of_convolution_O4_error  = np.genfromtxt(dateiname, skip_header=1,usecols=(16))

#fit
def linear(x, a, c):
    return a * x + c

popt, pcov = curve_fit(linear, AMF[400:416], result_of_convolution_O3[400:416],p0=[1.0 * 10**16,-1.0 * 10**16])

#plot
k = np.linspace(0,3.5,500)
plot = plt.errorbar(AMF[:416], result_of_convolution_NO2[:416], yerr=result_of_convolution_NO2_error[:416], label='Messdaten für NO2',fmt = '.')
plt.plot(k ,linear( k , *popt), 'r-', label='Fit', color='black') 
axes = plt.gca()
plt.ylabel("$\Delta$SCD für NO2")
plt.xlabel("AMF")

#nötig falls gegen Uhrzeit geplottet wird
#for index, label in enumerate(axes.xaxis.get_ticklabels()):
#    if index % 45 !=0:
#        label.set_visible(False)

f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.show()
print(popt, pcov)
print('Steigung:', popt[0])
print('y_Achsenabschnitt:', popt[1])
print('Kovarianz:', np.sqrt(pcov[0][0]))
