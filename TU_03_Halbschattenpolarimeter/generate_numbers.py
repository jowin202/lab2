def custom_round(num,n=2):
    if n == 1:
        return '{:.1f}'.format(round(num,1))
    if n == 3:
        return '{:.3f}'.format(round(num,3))
    else:
        return '{:.2f}'.format(round(num,2))

def avg(l):
    return sum(l)/len(l)
    
from math import sin
from math import cos
from math import sqrt
from math import pi
from statistics import stdev
import matplotlib


#Laenge Glas in mm
#Lges = [111.7, 111.65, 111.7,111.7, 111.6]
#L1 = [3.85,3.80,3.85,3.85,3.85]
#L2 = [3.85,3.85,3.80,3.85,3.85]

aoff = [39.1,39.3,39.2,39.3,39.2]
a1 = [26.2,25.2,26.6,25.5,25.3,26.3,26.5,26.1,25.5,26.6]

delta_l = 0.01 #mm
delta_alpha = 0.1


#$f = open("rohrzucker_abmessungen_tab.tex", "w", encoding='utf-8')
#f.write("\\begin{tabular}{rrr}\\\\\n")
#f.write(" $\\ell_\\text{ges}$ / mm & $\\ell_1$ / mm & $\\ell_2$ /mm \\\\\n ")
#f.write("\\hline\n")
#for i in range(5):
#    f.write(str(custom_round(Lges[i],2)) + " & " + str(custom_round(L1[i],2)) + " & " + str(custom_round(L2[i],2)))
#    if i != 4:
#        f.write("\\\\")
#    f.write("\n")
#f.write("\\end{tabular}")
#f.close()

f = open("rohrzucker_winkel_offset_tab.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{r|r}\\\\\n")
f.write(" Nr. & $\\alpha_\\text{off}$ / ${}^\circ$  \\\\\n ")
f.write("\\hline\n")
for i in range(5):
    f.write(str(i+1) + " & " + str(custom_round(aoff[i],2))  )
    f.write("\\\\")
    f.write("\n")
f.write("\\hline \\\n $\\overline{x}$ & " + str(custom_round(sum(aoff)/len(aoff),2)) + "\n")
f.write("\\end{tabular}")
f.close()


f = open("rohrzucker_winkel_alpha_tab.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{r|r}\\\\\n")
f.write(" Nr & $\\alpha_1$ / ${}^\circ$  \\\\\n ")
f.write("\\hline\n")
for i in range(10):
    f.write(str(i+1) + " & " + str(custom_round(a1[i],2)) )
    f.write("\\\\")
    f.write("\n")
f.write("\\hline \\\n $\\overline{x}$ & " + str(custom_round(sum(a1)/len(a1),2)) + "\n")
f.write("\\end{tabular}")
f.close()



#f = open("rohrzucker_laenge.tex", "w", encoding='utf-8')
#f.write("\\begin{align*}\\\\\n")
#f.write("\ell = (" + str(custom_round(avg(Lges)-avg(L1)-avg(L2),2)) + " \\pm" + str(3 * delta_l) + ")~\\text{mm} \\\\\n")
#f.write("\\end{align*}\\\\\n")
#f.close()

laenge = 200 #mm
winkel = abs(sum(a1)/len(a1) - sum(aoff)/len(aoff))

print("Winkel Rohrzucker: " + str(winkel))

laenge_in_dm = laenge/100 

print(laenge_in_dm)
konzentration = winkel/(66.5 * laenge_in_dm)
delta_konzentration = delta_alpha/(66.5 * laenge_in_dm) 

f = open("rohrzucker_konzentration.tex", "w", encoding='utf-8')
f.write("\\begin{align*}\\\\\n")
f.write("c = (" + str(custom_round(konzentration*10**3,2)) + " \\pm" + str(custom_round(delta_konzentration*10**3,2)) + ")~\\text{mg}/\\text{cm}^3 \\\\\n")
f.write("\\end{align*}\\\\\n")
f.close()








