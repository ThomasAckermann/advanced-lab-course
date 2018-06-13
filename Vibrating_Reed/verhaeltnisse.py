import numpy as np

n_1_theo = 6.267
n_2_theo = 17.548

omega_1 = 143.91
omega_1_err = 0.15
omega_1_t = 143.17
omega_1_t_err = 3.16

omega_2 = 909.52
omega_2_err = 1.06
omega_2_t = 916.41
omega_2_t_err = 35.84

omega_3_t = 2558.11
omega_3_t_err = 148.26
print('######## Experimentell ########')
n_1 = omega_2 / omega_1
n_1_err = np.sqrt((omega_2_err / omega_1_t)**2 + (omega_2  * omega_1_err / omega_1**2)**2)
print('n1 exp: ', n_1, '+/-', n_1_err)

n_1_t = omega_2_t / omega_1_t
n_1_t_err = np.sqrt((omega_2_t_err / omega_1_t)**2 + (omega_2_t  * omega_1_t_err / omega_1_t**2)**2)
print('n1 tilde exp: ', n_1_t, '+/-', n_1_t_err)
n_2_t = omega_3_t / omega_1_t
n_2_t_err = np.sqrt((omega_3_t_err / omega_1_t)**2 + (omega_3_t  * omega_1_t_err / omega_1_t**2)**2)
print('n2 tilde exp: ', n_2_t, '+/-', n_2_t_err)

print('######## Theoretisch ########')
print(n_1_theo)
print(n_2_theo)




print('sigma')
print('sigma 1: ', (n_1_theo - n_1) / n_1_err)
print('sigma 1 tilde: ', (n_1_theo - n_1_t) / n_1_t_err)
print('sigma 2 tilde: ', (n_2_theo - n_2_t) / n_2_t_err)



