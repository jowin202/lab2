import numpy as np
import matplotlib.pyplot as plt
from math import log




def calc_na(d, delta_d, f, delta_f):
    na = d/(2*f)
    delta_na = 0.5 * (delta_d * f + delta_f * d)/f**2
    
    return na, delta_na





f = 60 * 10**-3
delta_f = 1 * 10**-3

d1 = 2 * 10**-3
d2 = 3 * 10**-3
d3 = 6 * 10**-3
delta_d = 0.1 * 10**-3


na1, delta_na1 = calc_na(d1, delta_d, f, delta_f)
print(1000*na1, 1000*delta_na1)

na2, delta_na2 = calc_na(d2, delta_d, f, delta_f)
print(1000*na2, 1000*delta_na2)

na3, delta_na3 = calc_na(d3, delta_d, f, delta_f)
print(1000*na3, 1000*delta_na3)




x = []
y_blau = []
y_rot = []
for i in range(15,60):
    x.append(i/1000.0)
    y_blau.append(0.61 * 470.0 * 10**-9/(i/1000.0) *10**6)
    y_rot.append(0.61 * 635.0 * 10**-9/(i/1000.0) *10**6)
    



na = [0.0167, 0.025, 0.05]
tm_blue = [15.6, 11.0, 6.9]
tm_red = [17.5, 15.6, 8.8]


moodle_blue = [15.6, 11.0, 5.5]
moodle_red = [17.5, 15.6, 8.8]


abw_x = [0.05]
abw_y = [5.5]


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(x, y_blau, 'blue')
ax.plot(x, y_rot, 'red')
ax.plot(na, tm_blue, marker='o', ls='', color='blue')
ax.plot(na, tm_red, marker='o', ls='', color='red')
ax.plot(abw_x, abw_y, marker='x', ls='', color='green')
ax.legend(['blaues Licht','rotes Licht', 'Messwerte blau','Messwerte rot ', 'Ausreisser'])
ax.set_xlabel('N.A. / 1')
ax.set_ylabel('Auflösung / µm')
ax.set_title('Auflösung abhängig von Numerischer Apertur')
plt.savefig("plot.png")
plt.close()





def calc_theor_aufl(na, delta_na, col):
    f = 470.0*10**-9
    if col == 'red':
        f = 635.0*10**-9

    delta_f = 5*10**-9
    
    return 10**6 * 0.61 * f/na, 10**6 * 0.61 * (delta_f * na + f*delta_na)/na**2


print(na1)
print()

print(calc_theor_aufl(na1, delta_na1, 'red'))
print(calc_theor_aufl(na2, delta_na2, 'red'))
print(calc_theor_aufl(na3, delta_na3, 'red'))
print(calc_theor_aufl(na1, delta_na1, 'blue'))
print(calc_theor_aufl(na2, delta_na2, 'blue'))
print(calc_theor_aufl(na3, delta_na3, 'blue'))
print()
print()
print()
print()





wert55 = 50.8
wert56 = 57
wert61 = 64
wert62 = 71.8
wert63 = 80.6
wert64 = 90.5
wert65 = 102
wert66 = 114
wert71 = 128
wert72 = 144
wert73 = 161
wert74 = 181
wert75 = 203




def calc_gem_aufl(wert, vorher, nachher):
    ergebnis1 = 1/vorher
    ergebnis2 = 1/wert
    ergebnis3 = 1/nachher
    
    return 1000*ergebnis2, 1000*(ergebnis1-ergebnis3)/2


print(calc_gem_aufl(wert61,wert56,wert62))
print(calc_gem_aufl(wert64,wert63,wert65))
print(calc_gem_aufl(wert56,wert55,wert61))

print(calc_gem_aufl(wert66,wert65,wert71))
print(calc_gem_aufl(wert72,wert71,wert73))

print(calc_gem_aufl(wert74,wert73,wert75))





exit(0)





