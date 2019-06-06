import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime

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

#fit
def linear(x, a, c):
    return a * x + c

# popt, pcov = curve_fit(linear, AMF[:416],np.abs(result_of_convolution_O3[:416]),p0=[1.0 * 10**19,-1.0 * 10**19])
popt_1, pcov_1 = curve_fit(linear, AMF[:416], result_of_convolution_O3[:416],p0=[1.0 * 10**19,-1.0 * 10**19])
popt_2, pcov_2 = curve_fit(linear, AMF[380:394], result_of_convolution_O3[380:394],p0=[1.0 * 10**19,-1.0 * 10**19])


#plot
k = np.linspace(-0.1,3.5,500)
# plot = plt.errorbar(AMF[:416],np.abs(result_of_convolution_O3[:416]), yerr=result_of_convolution_O3_error[:416], label='Messdaten für O3',fmt = '.')
plot = plt.errorbar(AMF[:416], result_of_convolution_O3[:416], yerr=result_of_convolution_O3_error[:416], label='Messdaten für O3',fmt = '.')
plt.plot(k ,linear(k , *popt_1), 'r-', label='Fit 1', color='black') 
plt.plot(k ,linear(k , *popt_2), 'r-', label='Fit 2', color='black') 

plt.legend()
axes = plt.gca()
plt.ylabel("$\Delta$SCD für O$_3$")
plt.xlabel("AMF")

f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
#plt.show()
plt.savefig('scd_fit_o3.pdf')
print(popt_1, pcov_1)
print('Steigung:', popt_1[0])
print('y_Achsenabschnitt:', popt_1[1])
print('Kovarianz:', np.sqrt(pcov_1[0][0]))


print(popt_2, pcov_2)
print('Steigung:', popt_2[0])
print('y_Achsenabschnitt:', popt_2[1])
print('Kovarianz:', np.sqrt(pcov_2[0][0]))

