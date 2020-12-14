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
x_nofilter, y_nofilter= read_csv("moodle/img__.csv")
x_bp,y_bp= read_csv("moodle/img_633BP.csv")
x_lp,y_lp= read_csv("moodle/img_LP.csv")



'''
fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(x_nofilter, y_nofilter, 'blue')
ax.plot(x_bp, y_bp, 'green')
ax.plot(x_lp, y_lp, 'red')
ax.legend(['Kein Filter', '633 nm Bandpass', 'Langpass'])
ax.set_xlabel('pixel')
ax.set_ylabel('gray value')
ax.set_title('Beugungsmuster nach Filter')
plt.savefig("filter.png")

#ax.set_title('Aufgabe 3,  t=100 ns')
#plt.savefig("bilder/task3/task3_100ns.png")
plt.close()
'''



fig, (ax1,ax2,ax3) = plt.subplots(3,1) 
#ax1.axis([400, 800, 0.6, 1])
ax1.plot(x_nofilter, y_nofilter, 'blue')
ax1.legend(['Ohne Filter'])
ax1.set_ylabel('gray value')
ax1.set_title('Beugungsmuster nach Filter')
#plt.savefig("Transmission_Methyl.png")

#ax2.axis([400, 800, 0, 0.3])
ax2.plot(x_bp, y_bp, 'green')
ax2.legend(['633 nm Bandpass'])
ax2.set_ylabel('gray value')

#ax3.axis([400, 800, 0, 0.3])
ax3.plot(x_lp, y_lp, 'red')
ax3.legend(['Langpass'])
ax3.set_xlabel('pixel')
ax3.set_ylabel('gray value')

plt.savefig("filter.png")









