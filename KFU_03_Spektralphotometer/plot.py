import numpy as np
import matplotlib.pyplot as plt
from math import log

def custom_round(num,n=2):
    if n == 1:
        return '{:.1f}'.format(round(num,1))
    if n == 3:
        return '{:.3f}'.format(round(num,3))
    else:
        return '{:.2f}'.format(round(num,2))


def read_csv(filename):
    f = open(filename, "r")
    file_data = f.read()
    f.close()


    refspec_lines = file_data.split("\n")
    col1 = []
    col2 = []

    for line in refspec_lines:
        values = line.split(";")
        if len(values) < 2:
            continue
        values[0] = values[0].replace(",", ".")
        values[1] = values[1].replace(",", ".")
        if values[0] == "Column1":
            continue
        val1 = float(values[0])
        val2 = float(values[1])
        if val1 >= 400 and val1 <= 800:
            col1.append(val1)
            col2.append(val2)
    return col1, col2

def all_equal(data):
    return all(x == data[0] for x in data)


def average(data_list):
    result_list = []
    
    num_entries = -1
    num_lists = len(data_list)
    
    for list_element in data_list:
        if num_entries == -1:
            num_entries = len(list_element)
        else:
            if num_entries != len(list_element):
                print("Error: nicht alle Listen gleich lang")
                exit(1)

    for i in range(num_entries):
        element = 0
        for list_element in data_list:
            element += list_element[i]
        element /= num_lists
        result_list.append(element)
    return result_list



def read_one_color(filename_list):
    l_list = []
    I_list = []
    for filename in filename_list:
        l, I = read_csv(filename)
        l_list.append(l)
        I_list.append(I)
        
    if not all_equal(l_list):
        print("Weird error")
        exit(1)

    res_lambda_list = l_list[0]
    res_I_list = average(I_list)
    return res_lambda_list, res_I_list


def divide_two_lists(list1, list2):
    res_list = []
    if len(list1) != len(list2):
        print("weird error 2")
        exit(1)
    for i in range(len(list1)):
        res_list.append(abs(list1[i] / list2[i]))
    return res_list

def subtract_two_lists(list1, list2):
    res_list = []
    if len(list1) != len(list2):
        print("weird error 2")
        exit(1)
    for i in range(len(list1)):
        res_list.append(list1[i] - list2[i])
    return res_list

def add_two_lists(list1, list2):
    res_list = []
    if len(list1) != len(list2):
        print("weird error 2")
        exit(1)
    for i in range(len(list1)):
        res_list.append(list1[i] + list2[i])
    return res_list


def log_of_a_list(list1):
    res_list = []
    for elem in list1:
        res_list.append(log(elem)/log(10))
    return res_list



def calc_k(list1, list2):
    if len(list1) != len(list2):
        print("weird error 2")
        exit(1)
    sum_xy = 0
    sum_x2 = 0
    sum_x = 0
    sum_y = 0
    length = len(list1)
    for i in range(len(list1)):
        sum_xy += list1[i]*list2[i]
        sum_x2 += list1[i]*list1[i]
        sum_x += list1[i]
        sum_y += list2[i]
    return (sum_xy - (sum_x*sum_y)/length)/(sum_x2 - sum_x**2/length)

def filter664(list1, list2):
    l1 = -1
    l2 = -1
    E1 = -1
    E2 = -1
    if len(list1) != len(list2):
        print("weird error 3")
        exit(1)
    for i in range(len(list1)):
        if list1[i] > 664:
            l2 = list1[i]
            E2 = list2[i]
            break
        l1 = list1[i]
        E1 = list2[i]
    k = (E2-E1)/(l2-l1) # lin interpolation
    return E1 + k*(664-l1)
    


def find_max(list1,list2):
    maximum = -1
    max_i = -1
    if len(list1) != len(list2):
        print("weird error 3")
        exit(1)
    for i in range(len(list1)):
        if list2[i] > maximum:
            max_i = i
            maximum = list2[i]
    return list1[max_i], maximum


def find_transmission_max(list1,list2):
    if len(list1) != len(list2):
        print("weird error 3")
        exit(1)
    
    max_lambda_list = []
    max_transmission_list = []
    for i in range(len(list1)):
        if list1[i] > 700 and list1[i] < 720:
            if list2[i] > list2[i-1] and list2[i] > list2[i-2]  and  list2[i] > list2[i-3]  :
                if list2[i] > list2[i+1] and list2[i] > list2[i+2]  and  list2[i] > list2[i+3]:
                    max_lambda_list.append(list1[i])
                    max_transmission_list.append(list2[i])
    return max_lambda_list, max_transmission_list
                    
            
            
    
#referenzspektrum
refspec_lambda, refspec_I = read_csv("daten/1/I0.csv")

