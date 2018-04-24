import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sig):
    return A / (np.sqrt(2 * np.pi) * sig) * np.exp(- (x - mu)**2 / (2 * sig**2))


amplitude, counts = np.loadtxt('Data/Mn54.txt', skiprows=1, unpack=True)
counts_err = np.sqrt(counts)

popt, pcov = curve_fit(gaussian, amplitude[517:548], counts[517:548], p0=[1000, 5, 550], sigma=counts_err[517:548])


ax1 = plt.subplot(211)
plt.plot(amplitude, counts, ',', label='Messdaten')
plt.plot(amplitude[517:548], gaussian(amplitude[517:548], *popt), label='Gauss')
plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Mn^{54}$')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, ',')
plt.yscale('log')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Mn^{54}$ ($\log$)')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/spectrum_Mn54.pdf')

print('Maximum: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Mittelwert: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('Standardabweichung: ', popt[2], '+/-', np.sqrt(pcov[2][2]))




