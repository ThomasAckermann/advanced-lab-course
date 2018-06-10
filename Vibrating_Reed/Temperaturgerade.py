import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

# Fit Funktion
def linear(x, a, b):
    return a * x + b

temperature = np.array([25.3, 26.1, 27.1, 28.1, 29.1, 30.3, 31.6, 33.0, 35.4, 43.7, 45.0])
omega_0 = np.array([143.741, 143.760, 143.713, 143.664, 143.663, 143.625, 143.587, 143.523, 143.463, 143.410, 143.387])
omega_0_err = np.array([0.021, 0.022, 0.021, 0.021, 0.021, 0.021, 0.020, 0.021, 0.022, 0.021, 0.027])
# Fit Parameter
popt, pcov = curve_fit(linear, temperature, omega_0, sigma=omega_0_err)
# x-Bereich
omega_space = np.linspace(25.3, 45.0, 4000)

# Plot für Amplitude
plt.errorbar(temperature, omega_0, fmt='.', label='Messdaten')
plt.plot(omega_space, linear(omega_space, *popt), label='Linear-Fit')
plt.legend(loc='upper right')
plt.xlabel('Temperatur [$^\circ C$]')
plt.ylabel('Frequenz [Hz]')
plt.title('Temperaturabhängigkeit der Frequenz')

plt.tight_layout()
# f_gcf = plt.gcf()
# f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('fig/Temperatur_Gerade.pdf')

# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Linear-Fit:')
print('Steigung: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Y-Achsenabschnitt: ', popt[1], '+/-', np.sqrt(pcov[1][1]))

