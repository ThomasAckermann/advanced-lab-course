import numpy as np
import matplotlib.pyplot as plt

data_1 = np.loadtxt('data/mono_trans_1.txt', unpack=True)
data_2 = np.loadtxt('data/mono_rot_1.txt', unpack=True)


ax1 = plt.subplot(211)
ax1.plot(data_1[0], data_1[1], 'b.')
ax1.set_ylabel('Mutual Information', color='b')
ax1.set_xlabel('Parameter')
ax1.tick_params('y')
# ax1.title('Monomodal Translation')
ax2 = ax1.twinx()
ax2.plot(data_1[0], data_1[2], 'r.')
ax2.set_ylabel('SSD', color='r')
ax2.tick_params('y')
plt.tight_layout()



ax3 = plt.subplot(212)
ax3.plot(data_2[0], data_2[1], 'b.')
ax3.set_ylabel('Mutual Information', color='b')
ax3.set_xlabel('Parameter')
ax3.tick_params('y')
# ax3.title('Monomodal Rotation')
ax4 = ax3.twinx()
ax4.plot(data_2[0], data_2[2], 'r.')
ax4.set_ylabel('SSD', color='r')
ax4.tick_params('y')
plt.tight_layout()
plt.show()



  
