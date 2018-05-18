import numpy as np


r_1 = 29265/100
r_2 = 29076/100
r_ko = 3153/461
m_ko = 2
m_1 = 2
m_2 = 2

r_1_err = np.sqrt(r_1)
r_2_err = np.sqrt(r_2)
r_ko_err = np.sqrt(r_ko)

quell = r_1 * r_2 * m_ko / (r_ko * m_1 * m_2)
quell_err = np.sqrt((r_1 * r_2 * m_ko * r_ko_err / (r_ko**2 * m_1 * m_2))**2 
                    + (r_1 * r_2_err * m_ko / (r_ko * m_1 * m_2))**2
                    + (r_1_err * r_2 * m_ko / (r_ko * m_1 * m_2))**2)

print('Quellstärke Co60: ', quell, '+/-', quell_err)


##################################################


tau = 38.64 * 10**(-9)
tau_err = 3.75 * 10**(-9)
r_koinz = 2 * r_1 * r_2 * tau
r_koinz_err = np.sqrt((2 * r_1_err * r_2 * tau)**2 + (2 * r_1 * r_2_err * tau)**2 + (2 * r_1 * r_2 * tau_err)**2)
print('R_koinz: ', r_koinz, '+/-', r_koinz_err)


##################################################


lam = np.log(2) / (5.27 * 365)
act_0 = 404
act_0_err = 0.03 * 404
delta_t = 4650x
act = act_0 * np.exp(-1 * lam * delta_t)
act_err = act_0_err * np.exp(-1 * lam * delta_t)

print('Aktivität Co60: ', act, '+/-', act_err)


#############################
###################


nach_w_r1 = r_1 / (2 * quell)
nach_w_r1_err = np.sqrt(r_1_err/(2 * quell)**2 + (quell_err * r_1 / (2 * quell**2))**2)
print('Nachweiswahrscheinlickeit r1: ', nach_w_r1, ' +/- ', nach_w_r1_err)


nach_w_r2 = r_2 / (2 * quell)
nach_w_r2_err = np.sqrt(r_2_err/(2 * quell)**2 + (quell_err * r_2 / (2 * quell**2))**2)
print('Nachweiswahrscheinlickeit r1: ', nach_w_r2, ' +/- ', nach_w_r2_err)
