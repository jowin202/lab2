
#Messen nach Bessel

#G Gegenstandsposition
#B Bildposition
#L Linsenposition

#G fix, L1, L2 messen, alles in cm

G = [160, 160, 160, 160, 160, 160, 160, 160, 160, 160]
L1 = [135.6,135.3,135.1,135.8,135.3,136.2,135.9,136.1,135.5,135.2]
L2 = [39.5,44.8,42.7,36.4,46.8,29.2,32.3,34.5,49.1,51.1]
B = [15,20,18,12,22,5,8,10,24,26]

#unsicherheit fuer laengenmessung in cm
delta_l = 0.3
delta_a = 0.3*2
delta_e = 0.3*2

file = open("bessel_messwerte.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $G$ / cm & $B$ / cm & $L_1$ / cm & $L_2$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(G[i],2)) + " & " + str(round(B[i],2)) + " & " + str(round(L1[i],2))+ " & " + str(round(L2[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()


a = [0] * 10
e = [0] * 10
f = [0] * 10
delta_f = [0] * 10

for i in range(10):
    a[i] = G[i] - B[i]
    e[i] = abs(L1[i] - L2[i])
    f[i] = 0.25 * (a[i]**2 - e[i]**2)/a[i]
    delta_f[i] = 0.25/a[i]**2 * ( (a[i]**2 + e[i]**2) * delta_a + 2*a[i]*e[i]* delta_e)

file = open("bessel_auswertung.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $a$ / cm & $e$ / cm & $f$ / cm & $\\Delta f$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(a[i],2)) + " & " + str(round(e[i],2)) + " & " + str(round(f[i],2)) + " & " + str(round(delta_f[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()



file = open("bessel_ergebnis.tex", "w")
file.write("\\begin{align*}\n")
file.write("f = (" + str(round(sum(f)/10,2)) + " \pm " + str(round(sum(delta_f)/10,2)) + ")~\\text{cm}\\\\")
file.write("\\end{align*}\n")








