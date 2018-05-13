import matplotlib.pyplot as plt
import numpy as np
untergr_x, untergr_y = np.loadtxt('Data/Nachtmessung.txt', skiprows=1, unpack=True)
amplitude, counts = np.loadtxt('Data/CS137_SCA.txt', skiprows=1, unpack=True)


plt.plot(amplitude, counts, '.', label='Messdaten')

plt.legend(loc='upper right')
plt.ylabel('Counts')
plt.xlabel('Amplitude')
plt.title('Pulshöhenspektrum $Cs^{137}$')
plt.tight_layout()
# f_gcf = plt.gcf()
# f_gcf.set_size_inches(8.27, 11.69)
plt.savefig('Plots/spectrum_Cs137_sca.pdf')

