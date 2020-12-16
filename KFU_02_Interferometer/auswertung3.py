import numpy as np
import matplotlib.pyplot as plt
from math import log,sin, tan, sqrt, pi
import numpy

def read_csv(filename):
    f = open(filename, "r")
    file_data = f.read()
    f.close()


    lines = file_data.split("\n")
    col1 = []
    col2 = []


    
    for i in range(1,len(lines)):
        line = lines[i]
        values = line.split(",")
        if len(values) < 2:
            continue
        val1 = float(values[0])
        val2 = float(values[1])

        col1.append(val1)
        col2.append(val2)
    return col1, col2







#task 1a
x_shift,y_shift = read_csv("moodle/shift.csv")
x_noshift,y_noshift = read_csv("moodle/noshift.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(x_shift, y_shift, 'blue')
ax.plot(x_noshift, y_noshift, 'green')
ax.legend(['Mit Polyacrylatschicht', 'Ohne Polyacrylatschicht'])
ax.set_xlabel('pixel')
ax.set_ylabel('gray value')
ax.set_title('Verschiebung des Beugungsmusters\ndurch eine Polyacrylschicht')
plt.savefig("shift_noshift.png")

#ax.set_title('Aufgabe 3,  t=100 ns')
#plt.savefig("bilder/task3/task3_100ns.png")
plt.close()









n = 1.492


f = 150000 # in mu
delta_f = 500

l = 633 * 10**-9
delta_l = 10*10**-9

d = 0.43 * 10**-3 #change to 0.43
delta_d = 0.005*10**-3

x = 238
delta_x = 4


Z = f * tan( numpy.arcsin(4 * l/d))/x
delta_Z = 0.24

x_d = 67 #pixel verschiebung

b = x_d * Z

print("b: " + str(x_d * Z) + " + - " + str(2 * Z + x_d*delta_Z))
print("theta: " + str(numpy.arctan(b/f)))

#t = d/(n-1) * 67*Z/sqrt(f**2* (67*Z)**2)

t = d*sin(numpy.arctan(b/f))/(n-1)
print(t)
