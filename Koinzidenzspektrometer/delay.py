import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


time1, counts1 = np.loadtxt('Data/delay1.txt', skiprows=1, unpack=True)
time2, counts2 = np.loadtxt('Data/delay1.txt', skiprows=1, unpack=True)
time3, counts3 = np.loadtxt('Data/delay1.txt', skiprows=1, unpack=True)



ax1 = plt.subplot(311)
plt.plot(time1, counts1, '.', label='Messdaten')
plt.legend(loc='upper right')
plt.ylabel('Counts')
plt.xlabel('Delay [ns]')
plt.title('Delay 1')

ax2 = plt.subplot(312)
plt.plot(time2, counts2, '.')
plt.ylabel('Counts')
plt.xlabel('Delay [ns]')
plt.title('Delay 2')

ax3 = plt.subplot(313)
plt.plot(time3, counts3, '.')
plt.ylabel('Counts')
plt.xlabel('Delay [ns]')
plt.title('Delay 3')


plt.tight_layout()
f_gcf = plt.gcf()
f_gcf.set_size_inches(8.27, 11.69)
# plt.savefig('Plots/delay.pdf')
plt.show()

