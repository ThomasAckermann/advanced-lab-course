import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Linux Biolinum']
# rcParams['font.size'] = 20
rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = '\usepackage{libertine}'

data = np.loadtxt('test_7.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x, y, 'ks', markersize=0.5)
plt.xlabel('Wellenlänge [nm]')
plt.ylabel('Intensität')
plt.savefig('test_spektrum.pdf')
