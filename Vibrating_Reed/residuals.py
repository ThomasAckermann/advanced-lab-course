import matplotlib.pyplot as plt
import numpy as np


step = 0.1

#################### Residuals 1 #############################################
# Daten laden
amplitude_1 = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[1]
amplitude_1_err = np.loadtxt('data/spektrum140.txt', skiprows=1, unpack=True)[2]
omega_1 = np.array([120.1])
while (omega[-1] <= 160.0):
    omega = np.append(omega, omega[-1] + 0.1)

# Plot für Amplitude
ax1 = plt.subplot(311)
residuals = (amplitude - lorentz(omega, *popt_lorentz)) / amplitude_err
plt.plot(omega[100:], residuals[100:], '.')
plt.ylabel('Residual $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Residuals [1]')




amplitude = np.loadtxt('data/spektrum900.txt', skiprows=1, unpack=True)[1]
amplitude_err = np.loadtxt('data/spektrum900.txt', skiprows=1, unpack=True)[2]
omega = np.array([880.1])
while (omega[-1] <= 930):
    omega = np.append(omega, omega[-1] + 0.1)
print(len(omega))
# print(len(amplitude)) 

residuals = (amplitude - lorentz(omega, *popt_lorentz)) / amplitude_err
ax2 = plt.subplot(312)
plt.plot(omega[200:-180:5], residuals[200:-180:5], '.')
plt.ylabel('Residual $\Delta \phi$')
plt.xlabel('Frequenz $\omega$ [Hz]')
plt.title('Residuals [1]')






plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('fig/residuals.pdf')


