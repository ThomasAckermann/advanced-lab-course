import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear(x, m, c):
    return m * x + c


channel = np.array([398, 440, 485])
channel_err = np.array([20, 20, 20])
time = np.array([6, 26, 46])


popt, pcov = curve_fit(linear, channel, time, sigma=channel_err)

channel_lin = np.linspace(350, 500, 1000)
plt.errorbar(channel, time, xerr=channel_err, fmt='.', label='Messdaten')
plt.plot(channel_lin, linear(channel_lin, *popt), label='Linear')

plt.legend(loc='lower right')
plt.ylabel('Delayzeit')
plt.xlabel('Channel')
plt.title('Bestimmung der Zeitauflösung')


plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('Plots/Zeitauflösung.pdf')


print('Steigung: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('y-Achsenabschnitt: ', popt[1], '+/-', np.sqrt(pcov[1][1]))




