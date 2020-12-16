import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin




def curve(w):
    d = 0.23 * 10**-3
    f = 300 * 10**-3
    l = 633 * 10**-9
    return abs( sin(pi* d * w / (l*f)) / (pi* d * w / (l*f)))
    
    







dots_x = [0.23, 0.48, 0.73, 0.97, 1.23, 1.45]
dots_y = [0.88, 0.64, 0.29, 0.09, 0.14, 0.11]


x = [i/100 for i in range(1,181)]
y = [curve(w*10**-3) for w in x]




fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(x, y, 'blue')
ax.plot(dots_x, dots_y, 'red', ls='', marker='o')
#ax.plot(x_noshift, y_noshift, 'green')
#ax.legend(['Mit Polyacrylatschicht', 'Ohne Polyacrylatschicht'])
ax.set_xlabel('2w / mm')
ax.set_ylabel('Kontrast / 1')
ax.set_title('Breite der Lichtquelle gegenüber Kontrast')
plt.savefig("curve_task1.png")

#ax.set_title('Aufgabe 3,  t=100 ns')
#plt.savefig("bilder/task3/task3_100ns.png")
plt.close()



exit(0)

def read_from_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    
    lines = data.split("\n")
    
    maximum_i = 0
    maximum_x = 0
    maximum = -10000
    
    for i in range(1,len(lines)):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y > maximum:
            maximum = y
            maximum_i = i
            maximum_x = x
            
            
            
    minimum_1 = 100000
    minimum_2 = 100000
    for i in range(maximum_i-150,maximum_i):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y < minimum_1:
            minimum_1 = y
            
            
            
    for i in range(maximum_i,maximum_i+150):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y < minimum_2:
            minimum_2 = y
            
            
            
    return maximum_x,maximum, minimum_1,minimum_2
    
    

    
    
print(read_from_file("moodle/img2.csv"))
print(read_from_file("moodle/img3.csv"))
print(read_from_file("moodle/img4.csv"))
