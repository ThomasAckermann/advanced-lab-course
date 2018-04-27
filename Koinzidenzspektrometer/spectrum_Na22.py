import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sig):
    return A / (np.sqrt(2 * np.pi) * sig) * np.exp(- (x - mu)**2 / (2 * sig**2))


untergr_x, untergr_y = np.loadtxt('Data/Nachtmessung.txt', skiprows=1, unpack=True)
amplitude, counts = np.loadtxt('Data/Na22.txt', skiprows=1, unpack=True)
untergr_y = untergr_y * 420 / 72202
print(len(counts), len(untergr_y))

counts = counts - untergr_y

counts_err = np.sqrt(counts)
x = np.linspace(200, 280, 1000)

popt, pcov = curve_fit(gaussian, amplitude[220:260], counts[220:260], p0=[1500, 240, 5], sigma=counts_err[220:260])


ax1 = plt.subplot(211)
plt.plot(amplitude, counts, ',', label='Messdaten')
plt.plot(x, gaussian(x, *popt), label='Gaussfit')
plt.legend(loc='upper right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Na^{22}$')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, ',')
plt.yscale('log')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Na^{22}$ ($\log$)')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/spectrum_Na22.pdf')

print('A 1: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Mittelwert 1: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('Standardabweichung 1: ', popt[2], '+/-', np.sqrt(pcov[2][2]))




