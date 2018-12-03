import numpy as np
import matplotlib.pyplot as plt


data_1 = np.loadtxt('data/multi_bins_opt.txt', unpack=True)
data_2 = np.loadtxt('data/multi_bins_-10.txt', unpack=True)
data_3 = np.loadtxt('data/multi_bins_5.txt', unpack=True)



ax1 = plt.subplot(111)
ax1.plot(data_1[0], data_1[1], '.', label='var=opt')
ax1.set_ylabel('Mutual Information')
ax1.set_xlabel('Bin Anzahl')
# plt.tick_params('y')
# ax1.title('Multimodal unterschiedliche Bins')
ax2 = plt.subplot(111)
ax2.plot(data_2[0], data_2[1], '.', label='var=-10')
ax2.set_ylabel('Mutual Information')
ax2.set_xlabel('Bin Anzahl')
ax3 = plt.subplot(111)
ax3.plot(data_3[0], data_3[1], '.', label='var=5')
ax3.set_ylabel('Mutual Information')
ax3.set_xlabel('Bin Anzahl')



plt.legend()
plt.tight_layout()
plt.show()
