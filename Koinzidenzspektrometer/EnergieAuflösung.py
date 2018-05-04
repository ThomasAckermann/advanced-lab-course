import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, m, c):
    return c * np.exp(-1 * m * x)


sigma = np.array([17.6, 19.8, 13.2, 13.7, 10.8, 19.8, 4.1, 14.5, 16.7])
sigma_err = np.array([0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.1, 0.4, 0.8])
fwhm = 2 * np.sqrt(2 * np.log(2)) * sigma
fwhm_err = 2 * np.sqrt(2 * np.log(2)) * sigma_err
fwhm_energy = 0.00226 * fwhm
fwhm_energy_err = np.sqrt((1.68*10**-5 * fwhm)**2 + (0.00226 * fwhm_err)**2)
energy = np.array([1.17323, 1.32248, 0.6616, 0.8358, 0.511, 1.2746, 0.081, 0.302, 0.356])
relative_energy = fwhm_energy / energy
relative_energy_err = fwhm_energy_err / energy

popt, pcov = curve_fit(func, energy[0:-2], relative_energy[0:-2], sigma=relative_energy_err[0:-2])

x = np.linspace(0.08, 1.35, 1000)

plt.errorbar(energy, relative_energy, yerr=relative_energy_err, marker='.', lw=0, label='Messdaten')
plt.plot(x, func(x, *popt), label='Fit')
plt.legend(loc='upper right')
plt.xscale('log')
plt.ylabel('Relative Energie $\\frac{\Delta E}{E}$')
plt.xlabel('Energie $E$')
plt.title('Energie Auflösung')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('Plots/Energie_Aufloesung.pdf')

