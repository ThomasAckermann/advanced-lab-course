import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sig):
    return A / (np.sqrt(2 * np.pi) * sig) * np.exp(- (x - mu)**2 / (2 * sig**2))


untergr_x, untergr_y = np.loadtxt('Data/Nachtmessung.txt', skiprows=1, unpack=True)
amplitude, counts = np.loadtxt('Data/Cs137.txt', skiprows=1, unpack=True)

summe = np.sum(counts)

untergr_y = untergr_y * 420 / 72202
for i in range(100):
    untergr_y = np.append(untergr_y, 0)
counts = counts - untergr_y

counts_err = np.sqrt(counts)
x = np.linspace(280, 350, 1000)

popt, pcov = curve_fit(gaussian, amplitude[290:340], counts[290:340], p0=[1000, 300, 5], sigma=counts_err[290:340])


ax1 = plt.subplot(211)
plt.plot(amplitude, counts, 'o', label='Messdaten')
plt.plot(x, gaussian(x, *popt), 'o', label='Gaussfit')
plt.legend(loc='upper right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Cs^{137}$')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, 'o')
plt.yscale('log')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Cs^{137}$ ($\log$)')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
# plt.savefig('Plots/spectrum_Cs137.pdf')
plt.show()
print('A 1: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Mittelwert 1: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('Standardabweichung 1: ', popt[2], '+/-', np.sqrt(pcov[2][2]))

print('Summe der Ereignisse: ', summe)
