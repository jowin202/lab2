from math import sin
from math import cos
from math import pi


#Na-Dampflampe
na_lampe_lambda_1 = 588.995 * 10**-9
na_lampe_lambda_2 = 589.592 * 10**-9

L = [172.6, 172.8, 172.7, 172.8, 172.7]
R = [87.7, 87.7, 87.7, 87.7, 87.7, 87.7]


halber_winkel = [0] * 5
for i in range(5):
    halber_winkel[i] = (L[i] - R[i])/2
    
phi_average = sum(halber_winkel)/len(halber_winkel) # mittelwert
phi_average_bogenmass = phi_average / 360 * 2 * pi

delta_phi = 0.2
delta_phi_bogenmass = delta_phi/360 * 2 * pi
print(round(phi_average,2))


#gitterkonstante
g1 = 2 * na_lampe_lambda_1/sin(phi_average_bogenmass)
g2 = 2 * na_lampe_lambda_2/sin(phi_average_bogenmass)

g = (g1+g2)/2

delta_lambda = 1*10**-9
delta_g = 2*delta_lambda/sin(phi_average_bogenmass) + 2 * (na_lampe_lambda_1 + na_lampe_lambda_2)/2 /(sin(phi_average_bogenmass)**2) * cos(phi_average_bogenmass) * delta_phi_bogenmass

f = open("gitterkonst.tex", "w")
f.write("\\begin{align*}\n")
f.write("g = (" + str(round(g*10**6,2)) + " \\pm " + str(round(delta_g*10**6,2)) +  ")~{\mu}m\\\\\n")
f.write("\\end{align*}\n")
f.close()





print("Gitterkonstante: " + str(g))

f = open("tab2.tex", "w")
f.write("\\begin{tabular}{c|rr}\n")
f.write("Nr. & L / ${}^\circ$ & R / ${}^\circ$ \\\\\n")
f.write("\\hline\n")
for i in range(5):
    f.write(str(i+1) + " & " + str(L[i]) + " & " + str(R[i]))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()







#Hg-Lampe

farben = ['Violett', 'Blau', 'Türkis', 'Grün', 'Gelb']
R = [104.1, 101.8, 97.6, 93.4, 90.9]
L = [159.2, 161.7, 166.0, 170.8, 173.5, 173.8]

halber_winkel = [0] * 5
halber_winkel_bogenmass = [0] * 5
wellenlaenge_pro_farbe = [0] * 5
wellenlaenge_pro_farbe_in_nm = [0] * 5
for i in range(5):
    halber_winkel[i] = (L[i]-R[i])/2
    halber_winkel_bogenmass[i] = halber_winkel[i]/360 * 2 * pi
    wellenlaenge_pro_farbe[i] = g * sin(halber_winkel[i] / 360 * 2 * pi)/2
    wellenlaenge_pro_farbe_in_nm[i] = wellenlaenge_pro_farbe[i] * 10**9
    
print(wellenlaenge_pro_farbe_in_nm)


f = open("tab3.tex", "w")
f.write("\\begin{tabular}{c|rr}\n")
f.write("Farbe & L / ${}^\circ$ & R / ${}^\circ$ \\\\\n")
f.write("\\hline\n")
for i in range(5):
    f.write(farben[i] + " & " + str(L[i]) + " & " + str(R[i]))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()



f = open("tab5.tex", "w")
f.write("\\begin{tabular}{c|rr}\n")
f.write("Farbe & $\\lambda$ / nm  & $\\Delta\\lambda$ / nm \\\\\n")
f.write("\\hline\n")
for i in range(5):
    unsicherheit = delta_g * sin(halber_winkel_bogenmass[i])/2 +  g * cos(halber_winkel_bogenmass[i]) * delta_phi_bogenmass /2
    f.write(farben[i] + " & " + str(round(wellenlaenge_pro_farbe_in_nm[i],1)) + " & " + str( round(unsicherheit * 10**9, 1) ))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()




#Auflösevermögen

b = 2.1 * 10**-2 # 2.1 cm Breite
delta_b = 0.3 * 10**-2


f = open("aufl_gitter.tex", "w")
f.write("\\begin{align*}\n")
f.write("\\texttt{res} = (" + str(round(b/g)) + " \\pm " + str(round(delta_b/g + b/g**2 * delta_g)) +  ")\\\\\n")
f.write("\\end{align*}\n")
f.close()


print("Auflösung: " + str(b/g))
print("Auflösung Fehler: " + str(delta_b/g + b/g**2 * delta_g))

