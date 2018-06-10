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
omega = np.loadtxt('data/data_9.txt', skiprows=1, unpack=True)[0]
amplitude = np.loadtxt('data/data_9.txt', skiprows=1, unpack=True)[1]
# Fehler Daten laden
amplitude_err = np.loadtxt('data/data_9.txt', skiprows=1, unpack=True)[5]

# Fit Parameter
popt_lorentz, pcov_lorentz = curve_fit(lorentz, omega, amplitude, p0=[144, 20, 20])# , sigma=amplitude_err)

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
plt.title('Schwingungsamplitude mit Temperatur von: 35.4°C')

plt.tight_layout()
# f_gcf = plt.gcf()
# f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/Resonanz140_temp9.pdf')

# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Schwingungsampltiude:')
print('Omega_0: ', popt_lorentz[0], '+/-', np.sqrt(pcov_lorentz[0][0]))
print('Gamma: ', popt_lorentz[2], '+/-', np.sqrt(pcov_lorentz[1][1]))
print('f_0: ', popt_lorentz[1], '+/-', np.sqrt(pcov_lorentz[2][2]))
chi2_lorentz = np.sum((lorentz(omega, *popt_lorentz) - amplitude)**2 / amplitude_err**2)
dof_lorentz = len(amplitude) - 3    # Freiheitsgrade
chi2_red_lorentz = chi2_lorentz / dof_lorentz
prob = np.round(1 - chi2.cdf(chi2_lorentz, dof_lorentz), 2) * 100
print('chi2 Lorentz = ', chi2_lorentz)
print('chi2_red Lorentz = ', chi2_red_lorentz)
print('Fit Wahrscheinlichkeit Lorentz: ', prob, '%')
guete = popt_lorentz[0] / popt_lorentz[2]
delta_guete = np.sqrt((np.sqrt(pcov_lorentz[0][0]) / popt_lorentz[2])**2 + (popt_lorentz[0] * np.sqrt(pcov_lorentz[2][2]) / popt_lorentz[2]**2)**2)
print('Güte Q = ', guete, '+/-', delta_guete)



