import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

# Fit Funktion
def lorentz(omega_, omega_0, gamma, f_0):
    return f_0 / (np.sqrt((omega_0**2 - omega_**2)**2 + gamma**2 * omega_**2))

def phase_tan(omega_, omega_0, gamma):
    return gamma * omega_ / (omega_0**2 + omega_**2)


# Daten laden
# Gemittelte Werte laden
omega = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
amplitude = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
phase = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
# Fehler Daten laden
phase_err = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0]
amplitude_err = np.loadtxt('data/PFADEINGEBEN.txt', skiprows=1, unpack=True)[0] 


# Fit Parameter
popt_lorentz, pcov_lorentz = curve_fit(lorentz, omega, amplitude, sigma=amplitude_err)
popt_phase, pcov_phase = curve_fit(phase_tan, omega, phase, sigma=phase_err)

# x-Bereich
omega_space = np.linspace(120, 150, 4000)

# Plot für Amplitude
ax1 = plt.subplot(211)
plt.errorbar(omega, amplitude, xerr=channel_err, fmt='.', label='Messdaten')
plt.plot(omega_space, lorentz(omega_space, *popt_lorentz), label='Lorentz-Fit')
plt.legend(loc='lower right')
plt.ylabel('Amplitude [$\mu V$]')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Schwingungsamplitude [1]')

# Plot für Phasendifferenz
ax2 = plt.subplot(212)
plt.errorbar(omega, phase, xerr=channel_err, fmt='.', label='Messdaten')
plt.plot(omega_space, phase_tan(omega_space, *popt_phase), label='Phase-Fit')
plt.legend(loc='lower right'


plt.ylabel('Phasendifferenz$\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Phasenverschiebung [1]')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/Resonanzkurve_140.pdf')

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



# Phasenverschiebung
print('Fit Daten für Phasenverschiebung')
print('Omega_0: ', popt_phase[0], '+/-', np.sqrt(pcov_phase[0][0]))
print('Gamma: ', popt_phase[1], '+/-', np.sqrt(pcov_phase[1][1]))
chi2_phase = np.sum((phase_tan(omega, *popt_phase) - )**2 / phase_err**2)
dof_lorentz = len(phase) - 2    # Freiheitsgrade
chi2_red_lorentz = chi2_lorentz / dof_lorentz
prob = np.round(1 - chi2.cdf(chi2_lorentz, dof_lorentz), 2) * 100
print('chi2 Lorentz = ', chi2_lorentz)
print('chi2_red Lorentz = ', chi2_red_lorentz)
print('Fit Wahrscheinlichkeit Lorentz: ', prob, '%')



