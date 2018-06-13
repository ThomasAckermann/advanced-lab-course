import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

# Fit Funktion
def lorentz(omega_, omega_0, gamma, f_0, c):
    return f_0 / (np.sqrt((omega_0**2 - omega_**2)**2 + gamma**2 * omega_**2)) + c

def phase_tan(omega_, omega_0, gamma):
    return np.arctan(gamma * omega_ / (omega_0**2 - omega_**2))

def linear(omega, m, c):
    return omega * m + c

def lorentz_2(omega_, omega_0, gamma, f_0):
    return f_0 / (np.sqrt((omega_0**2 - omega_**2)**2 + gamma**2 * omega_**2)) + 1

# Daten laden
# Gemittelte Werte laden
# omega = np.loadtxt('data/spektrum2500.txt', skiprows=1, unpack=True)[0]
amplitude = np.loadtxt('data/spektrum2500.txt', skiprows=1, unpack=True)[1]
phase = np.loadtxt('data/spektrum2500.txt', skiprows=1, unpack=True)[4]
# Fehler Daten laden
phase_err = np.loadtxt('data/spektrum2500.txt', skiprows=1, unpack=True)[5]
amplitude_err = np.loadtxt('data/spektrum2500.txt', skiprows=1, unpack=True)[2]
omega = np.array([2530.3])
step = 0.3
while (omega[-1] <= 2585):
    omega = np.append(omega, omega[-1] + step)

cos_teil = amplitude * np.cos(phase)
sin_teil = amplitude * np.sin(phase)
# Fit Parameter
popt_lorentz, pcov_lorentz = curve_fit(lorentz, omega, amplitude, p0=[2556, 300, 0.65, 2], sigma=amplitude_err)
popt_linear, pcov_linear = curve_fit(linear, omega[70:-68], cos_teil[70:-68])
# x-Bereich
omega_space = np.linspace(2520, 2600, 5000)
omega_space_linear= np.linspace(2545, 2570, 400)
# Plot für Amplitude
ax1 = plt.subplot(311)
plt.errorbar(omega, amplitude, fmt='.', label='Messdaten', zorder=1)
plt.plot(omega, cos_teil, '.', label='$U_1 = A \cos(\phi)$')
plt.plot(omega, sin_teil, '.', label='$U_2 = A \cos(\phi)$')
# plt.plot(omega_space, lorentz(omega_space, *popt_lorentz))
plt.plot(omega_space_linear, linear(omega_space_linear, *popt_linear), label='Linearer Fit')
plt.legend(loc='upper right')
plt.xlim((2525, 2590))
plt.ylim(-2.5, 5.5)
plt.ylabel('Amplitude [$\mu V$]')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Schwingungsamplitude [3]')

# Plot für Phasendifferenz
ax2 = plt.subplot(312)
plt.errorbar(omega, phase, fmt='.', label='Messdaten')
plt.legend(loc='upper right')
plt.xlim((2525, 2590))
plt.ylim((-0.5, 3.5))
plt.ylabel('Phasendifferenz $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Phasenverschiebung [3]')

# Fit Daten ausgeben
# Schwingungsamplitude
print('Fit Daten für Schwingungsampltiude:')
print('Omega_0: ', popt_lorentz[0], '+/-', np.sqrt(pcov_lorentz[0][0]))
print('Gamma: ', popt_lorentz[2], '+/-', np.sqrt(pcov_lorentz[1][1]))
print('f_0: ', popt_lorentz[1], '+/-', np.sqrt(pcov_lorentz[2][2]))

guete = popt_lorentz[0] / popt_lorentz[1]
delta_guete = np.sqrt((np.sqrt(pcov_lorentz[0][0]) / popt_lorentz[1])**2 + (popt_lorentz[0] * np.sqrt(pcov_lorentz[1][1]) / popt_lorentz[1]**2)**2)
print('Güte Q = ', guete, '+/-', delta_guete)

omega_0 = popt_lorentz[0]
omega_0_err = np.sqrt(pcov_lorentz[0][0])
gamma = popt_lorentz[1]
gamma_err = np.sqrt(pcov_lorentz[1][1])

omega_r = np.sqrt(omega_0**2 - (gamma**2)/2)
omega_r_err = np.sqrt((omega_0 * omega_0_err / np.sqrt(omega_0 - (gamma/2)))**2 + (0.5* gamma * gamma_err / np.sqrt(omega_0**2-(gamma**2/2)))**2)
print('Resonanzfrequenz: ', omega_r, '+/-', omega_r_err)



print('#############################################')
print('linear')

print('Steigung m = ', popt_linear[0], '+/-', np.sqrt(pcov_linear[0][0]))
print('Achsenabschnitt c = ', popt_linear[1], '+/-', np.sqrt(pcov_linear[1][1]))


residuals = (amplitude - lorentz(omega, *popt_lorentz)) / amplitude_err
ax3 = plt.subplot(313)
plt.plot(omega[34:-40], residuals[34:-40], '.')
plt.ylabel('Residual $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Residuals [3]')





plt.tight_layout(pad=0.3, w_pad=0.3, h_pad=0.3)
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/Resonanzkurve_2500.pdf')

print('Resonanzfrequenz 2')
omega_r_2 = - popt_linear[1] / popt_linear[0]
omega_r_2_err = np.sqrt( (np.sqrt(pcov_linear[1][1])/popt_linear[0])**2 + (popt_linear[1]* np.sqrt(pcov_linear[0][0])/(popt_linear[0]**2))**2)
print('Resonanzfrequenz 2: ', omega_r_2, '+/-', omega_r_2_err)





print('############################################')
guete_2 = omega_r_2 / ((np.argmax(cos_teil) - np.argmin(cos_teil)) * step)
guete_2_err = omega_r_2_err / ((np.argmax(cos_teil) - np.argmin(cos_teil)) * step)
print('Guete 2: ', guete_2, '+/-', guete_2_err)

