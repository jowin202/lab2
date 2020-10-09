
#Messen nach Laplace

#G Gegenstandsposition
#B Bildposition
#L Linsenposition

#G, B fix, L messen, alles in cm

G = [160, 160, 160, 160, 160, 160, 160, 160, 160, 160]
B = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
L = [136.2, 135.7, 135.2, 134.5, 134.9, 134.0, 133.9, 133.6, 132.9, 131.9]

#unsicherheit fuer laengenmessung in cm
delta_l = 0.3
delta_b = 0.3*2
delta_g = 0.3*2

file = open("laplace_messwerte.tex", "w")
file.write("\\begin{tabular}{c|rrr}\n")
file.write("Nr. & $G$ / cm & $B$ / cm & $L$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(G[i],2)) + " & " + str(round(B[i],2)) + " & " + str(round(L[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()


g = [0] * 10
b = [0] * 10
f = [0] * 10
delta_f = [0] * 10

for i in range(10):
    g[i] = G[i] - L[i]
    b[i] = L[i] - B[i]
    f[i] = 1/(1/g[i] + 1/b[i])
    delta_f[i] = (1/g[i] + 1/b[i])**-2 * (delta_g/g[i]**2 + delta_b/b[i]**2)

file = open("laplace_auswertung.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $g$ / cm & $b$ / cm & $f$ / cm & $\\Delta f$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(g[i],2)) + " & " + str(round(b[i],2)) + " & " + str(round(f[i],2)) + " & " + str(round(delta_f[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()



file = open("laplace_ergebnis.tex", "w")
file.write("\\begin{align*}\n")
file.write("f = (" + str(round(sum(f)/10,2)) + " \pm " + str(round(sum(delta_f)/10,2)) + ")~\\text{cm}\\\\")
file.write("\\end{align*}\n")








