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





