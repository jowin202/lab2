import numpy as np
import matplotlib.pyplot as plt


x = [403, 435, 490, 545, 575]
y = [1.743, 1.738, 1.730, 1.723, 1.717]
xerr = [5,5,5,5,5]
yerr = [0.001,0.001,0.001,0.001,0.001]

fig, ax = plt.subplots()

ax.set_xlim(400,600)
ax.set_ylim(1.71,1.75)
ax.errorbar(x, y,
            xerr=xerr,
            yerr=yerr, ls='None')

ax.set_xlabel('Wellenlänge lambda / nm')
ax.set_ylabel('Brechungsindex n / 1 ')

plt.savefig("kurve.png")
