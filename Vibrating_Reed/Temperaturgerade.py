import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

# Fit Funktion
def linear(x, a, b):
    return a * x + b

# Daten laden
# Gemittelte Werte laden
omega = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
temperature = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
# Fehler Daten laden
omega_err = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0] 
temperature_err = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0] 


# Fit Parameter
popt, pcov = linear(lorentz, omega, amplitude, sigma=temperature_err)

# x-Bereich
omega_space = np.linspace(120, 150, 4000)

# Plot für Amplitude
plt.errorbar(omega, temperature, xerr=channel_err, yerr=, fmt='.', label='Messdaten')
plt.plot(omega_space, linear(omega_space, *popt), label='Linear-Fit')
plt.legend(loc='lower right')
plt.ylabel('Temperatur [$^\circ C$]')
plt.xlabel('Frequenz [Hz]')
plt.title('Temperaturabhängigkeit der Frequenz')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('fig/Temperatur_Gerade.pdf')

# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Linear-Fit:')
print('Steigung: ', popt[0], '+/-', np.sqrt(pcov[0][0]))
print('Y-Achsenabschnitt: ', popt[1], '+/-', np.sqrt(pcov[1][1]))
chi2 = np.sum((linear(omega, *popt_lorentz) - temperature)**2 / temperature_err**2)
dof = len(temperature) - 2    # Freiheitsgrade
chi2_red = chi2 / dof
prob = np.round(1 - chi2.cdf(chi2, dof), 2) * 100
print('chi2 = ', chi2)
print('chi2_red = ', chi2_red)
print('Fit Wahrscheinlichkeit: ', prob, '%')
