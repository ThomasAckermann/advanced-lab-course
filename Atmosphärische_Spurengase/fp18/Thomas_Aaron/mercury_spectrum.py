import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import rcParams

rcParams['font.size'] = 28
rcParams['text.usetex'] = True

data = np.loadtxt('hg_data.txt')
x = data[:,0]
y = data[:,1]

plt.plot(x,y, 'ks', markersize=3)
plt.xlabel('Wellenlänge [nm]')
plt.ylabel('Intensität [counts]')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
f_gcf = plt.gcf()
f_gcf.set_size_inches(11.69, 8.27)
# plt.show()
plt.savefig('hg_spectrum.pdf')
