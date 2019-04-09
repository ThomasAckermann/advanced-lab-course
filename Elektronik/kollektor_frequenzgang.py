import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * x + b


freq = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
    150, 200, 250, 300, 350, 1000, 10000, 50000, 75000, 100000, 500000, 1000000])

u_a = np.array([114, 226, 305, 362, 403, 430, 448, 480, 486, 496, 505, 505, 504, 
    506, 509, 530, 530, 534, 538, 518, 518, 523, 519, 521, 515, 521]) 
u_a_err = np.array([2, 2, 3, 2, 3, 1, 2, 3, 3, 5, 3, 5, 3, 2, 3, 6, 5, 6, 
    7, 3, 3, 4, 3, 3, 2, 15])
u_e = 296.0/1000
u_e_err = np.array([])
ver = u_a / u_e
# ver_err = np.sqrt((u_a_err/u_e)**2 + (u_a * u_e_err / u_e**2)**2 )
freq_lin = freq[:8]

x = np.linspace(10,300,100000)

popt, pcov = curve_fit(func, np.log10(freq[:5]), np.log10(ver[:5]))# , sigma=ver_err)


plt.plot(freq, ver, label='Messdaten')
plt.plot(x, 10**func(np.log10(x), *popt), label='Fit')

max_v = np.max(ver[20:]) * np.ones(len(freq))
max_sqrt = (np.max(ver[20:])/np.sqrt(2)) * np.ones(len(freq))
# print(np.abs(ys - max_sqrt[0]))

d = 10**func(np.log10(x), *popt) - max_sqrt[0]
a = np.argmin(np.abs(d))
print('Grenzfrequenz: ', x[a])
plt.plot(freq, max_v, label='max')
plt.plot(freq, max_sqrt, label='max_sqrt')




plt.xlabel('Frequenz $f$')
plt.ylabel('Verstärkung $V$')
plt.title('Abb. 2: Frequenzgang bei Kollektorschaltung')
plt.xscale('log')
plt.yscale('log')
plt.legend()
# plt.savefig('fig/kollektor_frequenzgang.pdf')
plt.show()




