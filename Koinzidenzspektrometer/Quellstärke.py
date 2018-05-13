import numpy as np
import matplotlib.pyplot as plt 


r_1 = 29265 / 100
r_2 = 29076 / 100
r_ko = 3153 / 461
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


lam = np.log(2) / (5.27 * 365)
act_0 = 404
delta_t = 4650
act = act_0 * np.exp(-1 * lam * delta_t)

print('Aktivität Co60: ', act)

