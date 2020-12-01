import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from math import log,sqrt


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
        if len(values) < 2:
            continue
        values[0] = values[0].replace(",", ".")
        values[1] = values[1].replace(",", ".")
        if values[0] == "x-axis" or values[0] == "second":
            continue
        val1 = 1000*float(values[0]) # in ms
        val2 = float(values[1])
        val3 = float(values[0]) # time in sec
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



def effektivwert_sinus(t, Volt):
    t = t[399:1201]
    Volt = Volt[399:1201] #händisch gesucht
    
    for i in range(len(Volt)):
        Volt[i] = Volt[i]**2
    
    return sqrt(1/0.020 * simps(Volt,t))


def effektivwert_dreieck(t, Volt):
    t = t[400:1203]
    Volt = Volt[400:1203] #händisch gesucht
    
    for i in range(len(Volt)):
        Volt[i] = Volt[i]**2
    
    return sqrt(1/0.020 * simps(Volt,t))


def effektivwert_rechteck(t, Volt):
    t = t[198:1000]
    Volt = Volt[198:1000] #händisch gesucht
    
    for i in range(len(Volt)):
        Volt[i] = Volt[i]**2
    
    return sqrt(1/0.020 * simps(Volt,t))





t, V, t1 = read_csv("daten/pul_1.csv")
print("Spitze-Tal (Sinus): " + str(spitze_tal(V)))
print("Effektivwert (Sinus): " + str(effektivwert_sinus(t1,V)))

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V, 'blue')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('Sinus')
plt.savefig("bilder/task1_sin.png")
plt.close()

t, V, t1 = read_csv("daten/pul_2.csv")
print("Spitze-Tal (Dreieck): " + str(spitze_tal(V)))
print("Effektivwert (Dreieck): " + str(effektivwert_dreieck(t1,V)))

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V, 'blue')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('Dreieck')
plt.savefig("bilder/task1_dreieck.png")
plt.close()

t, V, t1 = read_csv("daten/pul_3.csv")
print("Spitze-Tal (Rechteck): " + str(spitze_tal(V)))
print("Effektivwert (Rechteck): " + str(effektivwert_rechteck(t1,V)))

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t, V, 'blue')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
#ax.scatter(UF,IF)
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('t / ms')
ax.set_ylabel('U / V')
ax.set_title('Rechteck')
plt.savefig("bilder/task1_rechteck.png")
plt.close()










