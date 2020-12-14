import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from math import log,sqrt,pi,cos,sin
import math



def read_csv(filename):
    f = open(filename, "r")
    file_data = f.read()
    f.close()

    refspec_lines = file_data.split("\n")
    col1 = []
    col2 = []
    col3 = []
    
    for line in refspec_lines:
        values = line.split(",")
        if len(values) < 3:
            continue
        values[0] = values[0].replace(",", ".")
        values[1] = values[1].replace(",", ".")
        values[2] = values[2].replace(",", ".")
        if values[0] == "x-axis" or values[0] == "second":
            continue
        val1 = 1000*float(values[0]) # in ms
        val2 = float(values[1])
        val3 = float(values[2])
        col1.append(val1)
        col2.append(val2)
        col3.append(val3)
    return col1, col2, col3




def spitze_tal(Volt):
    Vmin =  10000000000000000000
    Vmax = -10000000000000000000
    for V in Volt:
        if V < Vmin:
            Vmin = V
        if V > Vmax:
            Vmax = V
    return Vmax-Vmin



def phasenverschiebung(t, V1, V2, offset):
    t0_V1 = 0
    t0_V2 = 0
    for i in range(offset, len(V1)-1):
        if V1[i] == 0:
            t0_V1 = t[i]
            break
        if V1[i] < 0 and V1[i+1] > 0:
            t0_V1 = (t[i] + t[i+1])/2
            break
    for i in range(len(V2)-1):
        if V2[i] == 0:
            t0_V2 = t[i]
            break
        if V2[i] < 0 and V2[i+1] > 0:
            t0_V2 = (t[i] + t[i+1])/2
            break
    
    return t0_V1-t0_V2
    
'''def effektivwert_sinus(t, Volt):
    t = t[399:1201]
    Volt = Volt[399:1201] #händisch gesucht
    
    for i in range(len(Volt)):
        Volt[i] = Volt[i]**2
    
    return sqrt(1/0.020 * simps(Volt,t))'''




f = 20 # in ms


t, V1, V2 = read_csv("daten/pul_6.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V1, 'blue')
ax.plot(t, V2, 'red')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
ax.legend(['CH1', 'CH2'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('RC-Schaltung')
plt.savefig("bilder/task4.png")
plt.close()




t, V1, V2 = read_csv("daten/pul_7.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V1, 'blue')
ax.plot(t, V2, 'red')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
ax.legend(['CH1', 'CH2'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('RL-Schaltung')
plt.savefig("bilder/task5.png")
plt.close()






#impedanzen
f = 50 #Hz
Delta_f = 0.02 #Hz
R = 68
Delta_R = 3.4
C = 47*10**-6
Delta_C = C/5

tan_phi4 = 1/(2*pi) * 1/(f*R*C)
delta_tan_phi4 = 1/(2*pi) * (Delta_f*R*C + f*Delta_R*C + f*R*Delta_C)/(f*R*C)**2
cos_phi4 = 1/sqrt(1+tan_phi4**2)
sin_phi4 = sqrt(1-cos_phi4**2)

phi4 = math.atan(tan_phi4)/pi*180
phi4_upper = math.atan(tan_phi4 + delta_tan_phi4)/pi*180
phi4_lower = math.atan(tan_phi4 - delta_tan_phi4)/pi*180
print("psi4 range: " + str(phi4_lower) + ", " + str(phi4) + ", " + str(phi4_upper))







UL = 13.07
Delta_UL = 0.16

IL = 0.051
Delta_IL = 0.0007

L =UL/(2*pi*f*IL)
Delta_L = (Delta_UL * IL*f + UL * Delta_IL * f + UL*IL*Delta_f)/(IL**2*f**2)

print("L: " + str(L) + " +- " + str(Delta_L))




tan_phi5 = 2*pi*f*L/R
delta_tan_phi5 = 2*pi * (Delta_f *L * R + f * Delta_L * R + f* L * Delta_R)/R**2
cos_phi5 = 1/sqrt(1+tan_phi5**2)
sin_phi5 = sqrt(1-cos_phi5**2)


phi5 = math.atan(tan_phi5)/pi*180
phi5_upper = math.atan(tan_phi5 + delta_tan_phi5)/pi*180
phi5_lower = math.atan(tan_phi5 - delta_tan_phi5)/pi*180
print("psi5 range: " + str(phi5_lower) + ", " + str(phi5) + ", " + str(phi5_upper))





print("")
print("")
print("")
print("")


#finale tabelle
UE_RC = 13.24
Delta_UE_RC = 0.16
UE_RL = 13.83
Delta_UE_RL = 0.16

I_RC = 136.7/1000
Delta_I_RC = 1.1/1000
I_RL = 51/1000
Delta_I_RL = 0.7/1000


print("S RC: " + str(UE_RC * I_RC) + " +- " + str(Delta_UE_RC * I_RC + UE_RC * Delta_I_RC) )
print("S RL: " + str(UE_RL * I_RL) + " +- " + str(Delta_UE_RL * I_RL + UE_RL * Delta_I_RL) )



print("Q RC: " + str(UE_RC * I_RC * sin_phi4) + " +- " + str(Delta_UE_RC * I_RC + UE_RC * Delta_I_RC) )
print("Q RL: " + str(UE_RL * I_RL * sin_phi5) + " +- " + str(Delta_UE_RL * I_RL + UE_RL * Delta_I_RL) )

print("W RC: " + str(UE_RC * I_RC * cos_phi4) + " +- " + str(Delta_UE_RC * I_RC + UE_RC * Delta_I_RC) )
print("W RL: " + str(UE_RL * I_RL * cos_phi5) + " +- " + str(Delta_UE_RL * I_RL + UE_RL * Delta_I_RL) )









