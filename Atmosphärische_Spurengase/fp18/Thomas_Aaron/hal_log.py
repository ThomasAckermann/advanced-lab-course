import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Linux Biolinum']
# rcParams['font.size'] = 20
rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = '\usepackage{libertine}'

data = np.loadtxt('log_1.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x[1:], y[1:], 'ks', markersize=2)
plt.xlabel('Channels')
plt.ylabel('Optical Density')
plt.savefig('hal_log.pdf')