#farbfilter farbe 1
blau_lambda, blau_I = read_one_color(["daten/1/I Farbfilter blau 1.csv","daten/1/I Farbfilter blau 2.csv","daten/1/I Farbfilter blau 3.csv", "daten/1/I Farbfilter blau 4.csv"])
rot_lambda, rot_I = read_one_color(["daten/1/I Farbfilter rot 1.csv","daten/1/I Farbfilter rot 2.csv","daten/1/I Farbfilter rot 3.csv", "daten/1/I Farbfilter rot 4.csv"])

br_lambda, br_I = read_one_color(["daten/1/I Farbfilter blau rot 1.csv","daten/1/I Farbfilter blau rot 2.csv","daten/1/I Farbfilter blau rot 3.csv", "daten/1/I Farbfilter blau rot 4.csv"])
rb_lambda, rb_I = read_one_color(["daten/1/I Farbfilter rot blau 1.csv","daten/1/I Farbfilter rot blau 2.csv","daten/1/I Farbfilter rot blau 3.csv", "daten/1/I Farbfilter rot blau 4.csv"])


E_blau = log_of_a_list(divide_two_lists(refspec_I,blau_I))
E_rot = log_of_a_list(divide_two_lists(refspec_I,rot_I))
E_br = log_of_a_list(divide_two_lists(refspec_I,br_I))


#methyldings
methylblau_lambda, methylblau_I = read_one_color(["daten/3/I Küvette Methylblau 1.csv","daten/3/I Küvette Methylblau 2.csv","daten/3/I Küvette Methylblau 3.csv"])
wasser_lambda, wasser_I = read_one_color(["daten/3/I Küvette Wasser.csv"])

transmission_methyl = divide_two_lists(methylblau_I,wasser_I)
extinktion_methyl = log_of_a_list(divide_two_lists(wasser_I,methylblau_I))

I_Methyl_664 = filter664(methylblau_lambda, methylblau_I)
I_Wasser_664 = filter664(methylblau_lambda, wasser_I)

d = 1 #cm
Delta_d = 0.001 #cm
eps = 77790 #Liter / (mol cm)
Delta_I = 0.002

c = (log(I_Wasser_664)/log(10) - log(I_Methyl_664)/log(10))/(d*eps)
Delta_c = (log(I_Wasser_664)/log(10) - log(I_Methyl_664)/log(10))/(d**2*eps) *Delta_d     +     Delta_I*(1/I_Methyl_664 + 1/I_Wasser_664)/(eps*d)

print("c: " + str( c ) )

print("Delta c: " + str(  Delta_c ))

f = open("methyl_ergebnis.tex", "w")
f.write("\\begin{align*}\n")
f.write("c = (" + str(custom_round(c*10**6,2)) + " \pm " +  str(custom_round(Delta_c*10**6,2)) + ")\\cdot 10^6~\\text{mol/Liter} \n" )
f.write("\\end{align*}\n")






#Glasplatte
glas_lambda, glas_ref_I = read_one_color(["daten/4/I0.csv"])
glas_lambda, glas_I = read_one_color(["daten/4/I Glas 1.csv","daten/4/I Glas 2.csv","daten/4/I Glas 3.csv","daten/4/I Glas 4.csv"])

transmission_glas = divide_two_lists(glas_I,glas_ref_I)
extinktion_glas = log_of_a_list(divide_two_lists(glas_ref_I,glas_I))

glas_max_lambda, glas_max_I = find_max(glas_lambda, glas_I)

f = open("glas_max.tex", "w")
f.write("\\begin{align*}\n")
f.write("I_{\\text{max}} = " + str(custom_round(glas_max_I,2)) + "\\qquad \\text{bei} \qquad \\lambda = " + str(custom_round(glas_max_lambda,2)) + " \n")
f.write("\\end{align*}\n")

glas_plot_limit = (10*round(glas_max_lambda/10))-10



transmission_max_lambda_glas,transmission_max_glas = find_transmission_max(glas_lambda, transmission_glas)
f = open("glas_max_trans_tab.tex", "w")
f.write("\\begin{tabular}{cccc}\n")
f.write("m & $\\lambda_m$ / nm & $\\nu_m$ / $\mu$m${}^{-1}$ & T / 1 \\\\\n\\hline")
count = 1
m_list = []
lambda_inv_list = []
for i in range(len(transmission_max_lambda_glas)):
    m_list.append(i+1)
    lambda_inv_list.append(1/transmission_max_lambda_glas[i])
    f.write(str(count) + " & " + str(custom_round(transmission_max_lambda_glas[i],1)) + " & " + str(custom_round(1000/transmission_max_lambda_glas[i],3)) + " & " + str(custom_round(transmission_max_glas[i],3)) + "\\\\\n")
    count += 1
f.write("\\end{tabular}\n")

glas_k = calc_k(m_list, lambda_inv_list)

f = open("glas_k_ergebnis.tex", "w")
f.write("\\begin{align*}\n")
f.write("k = (" + str(custom_round(10**6*glas_k,2)) + " \pm 0.08)\\cdot 10^{-6}~\\text{nm}^{-1} \n" )
f.write("\\end{align*}\n")



