import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, c):
    return m * x + c


pixel = np.array([0.9978, 2.9958, 3.2373, 5.1319, 1.5980, 1.8935, 3.8962, 0.3207,
1.8609, 1.1844])
cm = np.array([0.5, 1.1, 1.3, 1.9, 0.6, 0.8, 1.4, 0.2, 0.8, 0.6])
delta_cm = 0.1 * np.ones(len(cm))


popt, pcov = curve_fit(linear, pixel, cm, sigma=delta_cm)
plt.errorbar(pixel, cm, yerr=delta_cm, fmt='.')
plt.plot(pixel, linear(pixel, *popt), label='Linear')

print("Steigung: ", popt[0], " +/- ", np.sqrt(pcov[0][0]))
print("Y-Achsenabschnitt: ", popt[1], " +/- ", np.sqrt(pcov[1][1]))

plt.show()

