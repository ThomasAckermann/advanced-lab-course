import numpy as np
import matplotlib.pyplot as plt

angle = np.array([7, 12])

#Set 1

O3_1 = np.array([1.07 * 10**18, 7. * 10**17])
O3_1_error = np.array([5.9 * 10**16, 5.12 * 10**16])

NO2_1 = np.array([5.72 * 10**16, 4.92 * 10**16])
NO2_1_error = np.array([5.5236 * 10**14, 5.39 * 10**14])

O4_1 = np.array([3.41 * 10**43, 2.80 * 10**43])
O4_1_error = np.array([8.08 * 10**41, 3.83 * 10**42])

plt.errorbar(angle, O3_1, yerr=O3_1_error, fmt='.', label='Messung von O3 Set 1')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O3')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O3_1.pdf')
print('saved figure')

plt.errorbar(angle, NO2_1, yerr=NO2_1_error, fmt='.', label='Messung von NO2 Set 1')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO2')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_NO2_1.pdf')
print('saved figure')

plt.errorbar(angle, O4_1, yerr=O4_1_error, fmt='.', label='Messung von O4 Set 1')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O4_1.pdf')
print('saved figure')

#Set 2

O3_2 = np.array([6.21 * 10**17, 3.23 * 10**17])
O3_2_error = np.array([6.78 * 10**16, 7.61 * 10**16])

NO2_2 = np.array([2.77 * 10**16, 1.45 * 10**16])
NO2_2_error = np.array([6.31 * 10**14, 6.10 * 10**14])

O4_2 = np.array([2.79 * 10**43, 1.35 * 10**43])
O4_2_error = np.array([2.07 * 10**42, 1.97 * 10**42])

plt.errorbar(angle, O3_2, yerr=O3_2_error, fmt='.', label='Messung von O3 Set 2')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O3')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O3_2.pdf')
print('saved figure')

plt.errorbar(angle, NO2_2, yerr=NO2_2_error, fmt='.', label='Messung von NO2 Set 2')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO2')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_NO2_2.pdf')
print('saved figure')

plt.errorbar(angle, O4_2, yerr=O4_2_error, fmt='.', label='Messung von O4 Set r')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O4_2.pdf')
print('saved figure')

#Set 3

O3_3 = np.array([6.01 * 10**17, 3.51 * 10**17])
O3_3_error = np.array([7.20 * 10**16, 6.94 * 10**16])

NO2_3 = np.array([2.24 * 10**16, 1.10 * 10**16])
NO2_3_error = np.array([5.85 * 10**14, 5.37 * 10**14])

O4_3 = np.array([2.69 * 10**43, 9.36 * 10**42])
O4_3_error = np.array([1.95 * 10**42, 4.43 * 10**41])

plt.errorbar(angle, O3_3, yerr=O3_3_error, fmt='.', label='Messung von O3 Set 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O3')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O3_3.pdf')
print('saved figure')

plt.errorbar(angle, NO2_3, yerr=NO2_3_error, fmt='.', label='Messung von NO2 Set 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO2')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_NO2_3.pdf')
print('saved figure')

plt.errorbar(angle, O4_3, yerr=O4_3_error, fmt='.', label='Messung von O4 Set 3')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O4_3.pdf')
print('saved figure')

#Set4

O3_4 = np.array([8.81 * 10**17, 7.53 * 10**17])
O3_4_error = np.array([6.94 * 10**16, 7.60 * 10**16])

NO2_4 = np.array([2.60 * 10**16, 2.00 * 10**16])
NO2_4_error = np.array([5.13 * 10**14, 4.75 * 10**14])

O4_4 = np.array([2.81 * 10**43, 1.90 * 10**43])
O4_4_error = np.array([3.52 * 10**41, 3.361 * 10**41])

plt.errorbar(angle, O3_4, yerr=O3_4_error, fmt='.', label='Messung von O3 Set 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O3')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O3_4.pdf')
print('saved figure')

plt.errorbar(angle, NO2_4, yerr=NO2_4_error, fmt='.', label='Messung von NO2 Set 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von NO2')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_NO2_4.pdf')
print('saved figure')

plt.errorbar(angle, O4_4, yerr=O4_4_error, fmt='.', label='Messung von O4 Set 4')
plt.xlabel('Winkel')
plt.ylabel('$\Delta$SCD von O4')
f = plt.gcf()
f.set_size_inches(11.69, 8.27)
plt.show()
plt.savefig('max_DOAS_O4_4.pdf')
print('saved figure')



