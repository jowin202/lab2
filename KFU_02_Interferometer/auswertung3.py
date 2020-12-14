import numpy as np
import matplotlib.pyplot as plt
from math import log

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
