import numpy as np
import matplotlib.pyplot as plt
from math import log,sin, tan, sqrt, pi
import numpy

x1 = 0.320 * 10**-3
x2 = 0.714 * 10**-3
x3 = 1.790 * 10**-3

l = 633 * 10**-9
delta_l = 10*10**-9

d1 = 0.43 * 10**-3
d2 = 0.23 * 10**-3
d3 = 0.13 * 10**-3


delta_d = 0.005 * 10**-3

f1 = 300 * 10**-3
delta_f1 = 2 * 10**-3


def zw(d):
    zw = l*f1/d
    delta_zw = (delta_f1 * d * l + f1 * l *delta_d + f1*d * delta_l)/d**2
    return 1000000*zw, 1000000*delta_zw


print(zw(d1))
print(zw(d2))
print(zw(d3))




def zw_in_mm_curve(d):
    zw = l*f1/d
    delta_zw = (delta_f1 * d * l + f1 * l *delta_d + f1*d * delta_l)/d**2
    return 1000*zw

def zw_in_mm_oben(d):
    zw = l*f1/d
    delta_zw = (delta_f1 * d * l + f1 * l *delta_d + f1*d * delta_l)/d**2
    return 1000*(zw+delta_zw)

def zw_in_mm_unten(d):
    zw = l*f1/d
    delta_zw = (delta_f1 * d * l + f1 * l *delta_d + f1*d * delta_l)/d**2
    return 1000*(zw-delta_zw)


xd = [0.13, 0.23, 0.43]
yd = [1.790, 0.714, 0.320]

x = [i/100 for i in range(10,100)]
y1 = [zw_in_mm_oben(i*10**-3) for i in x]
y2 = [zw_in_mm_unten(i*10**-3) for i in x]
y = [zw_in_mm_curve(i*10**-3) for i in x]



fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(x, y, 'blue')
ax.plot(xd, yd, 'red', ls='', marker='x')
#ax.plot(x, y, '#3366FF')
#ax.plot(x, y, '#3366FF')
#ax.plot(x_noshift, y_noshift, 'green')
ax.legend(['Theoretische Werte als Kurve', 'Gemessene Werte'])
ax.set_xlabel('d / mm')
ax.set_ylabel('2w / mm')
ax.set_title('')
plt.savefig("task4.png")

