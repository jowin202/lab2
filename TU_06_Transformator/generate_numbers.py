from math import sqrt
from math import sin
from math import cos
from math import pi


import numpy as np
import matplotlib.pyplot as plt


print("Aufgabe 1:")

U_1 = 160
Delta_U_1 = 1.2
U_2 = 16.8
Delta_U_2 = 0.12

I_1 = 0.2
Delta_I_1 = 0.009
P_1 = 6.9
Delta_P_1 = 0.1



print("Scheinleistung:")

S_1 = U_1 * I_1
Delta_S_1 = Delta_U_1 * I_1 + U_1 * Delta_I_1

print(str(S_1) + " +- " + str(Delta_S_1))

print("")

print("Blindleistung:")

Q_1 = sqrt(S_1**2 - P_1**2)
Delta_Q_1 = (S_1 * Delta_S_1 + P_1 * Delta_P_1)/Q_1

print(str(Q_1) + " +- " + str(Delta_Q_1))

print("")
print("Leistungsfaktor:")

cos_phi = P_1/S_1
Delta_cos_phi = Delta_P_1/S_1 + P_1/S_1**2 * Delta_S_1


print(str(cos_phi) + " +- " + str(Delta_cos_phi))




print("")
print("")
print("")

print("Aufgabe 2:")

U_1 = 160
Delta_U_1 = 1.2
U_2 = 16.6
Delta_U_2 = 0.12

I_1 = 0.6/120*47
Delta_I_1 = 0.009

I_2 = 0.68
Delta_I_2 = 0.02 # 0.018

P_1 = 19.3
Delta_P_1 = 0.1

print("Primaerstrom: " + str(I_1))


print("Scheinleistung:")

S_1 = U_1 * I_1
Delta_S_1 = Delta_U_1 * I_1 + U_1 * Delta_I_1

print(str(S_1) + " +- " + str(Delta_S_1))

print("")

print("Blindleistung:")

Q_1 = sqrt(S_1**2 - P_1**2)
Delta_Q_1 = (S_1 * Delta_S_1 + P_1 * Delta_P_1)/Q_1

print(str(Q_1) + " +- " + str(Delta_Q_1))

print("")
print("Leistungsfaktor:")

cos_phi = P_1/S_1
Delta_cos_phi = Delta_P_1/S_1 + P_1/S_1**2 * Delta_S_1


print(str(cos_phi) + " +- " + str(Delta_cos_phi))


print("")

print("Wirkleistung sekundaer, P2: ")

P_2 = U_2 * I_2
Delta_P_2 = Delta_U_2 * I_2 + U_2 * Delta_I_2

print(str(P_2) + " +- " + str(Delta_P_2))


print("")

print("Wirkungsgrad, eta: ")

eta = P_2/P_1
Delta_eta = Delta_P_2/P_1 + P_2/P_1**2 * Delta_P_1

print(str(eta) + " +- " + str(Delta_eta))


print("")

print("Verlustleistung P_V: ")

print(str(P_1-P_2) + " +- " + str(Delta_P_1 + Delta_P_2))









x = [4.2,5.3,6.9,8.5,9.3,11.2,13.3,15.9,20.3,23.8,26.3,29.2,32.6,36.2,38.5]
y = [1.17,1.38,1.67,1.79,1.89,2.06,2.12,2.18,2.08,2.00,1.92,1.83,1.73,1.60,1.54]


fig, ax = plt.subplots()

ax.set_xlim(4,40)
ax.set_ylim(1.1,2.5)
ax.plot(x,y)


ax.set_xlabel('Widerstand / Ohm')
ax.set_ylabel('Leistung / W ')

plt.savefig("kurve.png")




