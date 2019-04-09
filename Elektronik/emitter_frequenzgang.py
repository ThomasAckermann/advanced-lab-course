import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




def func(x, a, b):
    return a * x + b

freq = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
    150, 200, 250, 300, 350, 1000, 10000, 50000, 75000, 100000, 500000])
u_a = np.array([2.10, 3.38, 4.27, 4.84, 5.18, 5.41, 5.56, 5.68, 5.75, 5.79, 5.87,
    5.94, 5.94, 5.98, 5.97, 6.03, 5.86, 5.88, 5.90, 5.92, 5.92, 5.75, 5.61, 5.44, 3.33])
u_a_err = np.array([6, 4, 7, 5, 6, 4, 4, 5, 6, 7, 4, 5, 6, 6, 4, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7])/100
u_e = 296.0/1000
u_e_err = np.array([])
ver = u_a / u_e
# ver_err = np.sqrt((u_a_err/u_e)**2 + (u_a * u_e_err / u_e**2)**2 )



x = np.linspace(10,300,100000)

popt, pcov = curve_fit(func, np.log10(freq[:6]), np.log10(ver[:6]))# , sigma=ver_err)


plt.plot(freq, ver, label='Messdaten')
plt.plot(x, 10**func(np.log10(x), *popt), label='Fit')

max_v = np.max(ver[15:]) * np.ones(len(freq))
max_sqrt = (np.max(ver[15:])/np.sqrt(2)) * np.ones(len(freq))
# print(np.abs(ys - max_sqrt[0]))

d = (10**func(np.log10(x), *popt)) - max_sqrt[0]

a = np.argmin(np.abs(d))
print('Grenzfrequenz: ', x[a])
plt.plot(freq, max_v, label='max')
plt.plot(freq, max_sqrt, label='max_sqrt')

plt.xlabel('Frequenz $f$')
plt.ylabel('Verstaerkung $V$')
plt.title('Abb. 1: Frequenzgang bei Emitterschaltung')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig('fig/emitter_frequenzgang.pdf')
# plt.show()

# maximum = np.max(ver)
# print(maximum)
# ver_gr = maximum / np.sqrt(2)
# f_gr = np.argmin(np.abs(ys - ver_gr))
# print(np.round(np.abs(ys - ver_gr),2))
# print(f_gr)
# print(arr[f_gr])

