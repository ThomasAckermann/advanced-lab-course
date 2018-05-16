import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# load data
amplitude1, counts1 = np.loadtxt('Data/Cs137_SCA.txt', skiprows=1, unpack=True)
amplitude2, counts2 = np.loadtxt('Data/Cs137_1Peak.txt', skiprows=1, unpack=True)
counts_err1 = np.sqrt(counts1)
counts_err2 = np.sqrt(counts2)


ax1 = plt.subplot(211)
plt.plot(amplitude1, counts1, '.')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Koinzidenzspektrum verbessert $Cs^{137}$')
ax2 = plt.subplot(212)
plt.plot(amplitude2, counts2, '.')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Beweis Compton Streuprozess$Cs^{137}$')


plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/Cs137Koinzidenzspektrum.pdf')


