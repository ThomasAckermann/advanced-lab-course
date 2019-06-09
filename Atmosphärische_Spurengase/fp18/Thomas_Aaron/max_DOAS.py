import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.size'] = 15
rcParams['text.usetex'] = True

angle = np.array([7, 12])

#
# ======== Daten laden  ========
# 
# ========  Messung 1 ========
O3_1 = np.array([1.09 * 10**18, 7.5 * 10**17])
O3_1_error = np.array([5.9 * 10**16, 5.12 * 10**16])
NO2_1 = np.array([5.72 * 10**16, 4.92 * 10**16])
NO2_1_error = np.array([5.5236 * 10**14, 5.39 * 10**14])
O4_1 = np.array([3.41 * 10**43, 2.80 * 10**43])
O4_1_error = np.array([8.08 * 10**41, 3.83 * 10**42])
# ========  Messung 2 ========
O3_2 = np.array([6.21 * 10**17, 3.23 * 10**17])
O3_2_error = np.array([6.78 * 10**16, 7.61 * 10**16])
NO2_2 = np.array([2.77 * 10**16, 1.45 * 10**16])
NO2_2_error = np.array([6.31 * 10**14, 6.10 * 10**14])
O4_2 = np.array([2.79 * 10**43, 1.35 * 10**43])
O4_2_error = np.array([2.07 * 10**42, 1.97 * 10**42])
# ========  Messung 3 ========
O3_3 = np.array([6.01 * 10**17, 3.51 * 10**17])
O3_3_error = np.array([7.20 * 10**16, 6.94 * 10**16])
NO2_3 = np.array([2.24 * 10**16, 1.10 * 10**16])
NO2_3_error = np.array([5.85 * 10**14, 5.37 * 10**14])
O4_3 = np.array([2.69 * 10**43, 9.36 * 10**42])
O4_3_error = np.array([1.95 * 10**42, 4.43 * 10**41])
# ========  Messung 4 ========
O3_4 = np.array([8.81*10**17, 7.53*10**17])
O3_4_error = np.array([7.16*10**16, 7.60*10**16])
NO2_4 = np.array([2.6*10**16, 2.00*10**16])
NO2_4_error = np.array([5.13*10**14, 4.75*10**14])
O4_4 = np.array([2.81*10**43, 1.9*10**43])
O4_4_error = np.array([3.52*10**41, 3.361*10**41])

o3_list = np.array([O3_1, O3_2, O3_3, O3_4])
print(np.array(o3_list)[:,0])
mean_o3_7 = np.mean(o3_list[:,0])
mean_o3_12 = np.mean(o3_list[:,0])
o3_ratio = mean_o3_7 / mean_o3_12
o3_ratio_err = np.sqrt((np.std(o3_list[:,0])/mean_o3_12)**2 + (mean_o3_7 * np.std(o3_list[:,1]) / mean_o3_12**2)**2)
print('Verhältnis O_3: ', o3_ratio, '+-', o3_ratio_err)


no2_list = np.array([NO2_1, NO2_2, NO2_3, NO2_4])
mean_no2_7 = np.mean(no2_list[:,0])
mean_no2_12 = np.mean(no2_list[:,1])
no2_ratio = mean_no2_7 / mean_no2_12
no2_ratio_err = np.sqrt((np.std(no2_list[:,0])/mean_no2_12)**2 + (mean_no2_7 * np.std(no2_list[:,1]) / mean_no2_12**2)**2)
print('Verhältnis NO_2: ', no2_ratio, '+-', no2_ratio_err)

o4_list = np.array([O4_1, O4_2, O4_3, O4_4])
mean_o4_7 = np.mean(o4_list[:,0])
mean_o4_12 = np.mean(o4_list[:,1])
o4_ratio = mean_o4_7 / mean_o4_12
o4_ratio_err = np.sqrt((np.std(o4_list[:,0])/mean_o4_12)**2 + (mean_o4_7 * np.std(o4_list[:,1]) / mean_o4_12**2)**2)
print('Verhältnis O_4: ', o4_ratio, '+-', o4_ratio_err)




plt.figure(1)
plt.errorbar(angle, O3_1, yerr=O3_1_error, fmt='.', markersize=11,label='Messung 1')
plt.errorbar(angle, O3_2, yerr=O3_2_error, fmt='.', markersize=11, label='Messung 2')
plt.errorbar(angle, O3_3, yerr=O3_3_error, fmt='.', markersize=11, label='Messung 3')
plt.errorbar(angle, O3_4, yerr=O3_4_error, fmt='.', markersize=11, label='Messung 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O$_3$')
plt.legend()
f = plt.gcf()
# f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_O3.pdf')
# plt.show()
print('saved figure')
plt.figure(2)
plt.errorbar(angle, NO2_1, yerr=NO2_1_error, fmt='.', markersize=11, label='Messung 1')
plt.errorbar(angle, NO2_2, yerr=NO2_2_error, fmt='.', markersize=11, label='Messung 2')
plt.errorbar(angle, NO2_3, yerr=NO2_3_error, fmt='.', markersize=11, label='Messung 3')
plt.errorbar(angle, NO2_4, yerr=NO2_4_error, fmt='.', markersize=11, label='Messung 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO$_2$')
plt.legend()
f = plt.gcf()
# f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_NO2.pdf')
# plt.show()
print('saved figure')
plt.figure(3)
plt.errorbar(angle, O4_1, yerr=O4_1_error, fmt='.', markersize=11, label='Messung 1')
plt.errorbar(angle, O4_2, yerr=O4_2_error, fmt='.', markersize=11, label='Messung 2')
plt.errorbar(angle, O4_3, yerr=O4_3_error, fmt='.', markersize=11, label='Messung 3')
plt.errorbar(angle, O4_4, yerr=O4_4_error, fmt='.', markersize=11, label='Messung 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
plt.legend()
f = plt.gcf()
# f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_O4.pdf')
# plt.show()
print('saved figure')


