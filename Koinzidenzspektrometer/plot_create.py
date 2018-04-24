import matplotlib.pyplot as plt
import numpy as np


counts = np.loadtxt('Data/PFADEINFÜGEN.txt', usecols=[0])
amplitude = np.loadtxt('Data/PFADEINFÜGEN.txt', usecols=[1])

counts_err = np.sqrt(counts)
amplitude_err = 0


ax1 = plt.subplot(111)
plt.errorbar(counts, amplitude, xerr=counts_err, yerr=amplitude_err, fmt=',')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('TITEL EINFÜGEN')


ax2 = plt.subplot(112)
plt.errorbar(counts, amplitude, xerr=counts_err, yerr=amplitude_err, fmt=',')
# plt.plot(counts, amplitude, 'r-', label='Fit', color='black')
ax2.yscale('log')
plt.legend(loc='lower right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('TITEL EINFÜGEN')

plt.savefig('Data/plot_create.pdf')