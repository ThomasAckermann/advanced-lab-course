import numpy as np
import matplotlib.pyplot as plt

angle = np.array([7, 12])

#
# ======== Daten laden  ========
# 
# ========  Messung 1 ========
O3_1 = np.array([1.07 * 10**18, 7. * 10**17])
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


plt.figure(1)
plt.errorbar(angle, O3_1, yerr=O3_1_error, fmt='.', label='Messung 1')
plt.errorbar(angle, O3_2, yerr=O3_2_error, fmt='.', label='Messung 2')
plt.errorbar(angle, O3_3, yerr=O3_3_error, fmt='.', label='Messung 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O$_3$')
plt.legend()
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_O3.pdf')
# plt.show()
print('saved figure')
plt.figure(2)
plt.errorbar(angle, NO2_1, yerr=NO2_1_error, fmt='.', label='Messung 1')
plt.errorbar(angle, NO2_2, yerr=NO2_2_error, fmt='.', label='Messung 2')
plt.errorbar(angle, NO2_3, yerr=NO2_3_error, fmt='.', label='Messung 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO$_2$')
plt.legend()
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_NO2.pdf')
# plt.show()
print('saved figure')
plt.figure(3)
plt.errorbar(angle, O4_1, yerr=O4_1_error, fmt='.', label='Messung 1')
plt.errorbar(angle, O4_2, yerr=O4_2_error, fmt='.', label='Messung 2')
plt.errorbar(angle, O4_3, yerr=O4_3_error, fmt='.', label='Messung 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
plt.legend()
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.savefig('max_DOAS_O4.pdf')
# plt.show()
print('saved figure')


