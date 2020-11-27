import numpy as np
import matplotlib.pyplot as plt
from math import log


def read_csv(filename):
    f = open(filename, "r")
    file_data = f.read()
    f.close()


    refspec_lines = file_data.split("\n")
    col1 = []
    col2 = []
    col3 = []
    col4 = []


    
    for line in refspec_lines:
        values = line.split(",")
        if len(values) < 3:
            continue
        values[0] = values[0].replace(",", ".")
        values[1] = values[1].replace(",", ".")
        values[2] = values[2].replace(",", ".")
        if values[0] == "x-axis" or values[0] == "second":
            continue
        val1 = 1000*float(values[0])
        val2 = float(values[1])
        val3 = float(values[2])
        val4 = (val2-val3)/100

        col1.append(val1)
        col2.append(val2)
        col3.append(val3)
        col4.append(val4)
    return col1, col2, col3, col4








UF = [0, 0.11, 0.391, 0.51, 0.595, 0.7, 0.723, 0.735, 0.747, 0.764, 0.78, 0.791, 0.799, 0.806, 0.812, 0.815]
IF = [0, 0.01, 0.01, 0.15, 1.02, 10.51, 14.5, 22.16, 32.53, 50.3, 75.6, 101.1, 125.7, 151.8, 176.6, 192.4]






#t1a_ch1_500, V1a_ch1_500 = read_csv("daten/scope_2_1.csv")
#t1a_ch2_500, V1a_ch2_500 = read_csv("daten/scope_2_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
#ax.plot(t1a_ch1_500, V1a_ch1_500, 'grey')
#ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
ax.scatter(UF,IF)
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('UF / V')
ax.set_ylabel('IF / mA')
ax.set_title('Diode in Durchlassrichtung')
plt.savefig("bilder/task1a.png")
plt.close()







UR = [0,-5,-10,-15,-20,-25,-30,-35,-40]
UIR = [0, -0.45, -0.74, -1.01, -1.19, -1.36, -1.49, -1.58, -1.67] # in mV







time, V1, V2, ID = read_csv("daten/Zenerdiode.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(time, V1, 'blue')
ax.plot(time, V2, 'green')
ax.legend(['CH1', 'CH2'])
ax.set_xlabel('time / ms')
ax.set_ylabel('U2 / V')
ax.set_title('Zenerdiode Spannung')
plt.savefig("bilder/task2.png")
plt.close()


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(time, ID, 'red')
#ax.legend(['CH1', 'CH2'])
ax.set_xlabel('time / ms')
ax.set_ylabel('I / A')
ax.set_title('Zenerdiode Stromverlauf')
plt.savefig("bilder/task2_I.png")
plt.close()

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(V2, ID, 'red')
#ax.legend(['CH1', 'CH2'])
ax.set_xlabel('U / V')
ax.set_ylabel('I / A')
ax.set_title('Kennlinie der Zenerdiode')
plt.savefig("bilder/task2_IU.png")
plt.close()

