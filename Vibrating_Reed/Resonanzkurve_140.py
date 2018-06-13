import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
import os

# Fit Funktion
def lorentz(omega_, omega_0, gamma, f_0):
    return f_0 / (np.sqrt((omega_0**2 - omega_**2)**2 + gamma**2 * omega_**2))

def phase_tan(f, f_0, a, b, c):
    return a * np.arctan((f - f_0) / b) + c

def linear(omega, m, c):
    return omega * m + c

# Daten laden
# Gemittelte Werte laden
# omega = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[0]
amplitude = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[1]
phase = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[4]
# Fehler Daten laden
phase_err = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[5]
amplitude_err = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[2]
cos_teil = amplitude * np.cos(phase)
sin_teil = amplitude * np.sin(phase)
omega = np.array([120.1])
step = 0.1
while (omega[-1] <= 160.0):
    omega = np.append(omega, omega[-1] + 0.1)
# print(len(omega))
# print(len(amplitude)) 
# Fit Parameter
popt_lorentz, pcov_lorentz = curve_fit(lorentz, omega, amplitude, p0=[144, 20, 20], sigma=amplitude_err)
popt_phase, pcov_phase = curve_fit(phase_tan, omega[100:], phase[100:], p0=[142, 4, 1.3, 1],sigma=phase_err[100:])
popt_linear, pcov_linear = curve_fit(linear, omega[180:-130], cos_teil[180:-130])
# x-Bereich
omega_space = np.linspace(120, 170, 4000)
omega_space_linear = np.linspace(137, 150, 100)
# Plot für Amplitude
ax1 = plt.subplot(311)
plt.errorbar(omega, amplitude, fmt='.', label='Messdaten', zorder=1)
plt.plot(omega_space, lorentz(omega_space, *popt_lorentz), label='Lorentz-Fit', zorder=10)
plt.plot(omega, cos_teil, '.', label='$U_1 = A \cos (\\varphi)$')
plt.plot(omega, sin_teil, '.', label='$U_1 = A \sin (\\varphi)$')
plt.plot(omega_space_linear, linear(omega_space_linear, *popt_linear), label='Linearer Fit')
plt.legend(loc='upper right')
plt.xlim((128, 160))
plt.ylim(-110,270)
plt.ylabel('Amplitude [$\mu V$]')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Schwingungsamplitude [1]')
# plt.plot(omega_space, lorentz(omega_space, *popt_lorentz), label='Lorentz-Fit')
# Plot für Phasendifferenz
ax2 = plt.subplot(312)
plt.errorbar(omega, phase, fmt='.', label='Messdaten')
plt.plot(omega_space, phase_tan(omega_space, *popt_phase), label='Phase-Fit', zorder=10)
plt.legend(loc='lower right')
plt.xlim((120, 160))
plt.ylim((0, 3.5))
plt.ylabel('Phasendifferenz $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Phasenverschiebung [1]')

print('############################################')
# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Schwingungsampltiude:')
print('Omega_0: ', popt_lorentz[0], '+/-', np.sqrt(pcov_lorentz[0][0]))
print('Gamma: ', popt_lorentz[1], '+/-', np.sqrt(pcov_lorentz[1][1]))
print('f_0: ', popt_lorentz[2], '+/-', np.sqrt(pcov_lorentz[2][2]))
chi2_lorentz = np.sum((lorentz(omega, *popt_lorentz) - amplitude)**2 / amplitude_err**2)
dof_lorentz = len(amplitude) - 3    # Freiheitsgrade
chi2_red_lorentz = chi2_lorentz / dof_lorentz
prob = np.round(1 - chi2.cdf(chi2_lorentz, dof_lorentz), 2) * 100
print('chi2 Lorentz = ', chi2_lorentz)
print('chi2_red Lorentz = ', chi2_red_lorentz)
print('Fit Wahrscheinlichkeit Lorentz: ', prob, '%')
guete = popt_lorentz[0] / popt_lorentz[1]
delta_guete = np.sqrt((np.sqrt(pcov_lorentz[0][0]) / popt_lorentz[1])**2 + (popt_lorentz[0] * np.sqrt(pcov_lorentz[1][1]) / popt_lorentz[1]**2)**2)
print('Guete Q = ', guete, '+/-', delta_guete)


print('############################################')

# Phasenverschiebung
print('Fit Daten für Phasenverschiebung')
print('Omega_0: ', popt_phase[0], '+/-', np.sqrt(pcov_phase[0][0]))
print('Gamma: ', popt_phase[1], '+/-', np.sqrt(pcov_phase[1][1]))
chi2_tan = np.sum((phase_tan(omega[100:], *popt_phase) - phase[100:])**2 / phase_err[100:]**2)
dof_tan = len(phase) - 4    # Freiheitsgrade
chi2_red_tan = chi2_tan / dof_tan
prob = np.round(1 - chi2.cdf(chi2_tan, dof_tan), 2) * 100
print('chi2 Lorentz = ', chi2_tan)
print('chi2_red Arctan = ', chi2_red_tan)
print('Fit Wahrscheinlichkeit Arctan: ', prob, '%')
print('############################################')
omega_0 = popt_lorentz[0]
omega_0_err = np.sqrt(pcov_lorentz[0][0])
gamma = popt_lorentz[1]
gamma_err = np.sqrt(pcov_lorentz[1][1])

omega_r = np.sqrt(omega_0**2 - (gamma**2)/2)
omega_r_err = np.sqrt((omega_0 * omega_0_err / np.sqrt(omega_0 - (gamma/2)))**2 + (0.5* gamma * gamma_err / np.sqrt(omega_0**2-(gamma**2/2)))**2)
print('Resonanzfrequenz: ', omega_r, '+/-', omega_r_err)

print('#############################################')
print('linear')

print('Steigung m=', popt_linear[0], '+/-', np.sqrt(pcov_linear[0][0]))
print('Achsenabschnitt c=', popt_linear[1], '+/-', np.sqrt(pcov_linear[1][1]))


residuals = (amplitude - lorentz(omega, *popt_lorentz)) / amplitude_err
ax3 = plt.subplot(313)
plt.plot(omega[100:], residuals[100:], '.')
plt.ylabel('Residual $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Residuals [1]')

plt.tight_layout(pad=0.0, w_pad=0.0, h_pad=0.0)
# plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/Resonanzkurve_140.pdf')


print('############################################')
guete_2 = omega_r / ((np.argmax(cos_teil) - np.argmin(cos_teil)) * step)
guete_2_err = omega_r_err / ((np.argmax(cos_teil) - np.argmin(cos_teil)) * step)
print('Guete 2: ', guete_2, '+/-', guete_2_err)


print('Resonanzfrequenz 2')
omega_r_2 = - popt_linear[1] / popt_linear[0]
omega_r_2_err = np.sqrt( (np.sqrt(pcov_linear[1][1])/popt_linear[0])**2 + (popt_linear[1]* np.sqrt(pcov_linear[0][0])/(popt_linear[0]**2))**2)
print('Resonanzfrequenz 2: ', omega_r_2, '+/-', omega_r_2_err)
