import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear(x, m, c):
    return m * x + c


channel = np.array([530, 596, 310, 386, 242, 572, 42, 145, 165])
channel_err = np.array([2, 2, 2, 2, 2, 2, 2, 2, 10])
energy = np.array([1.17323, 1.32248, 0.6616, 0.8358, 0.511, 1.2746, 0.081, 0.302, 0.356])


popt, pcov = curve_fit(linear, channel, energy, sigma=channel_err)


plt.plot(channel, energy, 'o', label='Messdaten')
plt.plot(channel, linear(channel, *popt), label='Linear')

plt.legend(loc='lower right')
plt.ylabel('Energie [MeV]')
plt.xlabel('Channel')
plt.title('Eichkurve für Energie')


plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('Plots/EichkurveEnergie.pdf')


print('Steigung: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('y-Achsenabschnitt: ', popt[1], '+/-', np.sqrt(pcov[1][1]))




