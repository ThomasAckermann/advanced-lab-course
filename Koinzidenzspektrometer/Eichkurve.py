import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear(x, m, c):
    return m * x + c


amplitude, counts = np.loadtxt('Data/Co60.txt', skiprows=1, unpack=True)
counts_err = np.sqrt(counts)

popt, pcov = curve_fit(linear, amplitude[517:548], counts[517:548], sigma=counts_err[517:548])


plt.plot(amplitude, counts, ',', label='Messdaten')
plt.plot(amplitude[517:548], linear(amplitude[517:548], *popt), label='Linear')

plt.legend(loc='lower right')
plt.ylabel('Energie')
plt.xlabel('Amplitude')
plt.title('Eichkurve')


plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('Plots/Eichkurve.pdf')


print('Steigung: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('y-Achsenabschnitt: ', popt[2], '+/-', np.sqrt(pcov[2][2]))




