import numpy as np
import matplotlib.pyplot as plt


amplitude, counts = np.loadtxt('Data/Nachtmessung.txt', skiprows=1, unpack=True)
counts_err = np.sqrt(counts)



ax1 = plt.subplot(211)
plt.plot(amplitude, counts, '.')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Nachtmessung')


ax2 = plt.subplot(212)
plt.plot(amplitude, counts, '.')
plt.yscale('log')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Nachtmessung ($\log$)')
plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)


# plt.savefig('Plots/Nachtmessung.pdf')
plt.show()

