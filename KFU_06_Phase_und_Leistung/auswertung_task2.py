import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from math import log,sqrt,pi
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

print("Phasenverschiebungen:")
t, V1, V2 = read_csv("daten/pul_4.csv")

phase_t = phasenverschiebung(t,V1,V2,0)
print("praktische phasenverschiebung C: " + str(phase_t/f*360))

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V1, 'blue')
ax.plot(t, V2, 'red')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
ax.legend(['CH1', 'CH2'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('Phase Kondensator')
plt.savefig("bilder/task2.png")
plt.close()




t, V1, V2 = read_csv("daten/pul_5.csv")
phase_t = phasenverschiebung(t,V1,V2,900)
print("praktische phasenverschiebung L: " + str(phase_t/f*360))

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V1, 'blue')
ax.plot(t, V2, 'red')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
ax.legend(['CH1', 'CH2'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('Phase Spule')
plt.savefig("bilder/task3.png")
plt.close()





#impedanzen
f = 50 #Hz
Delta_f = 0.02 #Hz
R = 68
Delta_R = 3.4
C = 47*10**-6
Delta_C = C/5
print("Theoretische Phasenverschiebungen:")
phi2 = 1/(2*pi) * 1/(f*R*C)
delta_phi2 = 1/(2*pi) * (Delta_f*R*C + f*Delta_R*C + f*R*Delta_C)/(f*R*C)**2
print("phi2: " + str(phi2) + " +- " + str(delta_phi2))
print("phi2 range: " + str(180/pi*math.atan(phi2+delta_phi2)) + ", " + str(180/pi*math.atan(phi2-delta_phi2)))
print("theoretisch exakter Wert phi2: " + str(180/pi * math.atan(phi2)))
