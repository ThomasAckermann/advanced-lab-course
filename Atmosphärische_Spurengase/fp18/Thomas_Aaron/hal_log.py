import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.size'] = 28
rcParams['text.usetex'] = True

data = np.loadtxt('log_1.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x[1:], y[1:], 'ks', markersize=2)
plt.xlabel('Wellenlänge [nm]')
plt.ylabel('Optische Dichte')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('hal_log.pdf')
