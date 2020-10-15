def custom_round(num,n=2):
    if n == 1:
        return '{:.1f}'.format(round(num,1))
    if n == 3:
        return '{:.3f}'.format(round(num,3))
    else:
        return '{:.2f}'.format(round(num,2))
    
from math import sin
from math import cos
from math import sqrt
import matplotlib
from math import pi




L = [54.5, 54.4, 54.5, 54.5, 54.4]
R = [174.6, 174.7, 174.5, 174.6, 174.6]




halber_winkel = [0] * 5
for i in range(5):
    halber_winkel[i] = (R[i] - L[i])/2
    
phi_average = sum(halber_winkel)/len(halber_winkel) # mittelwert
phi_average_bogenmass = phi_average / 360 * 2 * pi

delta_phi = 0.2
delta_phi_bogenmass = delta_phi/360 * 2 * pi
print(custom_round(phi_average,2))


f = open("tab_prisma_messen_1.tex", "w")
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


halber_winkel = [0] * 5
halber_winkel_bogenmass = [0] * 5
for i in range(5):
    halber_winkel[i] = (R[i]-L[i])/2
    halber_winkel_bogenmass[i] = halber_winkel[i]/360 * 2 * pi



gamma = sum(halber_winkel)/len(halber_winkel)
gamma_bogenmass = gamma/360 * 2 * pi

f = open("prisma_gamma.tex", "w")
f.write("\\begin{align*}\n")
f.write("\\gamma = \\frac{\\epsilon}{2} =  " + str(custom_round(gamma,2)) + "^\\circ\n")
f.write("\\end{align*}\n")
f.close()

f = open("prisma_gamma_mit_fehler.tex", "w")
f.write("\\begin{align*}\n")
f.write("\\gamma = (" + str(custom_round(gamma,1)) + " \pm 0.9)^\\circ\n")
f.write("\\end{align*}\n")
f.close()




#Hg-Lampe

farben = ['Violett', 'Indigo', 'Blaugrün', 'Grün', 'Gelb']
R = [80.0, 80.9, 82.0, 82.6, 83.0]
#L = [199.8, 200.8, 201.9, 202.5, 202.9]
L = [202.9, 202.5, 201.9, 200.8, 199.8]
     

halber_winkel = [0] * 5
halber_winkel_bogenmass = [0] * 5
for i in range(5):
    halber_winkel[i] = abs(R[i]-L[i])/2
    halber_winkel_bogenmass[i] = halber_winkel[i]/360 * 2 * pi
    print(halber_winkel[i])
    

f = open("tab_prisma_messen_2.tex", "w", encoding='utf-8')
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




delta_gamma = (0.2/sqrt(5))/360 * 2 * pi
delta_delta = 0.2 / 360 * 2 * pi
f = open("prisma_auswertung.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{c|rrr}\n")
f.write("Farbe &  n & $\Delta n$ \\\\\n")
f.write("\\hline\n")
for i in range(5):
    unsicherheit = cos( (halber_winkel_bogenmass[i] + gamma_bogenmass)/2) / sin( gamma_bogenmass/2) * delta_delta/2
    unsicherheit += (cos( (gamma_bogenmass + halber_winkel_bogenmass[i])/2 ) * sin( gamma_bogenmass/2) - sin( (halber_winkel_bogenmass[i] + gamma_bogenmass)/2)*cos( gamma_bogenmass/2 ))/sin( gamma_bogenmass/2) * delta_gamma/2
    n = sin( (gamma_bogenmass + halber_winkel_bogenmass[i])/2 )/sin( gamma_bogenmass / 2)
    f.write(farben[i] + "  & " + str( custom_round(n,3) ) + " & " + str(custom_round(unsicherheit,3)))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()



exit(1)


















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





print("Auflösung: " + str(b/g))
print("Auflösung Fehler: " + str(delta_b/g + b/g**2 * delta_g))

