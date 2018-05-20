import numpy as np


# constants             # units
l = 2                   # cm
b = 5                   # mm
d = 200                 # mum
g_a = 100               # mum
g_d = 100               # mum
D_a = 3                 # mm
D_d = D_a
U_a = 10                # Volt
U_0 = U_a
U_b = 108               # Volt
E = 98                  # GN/m^2
rho = 8.5 * 10**3       # kg/m^3
C_L = 300               # pF
R = 300                 # MOhm
epsilon_0 = 8.85*10**(-12)   # (A * s) / (V * m)


C_a = epsilon_0 * S / g_a
C_d = epsilon_0 * s / g_d
force_max = 0.25 * C_a * U_0**2 * 2 / g_a
amplitude_max = 4 * l**3 * force_max / (E * d**3 * b)
U_max = U_b * amplitude_max * C_d / (g_d * C_L)

print('Maximale geschätzte Amplitude: ', U_max)
  
