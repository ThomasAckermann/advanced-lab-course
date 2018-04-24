import matplotlib.pyplot as plt
import numpy as np


counts, amplitude = np.loadtxt('Data/Co60.txt', skiprows=1, unpack=True)

counts_err = np.sqrt(counts)
amplitude_err = 0


ax1 = plt.subplot(211)
plt.plot(counts, amplitude, ',')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$')


ax2 = plt.subplot(212)
plt.plot(counts, amplitude, ',')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
plt.yscale('log')
# plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Co^{60}$ ($\log$)')

plt.tight_layout()
plt.savefig('Plots/spectrum_Co60.pdf')