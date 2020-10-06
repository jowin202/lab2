
#Messen nach Bessel

#G Gegenstandsposition
#B Bildposition
#L Linsenposition

#G fix, L1, L2 messen, alles in cm

G = [161, 161, 161, 161, 161]
L1 = [44.7, 39.6, 53.3, 66.0, 76.8]
L2 = [136.6, 136.6, 136.0, 135.4, 134.4]
B = [15, 20,30,40,50]

#unsicherheit fuer laengenmessung in cm
delta_l = 0.01
delta_a = 0.01*2
delta_e = 0.01*2

file = open("bessel_messwerte.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $G$ / cm & $B$ / cm & $L_1$ / cm & $L_2$ / cm \\\\\n")
file.write("\hline\n")

for i in range(5):
    file.write(str(i+1) + " & " + str(round(G[i],2)) + " & " + str(round(B[i],2)) + " & " + str(round(L1[i],2))+ " & " + str(round(L2[i],2)))
    if i != 4:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()


a = [0] * 5
e = [0] * 5
f = [0] * 5
delta_f = [0] * 5

for i in range(5):
    a[i] = G[i] - B[i]
    e[i] = abs(L1[i] - L2[i])
    f[i] = 0.25 * (a[i]**2 - e[i]**2)/a[i]
    delta_f[i] = 0.25/a[i]**2 * ( (a[i]**2 + e[i]**2) * delta_a + 2*a[i]*e[i]* delta_e)

file = open("bessel_auswertung.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $a$ / cm & $e$ / cm & $f$ / cm & $\\Delta f$ / cm \\\\\n")
file.write("\hline\n")

for i in range(5):
    file.write(str(i+1) + " & " + str(round(a[i],2)) + " & " + str(round(e[i],2)) + " & " + str(round(f[i],2)) + " & " + str(round(delta_f[i],2)))
    if i != 4:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()



file = open("bessel_ergebnis.tex", "w")
file.write("\\begin{align*}\n")
file.write("f = (" + str(round(sum(f)/5,2)) + " \pm " + str(round(sum(delta_f)/5,2)) + ")~\\text{cm}\\\\")
file.write("\\end{align*}\n")








