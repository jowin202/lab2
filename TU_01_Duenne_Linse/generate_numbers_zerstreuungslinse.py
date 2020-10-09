
#Messen der Zerstreuungslinse

#G Gegenstandsposition
#B Bildposition
#B1 Bildposition der Sammellinse
#L1 Linsenposition Sammellinse
#L2 Linsenposition Zerstreuungslinse

#G, B fix, L messen, alles in cm

G = [160, 160, 160, 160, 160, 160, 160, 160, 160, 160]
B = [65, 35.5, 56.6, 50, 60.3, 22.6, 54.1, 35.9, 69.8, 69.6]
B1 = [77, 77, 77, 77, 77, 77, 77, 77, 77, 77]
L1 = [112, 112, 112, 112, 112, 112, 112, 112, 112, 112]
L2 = [90, 94.5, 92, 93, 91, 96, 92.5, 95, 88, 87.5]

#unsicherheit fuer laengenmessung in cm
delta_l = 0.3
delta_b = 0.3*2
delta_g = 0.3*2

file = open("zerstreuungslinse_messwerte.tex", "w")
file.write("\\begin{tabular}{c|rrrrr}\n")
file.write("Nr. & $G$ / cm & $B^\\prime$ / cm & $B$ / cm & $L_1$ / cm & $L_2$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(G[i],2)) + " & " + str(round(B1[i],2)) + " & " + str(round(B[i],2)) + " & " + str(round(L1[i],2)) + " & " + str(round(L2[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()


g1 = [0] * 10
b = [0] * 10
f = [0] * 10
delta_f = [0] * 10

for i in range(10):
    g1[i] = B1[i] - L2[i]
    b[i] = L2[i] - B[i]
    f[i] = 1/(1/g1[i] + 1/b[i])
    delta_f[i] = (1/g1[i] + 1/b[i])**-2 * (delta_g/g1[i]**2 + delta_b/b[i]**2)

file = open("zerstreuungslinse_auswertung.tex", "w")
file.write("\\begin{tabular}{c|rrrr}\n")
file.write("Nr. & $g^\\prime$ / cm & $b$ / cm & $f$ / cm & $\\Delta f$ / cm \\\\\n")
file.write("\hline\n")

for i in range(10):
    file.write(str(i+1) + " & " + str(round(g1[i],2)) + " & " + str(round(b[i],2)) + " & " + str(round(f[i],2)) + " & " + str(round(delta_f[i],2)))
    if i != 9:
        file.write("\\\\")
    file.write("\n")
file.write("\\end{tabular}\n")
file.close()



file = open("zerstreuungslinse_ergebnis.tex", "w")
file.write("\\begin{align*}\n")
file.write("f = (" + str(round(abs(sum(f))/10,2)) + " \pm " + str(round(sum(delta_f)/10,2)) + ")~\\text{cm}\\\\")
file.write("\\end{align*}\n")








