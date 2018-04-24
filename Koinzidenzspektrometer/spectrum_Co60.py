import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sig):
    return A / (np.sqrt(2 * np.pi) * sig) * np.exp(- (x - mu)**2 / (2 * sig**2))


amplitude, counts = np.loadtxt('Data/Co60.txt', skiprows=1, unpack=True)
counts_err = np.sqrt(counts)

popt, pcov = curve_fit(gaussian, amplitude[517:548], counts[517:548], p0=[1000, 5, 550], sigma=counts_err[517:548])
popt2, pcov2 = curve_fit(gaussian, amplitude[580:610], counts[580:620], p0=[1000, 5, 600], sigma=counts_err[580:610])


ax1 = plt.subplot(211)
plt.plot(amplitude, counts, ',', label='Messdaten')
plt.plot(amplitude[517:548], gaussian(amplitude[517:548], *popt), label='Gauss 1')
plt.plot(amplitude[580:610], gaussian(amplitude[580:610], *popt), label='Gauss 2')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, ',')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
plt.yscale('log')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$ ($\log$)')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/spectrum_Co60.pdf')

print('Maximum 1: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Mittelwert 1: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('Standardabweichung 1: ', popt[2], '+/-', np.sqrt(pcov[2][2]))

print('Maximum 2: ', popt2[0], '+/-', np.sqrt(pcov2[0][0]))
print('Mittelwert 2: ', popt2[1], '+/-', np.sqrt(pcov2[1][1]))
print('Standardabweichung 2: ', popt2[2], '+/-', np.sqrt(pcov2[2][2]))



