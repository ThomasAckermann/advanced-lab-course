import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
import os

# Fit Funktion
def lorentz(omega_, omega_0, gamma, f_0):
    return f_0 / (np.sqrt((omega_0**2 - omega_**2)**2 + gamma**2 * omega_**2))



# Daten laden
# Gemittelte Werte laden
omega = np.loadtxt('data/data_7.txt', skiprows=1, unpack=True)[0]
amplitude = np.loadtxt('data/data_7.txt', skiprows=1, unpack=True)[1]
# Fehler Daten laden
amplitude_err = np.loadtxt('data/data_7.txt', skiprows=1, unpack=True)[5]

# Fit Parameter
popt_lorentz, pcov_lorentz = curve_fit(lorentz, omega[78:], amplitude[78:], p0=[144, 20, 20])# , sigma=amplitude_err)

# x-Bereich
omega_space = np.linspace(115, 170, 4000)

# Plot für Amplitude
plt.errorbar(omega, amplitude, fmt='.', label='Messdaten', zorder=1)
plt.plot(omega_space, lorentz(omega_space, *popt_lorentz), label='Lorentz-Fit', zorder=10)
plt.legend(loc='upper right')
plt.xlim((115, 170))
plt.ylim((0,270))
plt.ylabel('Amplitude [$\mu V$]')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Schwingungsamplitude mit Temperatur von: 31.6°C')

plt.tight_layout()
# f_gcf = plt.gcf()
# f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/Resonanz140_temp7.pdf')

# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Schwingungsampltiude:')
print('Omega_0: ', popt_lorentz[0], '+/-', np.sqrt(pcov_lorentz[0][0]))


