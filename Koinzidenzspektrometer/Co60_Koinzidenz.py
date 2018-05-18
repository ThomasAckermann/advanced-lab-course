import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# load data
amplitude1, counts1 = np.loadtxt('Data/Co60_Zeitspektrum.txt', skiprows=1, unpack=True)
amplitude2, counts2 = np.loadtxt('Data/Co60_Koinzidenz.txt', skiprows=1, unpack=True)
amplitude3, counts3 = np.loadtxt('Data/Beweis_Kaskade.txt', skiprows=1, unpack=True)
counts_err1 = np.sqrt(counts1)
counts_err2 = np.sqrt(counts2)
counts_err3 = np.sqrt(counts3)

ax1 = plt.subplot(311)
plt.plot(amplitude1, counts1, '.')
plt.ylabel('Counts')
plt.xlabel('Zeit [ns]')
plt.title('Zeitspektrum $Co^{60}$')

summe = sum(counts1[500:])
print('Summe:', summe)

ax2 = plt.subplot(312)
plt.plot(amplitude2, counts2, '.')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Koinzidenzspektrum verbesssert $Co^{60}$')

ax2 = plt.subplot(313)
plt.plot(amplitude3, counts3, '.')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Beweis Kaskadenzerfall $Co^{60}$')

plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/Co60Koinzidenz.pdf')
