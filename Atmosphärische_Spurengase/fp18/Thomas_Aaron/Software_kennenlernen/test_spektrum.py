import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Linux Biolinum']
rcParams['font.size'] = 24
rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = '\usepackage{libertine}'

data = np.loadtxt('test_7.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x, y, 'ks', markersize=0.5)
plt.xlabel('Wellenlänge [nm]')
plt.ylabel('Intensität [counts]')

f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
plt.savefig('test_spektrum.pdf')