np = 1.519
Delta_np = 0.001
Delta_k = 0.08*10**-6
d = -1/(2 * np * glas_k) #minus machen
delta_d = d/np * Delta_np - d/glas_k * Delta_k
f = open("glas_d_ergebnis.tex", "w")
f.write("\\begin{align*}\n")
f.write("d = (" + str(custom_round(d*10**-6,2)) + " \pm " + str(custom_round(10**-6*delta_d,2)) +  ")~\\text{mm} \n" )
f.write("\\end{align*}\n")




fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(refspec_lambda, refspec_I, 'green')
ax.plot(blau_lambda, blau_I, 'blue')
ax.plot(rot_lambda, rot_I, 'red')
ax.plot(br_lambda, br_I, 'magenta')
#ax.plot(rb_lambda, rb_I, 'orange')
ax.legend(['Referenzspektrum (kein Filter)', 'Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten nach Filter')
plt.savefig("Intensitaeten.png")

fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(blau_lambda, divide_two_lists(blau_I,refspec_I), 'blue')
ax.plot(rot_lambda, divide_two_lists(rot_I,refspec_I), 'red')
ax.plot(br_lambda, divide_two_lists(br_I,refspec_I), 'magenta')
#ax.plot(rb_lambda, rb_I, 'orange')
ax.legend(['Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('T / 1')
ax.set_title('Transmissionen der Filter')
plt.savefig("Transmissionen.png")


fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 3])
ax.plot(blau_lambda, E_blau, 'blue')
ax.plot(rot_lambda, E_rot, 'red')
ax.plot(br_lambda, E_br, 'magenta')
#ax.plot(rb_lambda, rb_I, 'orange')
ax.legend(['Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('E / 1')
ax.set_title('Exktionenen der Filter')
plt.savefig("Extinktionen.png")


fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 3])
ax.plot(br_lambda, E_br, 'magenta')
ax.plot(blau_lambda, add_two_lists(E_blau, E_rot), 'orange')
ax.legend(['Filter Blau Rot','Filter blau + Filter rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('E / 1')
ax.set_title('Addition Exktionenen der Filter')
plt.savefig("Extinktionen_addition.png")



fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
#ax.plot(refspec_lambda, refspec_I, 'green')
#ax.plot(blau_lambda, blau_I, 'blue')
#ax.plot(rot_lambda, rot_I, 'red')
ax.plot(br_lambda, br_I, 'magenta', linewidth=1)
ax.plot(rb_lambda, rb_I, 'orange', linewidth=1)
ax.legend(['Filter Blau Rot','Filter Rot Blau'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Reihenfolge der Filter')
plt.savefig("reihenfolge1.png")
fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])


fig, ax = plt.subplots() 
ax.axis([400, 800, -0.007, 0.003])
#ax.plot(refspec_lambda, refspec_I, 'green')
#ax.plot(blau_lambda, blau_I, 'blue')
#ax.plot(rot_lambda, rot_I, 'red')
ax.plot(br_lambda, subtract_two_lists(br_I,rb_I), 'magenta', linewidth=1)
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Differenz der Intensitäten bei\n Vertauschung der Reihenfolge der Filter')
plt.savefig("reihenfolge2.png")


fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(wasser_lambda, wasser_I, 'grey')
ax.plot(methylblau_lambda, methylblau_I, 'blue')
ax.legend(['I_0 (Wasser)', 'I (Methylenblau)'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten Methylenblau')
plt.savefig("Intensitaeten_Methyl.png")



fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([400, 800, 0.6, 1])
ax1.plot(methylblau_lambda, transmission_methyl, 'blue')
ax1.legend(['Transmission'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Methylenblau')
#plt.savefig("Transmission_Methyl.png")

ax2.axis([400, 800, 0, 0.3])
ax2.plot(methylblau_lambda, extinktion_methyl, 'red')
ax2.legend(['Extinktion'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("Transmission_Extinktion_Methyl.png")





#glas

fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(glas_lambda, glas_ref_I, 'gray')
ax.plot(glas_lambda, glas_I, 'red')
ax.legend(['Referenzspektrum (kein Glas)', 'Glas'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten mit und ohne Glasplatte')
plt.savefig("Glas_Intensitaeten.png")


fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([glas_plot_limit, glas_plot_limit+20, 0.89, 0.92])
ax1.plot(glas_lambda, transmission_glas, 'blue')
ax1.legend(['Transmission Extinktion der Glasplatte'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Glasplatte')
for m in transmission_max_lambda_glas:
    ax1.axvline(x=m)


ax2.axis([glas_plot_limit, glas_plot_limit+20, 0.04, 0.05])
ax2.plot(glas_lambda, extinktion_glas, 'red')
ax2.legend(['Extinktion der Glasplatte'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("Glas_Transmission_Extinktion.png")