#Kristalldicken mm
d1 = [6.98,6.99,6.99,6.99,6.99,6.98,6.99,6.98,6.99,6.99]
d2 = [6.51,6.50,6.50,6.51,6.51,6.50,6.51,6.50,6.50,6.51]
d3 = [9.17,9.16,9.17,9.16,9.16,9.16,9.17,9.16,9.16,9.16]
d4 = [9.43,9.43,9.42,9.43,9.42,9.43,9.42,9.44,9.43,9.43]

aoff = [0,0,0,0,0]
a1 = [28.85,28.6,28.4,28.7,28.0]
a2 = [39.75,39.8,39.0,39.6,39.8]
a3 = [160.65,160.60,160.25,160.4,160.6]
a4 = [25.7,25.35,25.3,26,25.5]

f = open("kristall_abmessungen_tab.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{rrrr}\\\\\n")
f.write(" $d_1$ / mm & $d_2$ / mm & $d_3$ / mm & $d_4$ / mm  \\\\\n ")
f.write("\\hline\n")
for i in range(10):
    f.write(str(custom_round(d1[i],2)) + " & " + str(custom_round(d2[i],2)) + " & " + str(custom_round(d3[i],2)) + " & " + str(custom_round(d4[i],2)))
    if i != 9:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()



f = open("kristall_winkel_tab.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{r|rrrr}\\\\\n")
f.write(" $\\alpha_\\text{off}$ / ${}^\circ$ & $\\alpha_1$ / ${}^\circ$ & $\\alpha_2$ / ${}^\circ$ & $\\alpha_3$ / ${}^\circ$ & $\\alpha_4$ / ${}^\circ$  \\\\\n ")
f.write("\\hline\n")
for i in range(5):
    f.write(str(custom_round(aoff[i],2)) + " & " + str(custom_round(a1[i],2)) + " & " + str(custom_round(a2[i],2))  + " & " + str(custom_round(a3[i],2)) + " & " + str(custom_round(a4[i],2)))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()



def calc_beta(alpha, offset, l):
    res = 0
    for i in range(5):
        res += alpha[i]-offset[i]
    res /= 5
    
    ret = [res]*5
    ret[1] += 180
    ret[2] -= 180
    ret[3] += 360
    ret[4] -= 360
    
    for i in range(5):
        ret[i] /= l
    return ret


colored_values = []

def col(num):
    if abs(abs(num)-21) <= 1:
        colored_values.append(abs(num))
        return "{\\color{red} " + str(custom_round(num,2)) + "}"
    else:
        return str(custom_round(num,2))


f = open("kristall_auswertung_tab.tex", "w", encoding='utf-8')
f.write("\\begin{tabular}{rrrrr}\\\\\n")
f.write(" $x$ / ${}^\\circ$ & $\\beta_1$ / ${}^\\circ$ & $\\beta_2$ / ${}^\\circ$ & $\\beta_3$ / ${}^\\circ$ & $\\beta_4$ / ${}^\\circ$  \\\\\n ")
beta1 = calc_beta(a1, aoff, avg(d1))
beta2 = calc_beta(a2, aoff, avg(d2))
beta3 = calc_beta(a3, aoff, avg(d3))
beta4 = calc_beta(a4, aoff, avg(d4))

x_winkel = [0, 180, -180, 360, -360]

f.write("\\hline\n")
for i in range(5):
    f.write("$" + str(x_winkel[i]) + "~^\\circ$ & " + str(col(beta1[i])) + " & " + str(col(beta2[i])) + " & " + str(col(beta3[i])) + " & " + str(col(beta4[i])))
    if i != 4:
        f.write("\\\\")
    f.write("\n")
f.write("\\end{tabular}")
f.close()


f = open("kristall_auswertung_ergebnis.tex", "w", encoding='utf-8')
f.write("\\begin{align*}\\\\\n \\beta = (" + str(custom_round(sum(colored_values)/len(colored_values),2)) + " \\pm " + str(custom_round(stdev(colored_values,2))) + ")~^\\circ\\\\\n\\end{align*}")
f.close()        

