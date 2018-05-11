import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sig):
    return A / (np.sqrt(2 * np.pi) * sig) * np.exp(- (x - mu)**2 / (2 * sig**2))


untergr_x, untergr_y = np.loadtxt('Data/Nachtmessung.txt', skiprows=1, unpack=True)
amplitude, counts = np.loadtxt('Data/Co60.txt', skiprows=1, unpack=True)
untergr_y = untergr_y * 420 / 72202
for i in range(100):
    untergr_y = np.append(untergr_y, 87)
counts = counts - untergr_y

counts_err = np.sqrt(counts)
x1 = np.linspace(500, 560, 1000)
x2 = np.linspace(560, 640, 1000)

popt, pcov = curve_fit(gaussian, amplitude[517:550], counts[517:550], p0=[1000, 550, 5], sigma=counts_err[517:550])
popt2, pcov2 = curve_fit(gaussian, amplitude[570:620], counts[570:620], p0=[800, 600, 10], sigma=counts_err[570:620])


ax1 = plt.subplot(211)
plt.plot(amplitude, counts, 'o', label='Messdaten')
plt.plot(x1, gaussian(x1, *popt), 'o', label='Gauss 1')
plt.plot(x2, gaussian(x2, *popt2), 'o', label='Gauss 2')
plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, 'o')
plt.yscale('log')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$ ($\log$)')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
# plt.savefig('Plots/spectrum_Co60.pdf')
plt.show()
print('A 1: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Mittelwert 1: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
print('Standardabweichung 1: ', popt[2], '+/-', np.sqrt(pcov[2][2]))

print('A 1: ', popt2[0], '+/-', np.sqrt(pcov2[0][0]))
print('Mittelwert 2: ', popt2[1], '+/-', np.sqrt(pcov2[1][1]))
print('Standardabweichung 2: ', popt2[2], '+/-', np.sqrt(pcov2[2][2]))



