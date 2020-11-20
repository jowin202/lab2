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
        values = line.split("\t")
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

def mult_two_lists(list1,list2):
    res_list = []
    if len(list1) != len(list2):
        print("weird error 2")
        exit(1)
    for i in range(len(list1)):
        res_list.append(list1[i] * list2[i])
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
refspec_lambda, refspec_I = read_csv("daten_moodle/FF-ref.csv")
blau_lambda, blau_I = read_csv("daten_moodle/FF-blau.csv")
rot_lambda, rot_I = read_csv("daten_moodle/FF-rot.csv")
gelb_lambda, gelb_I = read_csv("daten_moodle/FF-gelb.csv")
br_lambda, br_I = read_csv("daten_moodle/FF-blau_rot.csv")
bg_lambda, bg_I = read_csv("daten_moodle/FF-blau_gelb.csv")




T_blau = divide_two_lists(blau_I,refspec_I)
T_rot = divide_two_lists(rot_I,refspec_I)
T_gelb = divide_two_lists(gelb_I,refspec_I)
T_br = divide_two_lists(br_I,refspec_I)
T_bg = divide_two_lists(bg_I,refspec_I)

E_blau = log_of_a_list(divide_two_lists(refspec_I,blau_I))
E_rot = log_of_a_list(divide_two_lists(refspec_I,rot_I))
E_gelb = log_of_a_list(divide_two_lists(refspec_I,gelb_I))
E_br = log_of_a_list(divide_two_lists(refspec_I,br_I))
E_bg = log_of_a_list(divide_two_lists(refspec_I,bg_I))



fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(refspec_lambda, refspec_I, 'black')
ax.plot(blau_lambda, blau_I, 'blue')
ax.plot(rot_lambda, rot_I, 'red')
#ax.plot(rot_lambda, gelb_I, 'yellow')
ax.plot(br_lambda, br_I, 'magenta')
#ax.plot(bg_lambda, bg_I, 'green')
#ax.legend(['Referenzspektrum (kein Filter)', 'Filter blau', 'Filter rot', 'Filter gelb', 'Filter Blau Rot', 'Filter Blau gelb'])
ax.legend(['Referenzspektrum (kein Filter)', 'Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten nach Filter')
plt.savefig("FF_Intensitaeten.png")

fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(blau_lambda, T_blau, 'blue')
ax.plot(rot_lambda, T_rot, 'red')
#ax.plot(gelb_lambda, T_gelb, 'yellow')
ax.plot(br_lambda, T_br, 'magenta')
#ax.plot(bg_lambda, T_bg, 'green')
#ax.legend(['Filter blau', 'Filter rot', 'Filter gelb', 'Filter Blau Rot', 'Filter Blau Gelb'])
ax.legend(['Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('T / 1')
ax.set_title('Transmissionen der Filter')
plt.savefig("FF_Transmissionen.png")


fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 3])
ax.plot(blau_lambda, E_blau, 'blue')
ax.plot(rot_lambda, E_rot, 'red')
#ax.plot(rot_lambda, E_gelb, 'yellow')
ax.plot(br_lambda, E_br, 'magenta')
#ax.plot(br_lambda, E_bg, 'green')
#ax.legend(['Filter blau', 'Filter rot', 'Filter gelb', 'Filter Blau Rot', 'Filter Blau Gelb'])
ax.legend(['Filter blau', 'Filter rot', 'Filter Blau Rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('E / 1')
ax.set_title('Exktionenen der Filter')
plt.savefig("FF_Extinktionen.png")




fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 3])
ax.plot(br_lambda, E_br, 'magenta')
ax.plot(blau_lambda, add_two_lists(E_blau, E_rot), 'gray')
ax.legend(['Filter Blau Rot','Filter blau + Filter rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('E / 1')
ax.set_title('Addition der Extinktionen der Filter')
plt.savefig("FF_Extinktionen_addition_1.png")

fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1.5])
ax.plot(br_lambda, T_br, 'magenta')
ax.plot(blau_lambda, mult_two_lists(T_blau, T_rot), 'gray')
ax.legend(['Filter Blau Rot','Filter blau * Filter rot'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('T / 1')
ax.set_title('Multiplikation der Transmissionen der Filter')
plt.savefig("FF_Extinktionen_multiplikation_1.png")



fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 3])
ax.plot(br_lambda, E_bg, 'green')
ax.plot(blau_lambda, add_two_lists(E_blau, E_gelb), 'gray')
ax.legend(['Filter Blau Rot','Filter blau + Filter gelb'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('E / 1')
ax.set_title('Addition Exktionenen der Filter')
plt.savefig("FF_Extinktionen_addition_2.png")




MB1_Ref_Lambda = []
MB1_Ref_I = []
MB1_Lambda = []
MB1_I = []

MB2_Ref_Lambda = []
MB2_Ref_I = []
MB2_Lambda = []
MB2_I = []


for i in range(5):
    ref_l, ref_I = read_csv("daten_moodle/MB_ref1" + str(i+1) + ".csv")
    l, I = read_csv("daten_moodle/MB_1" + str(i+1) + ".csv")
    
    MB1_Ref_Lambda.append(ref_l)
    MB1_Ref_I.append(ref_I)
    
    MB1_Lambda.append(l)
    MB1_I.append(I)
    
    
for i in range(5):
    ref_l, ref_I = read_csv("daten_moodle/MB_ref2" + str(i+1) + ".csv")
    l, I = read_csv("daten_moodle/MB_2" + str(i+1) + ".csv")
    
    MB2_Ref_Lambda.append(ref_l)
    MB2_Ref_I.append(ref_I)
    
    MB2_Lambda.append(l)
    MB2_I.append(I)


MB1_Ref_Lambda_Final = average(MB1_Ref_Lambda)
MB1_Ref_I_Final = average(MB1_Ref_I)
MB1_Lambda_Final = average(MB1_Lambda)
MB1_I_Final = average(MB1_I)

MB2_Ref_Lambda_Final = average(MB2_Ref_Lambda)
MB2_Ref_I_Final = average(MB2_Ref_I)
MB2_Lambda_Final = average(MB2_Lambda)
MB2_I_Final = average(MB2_I)



MB_1_T = divide_two_lists(MB1_I_Final,MB1_Ref_I_Final)
MB_2_T = divide_two_lists(MB2_I_Final,MB2_Ref_I_Final)


MB_1_E = log_of_a_list(divide_two_lists(MB1_Ref_I_Final,MB1_I_Final))
MB_2_E = log_of_a_list(divide_two_lists(MB2_Ref_I_Final,MB2_I_Final))



MB_1_Ref_664 = filter664(MB1_Ref_Lambda_Final, MB1_Ref_I_Final)
MB_1_I_664 = filter664(MB1_Lambda_Final, MB1_I_Final)
MB_2_Ref_664 = filter664(MB2_Ref_Lambda_Final, MB2_Ref_I_Final)
MB_2_I_664 = filter664(MB2_Lambda_Final, MB2_I_Final)

d = 1 #cm
Delta_d = 0.001 #cm
eps = 77790 #Liter / (mol cm)
Delta_I = 0.002


c1 = (log(MB_1_Ref_664)/log(10) - log(MB_1_I_664)/log(10))/(d*eps)
Delta_c1 = (log(MB_1_Ref_664)/log(10) - log(MB_1_I_664)/log(10))/(d**2*eps) *Delta_d     +     Delta_I*(1/MB_1_I_664 + 1/MB_1_Ref_664)/(eps*d)

c2 = (log(MB_2_Ref_664)/log(10) - log(MB_2_I_664)/log(10))/(d*eps)
Delta_c2 = (log(MB_2_Ref_664)/log(10) - log(MB_2_I_664)/log(10))/(d**2*eps) *Delta_d     +     Delta_I*(1/MB_2_I_664 + 1/MB_2_Ref_664)/(eps*d)


f = open("MB_ergebnis.tex", "w")
f.write("\\begin{align*}\n")
f.write("c_1 &= (" + str(custom_round(c1*10**6,2)) + " \pm " +  str(custom_round(Delta_c1*10**6,2)) + ")\\cdot 10^{-6}~\\text{mol/Liter}  \n" )
#f.write("c_2 &= (" + str(custom_round(c2*10**6,2)) + " \pm " +  str(custom_round(Delta_c2*10**6,2)) + ")\\cdot 10^{-6}~\\text{mol/Liter}  \n" )
f.write("\\end{align*}\n")





fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(MB1_Ref_Lambda_Final, MB1_Ref_I_Final, 'grey')
ax.plot(MB1_Lambda_Final, MB1_I_Final, 'blue')
ax.legend(['I_0 (Wasser)', 'I (Methylenblau)'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten Methylenblau 1')
plt.savefig("MB_Intensitaeten_1.png")


fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(MB2_Ref_Lambda_Final, MB2_Ref_I_Final, 'grey')
ax.plot(MB2_Lambda_Final, MB2_I_Final, 'blue')
ax.legend(['I_0 (Wasser)', 'I (Methylenblau)'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensitäten Methylenblau 2')
plt.savefig("MB_Intensitaeten_2.png")




fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([400, 800, 0.6, 1])
ax1.plot(MB1_Ref_Lambda_Final, MB_1_T, 'blue')
ax1.legend(['Transmission'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Methylenblau 1')
#plt.savefig("Transmission_Methyl.png")

ax2.axis([400, 800, 0, 0.3])
ax2.plot(MB1_Ref_Lambda_Final, MB_1_E, 'red')
ax2.legend(['Extinktion'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("MB_ET_1.png")


fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([400, 800, 0.6, 1])
ax1.plot(MB2_Ref_Lambda_Final, MB_2_T, 'blue')
ax1.legend(['Transmission'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Methylenblau 2')
#plt.savefig("Transmission_Methyl.png")

ax2.axis([400, 800, 0, 0.3])
ax2.plot(MB2_Ref_Lambda_Final, MB_2_E, 'red')
ax2.legend(['Extinktion'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("MB_ET_2.png")





GP1_Ref_lambda, GP1_Ref_I = read_csv("daten_moodle/GP1_ref.csv")
GP1_lambda, GP1_I = read_csv("daten_moodle/GP1.csv")

GP2_Ref_lambda, GP2_Ref_I = read_csv("daten_moodle/GP2_ref.csv")
GP2_lambda, GP2_I = read_csv("daten_moodle/GP2.csv")

GP1_T = divide_two_lists(GP1_I,GP1_Ref_I)
GP2_T = divide_two_lists(GP2_I,GP2_Ref_I)

GP1_E = log_of_a_list(divide_two_lists(GP1_Ref_I,GP1_I))
GP2_E = log_of_a_list(divide_two_lists(GP2_Ref_I,GP2_I))

GP1_lambda_max, GP1_I_max = find_max(GP1_lambda, GP1_I)
GP2_lambda_max, GP2_I_max = find_max(GP2_lambda, GP2_I)

f = open("GP_max.tex", "w")
f.write("\\begin{align*}\n")
f.write("I_{1,\\text{max}} &= " + str(custom_round(GP1_I_max,2)) + "\\qquad \\text{bei} \qquad \\lambda_1 = " + str(custom_round(GP1_lambda_max,2)) + " \n")
#f.write("I_{2,\\text{max}} &= " + str(custom_round(GP2_I_max,2)) + "\\qquad \\text{bei} \qquad \\lambda_2 = " + str(custom_round(GP2_lambda_max,2)) + " \n")
f.write("\\end{align*}\n")


GP1_max_T_lambda, GP1_max_T = find_transmission_max(GP1_lambda, GP1_T)
GP2_max_T_lambda, GP2_max_T = find_transmission_max(GP2_lambda, GP2_T)


f = open("GP_max_glas_1.tex", "w")
f.write("\\begin{tabular}{cccc}\n")
f.write("m & $\\lambda_m$ / nm & $\\nu_m$ / $\mu$m${}^{-1}$ & $T_{1,m}$ / 1 \\\\\n\\hline")
count = 1
m_list = []
lambda_list = []
lambda_inv_list = []
for i in range(len(GP1_max_T)):
    m_list.append(i+1)
    lambda_list.append(GP1_max_T_lambda[i])
    lambda_inv_list.append(1/GP1_max_T_lambda[i])
    f.write(str(count) + " & " + str(custom_round(GP1_max_T_lambda[i],1)) + " & " + str(custom_round(1000/GP1_max_T_lambda[i],3)) + " & " + str(custom_round(GP1_max_T[i],3)) + "\\\\\n")
    count += 1
f.write("\\end{tabular}\n")
f.close()

GP1_k = calc_k(m_list, lambda_inv_list)


fig, ax = plt.subplots() 
ax.axis([0, 20, 700, 722])
ax.scatter(m_list,lambda_list)
ax.set_xlabel('m / 1')
#ax.set_ylabel('lambda / nm')
#ax.axis([0, 5, 0, 20])
ax.set_title('Regression\nTransmissionsmaxima nach Wellenlänge')
plt.savefig("GP1_scatterplot_1.png")

fig, ax = plt.subplots() 
ax.axis([0, 20, 0.00138, 0.00144])
ax.scatter(m_list,lambda_inv_list)
ax.set_xlabel('m / 1')
#ax.set_ylabel('nu / nm^(-1)')
ax.set_title('Regression\nTransmissionsmaxima nach Wellenzahl')
plt.savefig("GP1_scatterplot_2.png")



f = open("GP_max_glas_2.tex", "w")
f.write("\\begin{tabular}{cccc}\n")
f.write("m & $\\lambda_m$ / nm & $\\nu_m$ / $\mu$m${}^{-1}$ & $T_{2,m}$ / 1 \\\\\n\\hline")
count = 1
m_list = []
lambda_inv_list = []
for i in range(len(GP2_max_T)):
    m_list.append(i+1)
    lambda_inv_list.append(1/GP2_max_T_lambda[i])
    f.write(str(count) + " & " + str(custom_round(GP2_max_T_lambda[i],1)) + " & " + str(custom_round(1000/GP2_max_T_lambda[i],3)) + " & " + str(custom_round(GP2_max_T[i],3)) + "\\\\\n")
    count += 1
f.write("\\end{tabular}\n")
f.close()

GP2_k = calc_k(m_list, lambda_inv_list)











f = open("GP_k.tex", "w")
f.write("\\begin{align*}\n")
f.write("k_1 &= (" + str(custom_round(10**6*GP1_k,2)) + " \pm 0.08)\\cdot 10^{-6}~\\text{nm}^{-1} \n" )
#f.write("k_2 &= (" + str(custom_round(10**6*GP2_k,2)) + " \pm 0.08)\\cdot 10^{-6}~\\text{nm}^{-1} \n" )
f.write("\\end{align*}\n")




np = 1.519
Delta_np = 0.001
Delta_k = 0.08*10**-6
GP_d1 = -1/(2 * np * GP1_k) #minus machen
GP_d2 = -1/(2 * np * GP2_k) #minus machen
delta_d1 = GP_d1/np * Delta_np - GP_d1/GP1_k * Delta_k
delta_d2 = GP_d2/np * Delta_np - GP_d2/GP2_k * Delta_k
f = open("GP_d.tex", "w")
f.write("\\begin{align*}\n")
f.write("d_1 &= (" + str(custom_round(GP_d1*10**-6,2)) + " \pm " + str(custom_round(10**-6*delta_d1,2)) +  ")~\\text{mm} \n" )
#f.write("d_2 &= (" + str(custom_round(GP_d2*10**-6,2)) + " \pm " + str(custom_round(10**-6*delta_d2,2)) +  ")~\\text{mm} \n" )
f.write("\\end{align*}\n")





fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(GP1_Ref_lambda, GP1_Ref_I, 'gray')
ax.plot(GP1_lambda, GP1_I, 'red')
ax.legend(['Referenzspektrum', 'Glasplatte 1'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensität von Glasplatte 1')
plt.savefig("GP_Intensitaet_1.png")




fig, ax = plt.subplots() 
ax.axis([400, 800, 0, 1])
ax.plot(GP2_Ref_lambda, GP2_Ref_I, 'gray')
ax.plot(GP2_lambda, GP2_I, 'red')
ax.legend(['Referenzspektrum', 'Glasplatte 2'])
ax.set_xlabel('lambda / nm')
ax.set_ylabel('I / 1')
ax.set_title('Intensität von Glasplatte 2')
plt.savefig("GP_Intensitaet_2.png")






fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([700, 720, 0.9, 0.95])
ax1.plot(GP1_lambda, GP1_T, 'blue')
ax1.legend(['Transmission Extinktion der Glasplatte 1'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Glasplatte 1')
for m in GP1_max_T_lambda:
    ax1.axvline(x=m)


ax2.axis([700, 720, 0.02, 0.05])
ax2.plot(GP1_lambda, GP1_E, 'red')
ax2.legend(['Extinktion der Glasplatte 1'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("GP1_ET.png")




fig, (ax1,ax2) = plt.subplots(2,1) 
ax1.axis([700, 720, 0.90, 0.95])
ax1.plot(GP2_lambda, GP2_T, 'blue')
ax1.legend(['Transmission Extinktion der Glasplatte 2'])
ax1.set_ylabel('T / 1')
ax1.set_title('Transmission / Extinktion Glasplatte 2')
for m in GP2_max_T_lambda:
    ax1.axvline(x=m)


ax2.axis([700, 720, 0.02, 0.05])
ax2.plot(GP2_lambda, GP2_E, 'red')
ax2.legend(['Extinktion der Glasplatte 2'])
ax2.set_xlabel('lambda / nm')
ax2.set_ylabel('E / 1')
plt.savefig("GP2_ET.png")



