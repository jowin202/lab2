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
        values = line.split(",")
        if len(values) < 2:
            continue
        values[0] = values[0].replace(",", ".")
        values[1] = values[1].replace(",", ".")
        if values[0] == "x-axis" or values[0] == "second":
            continue
        val1 = 1000000000*float(values[0])
        val2 = float(values[1])

        col1.append(val1)
        col2.append(val2)
    return col1, col2







#task 1a
t1a_ch1_100, V1a_ch1_100 = read_csv("daten/scope_0_1.csv")
t1a_ch2_100, V1a_ch2_100 = read_csv("daten/scope_0_2.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1a_ch1_100, V1a_ch1_100, 'grey')
ax.plot(t1a_ch2_100, V1a_ch2_100, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 a,  t=100 ns')
plt.savefig("bilder/task1a/task1a_100ns.png")

#ax.set_title('Aufgabe 3,  t=100 ns')
#plt.savefig("bilder/task3/task3_100ns.png")
plt.close()



t1a_ch1_240, V1a_ch1_240 = read_csv("daten/scope_1_1.csv")
t1a_ch2_240, V1a_ch2_240 = read_csv("daten/scope_1_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1a_ch1_240, V1a_ch1_240, 'grey')
ax.plot(t1a_ch2_240, V1a_ch2_240, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 a,  t=240 ns')
plt.savefig("bilder/task1a/task1a_240ns.png")

#ax.set_title('Aufgabe 3,  t=240 ns')
#plt.savefig("bilder/task3/task3_240ns.png")
plt.close()





t1a_ch1_500, V1a_ch1_500 = read_csv("daten/scope_2_1.csv")
t1a_ch2_500, V1a_ch2_500 = read_csv("daten/scope_2_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1a_ch1_500, V1a_ch1_500, 'grey')
ax.plot(t1a_ch2_500, V1a_ch2_500, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 a,  t=500 ns')
plt.savefig("bilder/task1a/task1a_500ns.png")
plt.close()






t1a_ch1_750, V1a_ch1_750 = read_csv("daten/scope_3_1.csv")
t1a_ch2_750, V1a_ch2_750 = read_csv("daten/scope_3_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1a_ch1_750, V1a_ch1_750, 'grey')
ax.plot(t1a_ch2_750, V1a_ch2_750, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 a,  t=750 ns')
plt.savefig("bilder/task1a/task1a_750ns.png")
plt.close()






#task1b




t1b_ch1_150, V1b_ch1_150 = read_csv("daten/scope_6_1.csv")
t1b_ch2_150, V1b_ch2_150 = read_csv("daten/scope_6_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1b_ch1_150, V1b_ch1_150, 'grey')
ax.plot(t1b_ch2_150, V1b_ch2_150, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 b,  t=150 ns')
plt.savefig("bilder/task1b/task1b_150ns.png")
plt.close()




t1b_ch1_2300, V1b_ch1_2300 = read_csv("daten/scope_7_1.csv")
t1b_ch2_2300, V1b_ch2_2300 = read_csv("daten/scope_7_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1b_ch1_2300, V1b_ch1_2300, 'grey')
ax.plot(t1b_ch2_2300, V1b_ch2_2300, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 b,  t=2300 ns')
plt.savefig("bilder/task1b/task1b_2300ns.png")
plt.close()






#task1c


t1c_ch1_150, V1c_ch1_150 = read_csv("daten/scope_8_1.csv")
t1c_ch2_150, V1c_ch2_150 = read_csv("daten/scope_8_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1c_ch1_150, V1c_ch1_150, 'grey')
ax.plot(t1c_ch2_150, V1c_ch2_150, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 c,  t=150 ns')
plt.savefig("bilder/task1c/task1c_150ns.png")
plt.close()


t1c_ch1_2650, V1c_ch1_2650 = read_csv("daten/scope_9_1.csv")
t1c_ch2_2650, V1c_ch2_2650 = read_csv("daten/scope_9_2.csv")

fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t1c_ch1_2650, V1c_ch1_2650, 'grey')
ax.plot(t1c_ch2_2650, V1c_ch2_2650, 'blue')
ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 1 c,  t=2650 ns')
plt.savefig("bilder/task1c/task1c_2650ns.png")
plt.close()







#task 2 R1
t2_R1, V2_R1 = read_csv("daten/scope_10_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R1, V2_R1, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R1)')
plt.savefig("bilder/task2/task2_R1.png")
plt.close()



#task 2 R2
t2_R2, V2_R2 = read_csv("daten/scope_11_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R2, V2_R2, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R2)')
plt.savefig("bilder/task2/task2_R2.png")
plt.close()



#task 2 R3
t2_R3, V2_R3 = read_csv("daten/scope_12_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R3, V2_R3, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R3)')
plt.savefig("bilder/task2/task2_R3.png")
plt.close()




#task 2 R4
t2_R4, V2_R4 = read_csv("daten/scope_13_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R4, V2_R4, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R4)')
plt.savefig("bilder/task2/task2_R4.png")
plt.close()





#task 2 R5
t2_R5, V2_R5 = read_csv("daten/scope_14_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R5, V2_R5, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R5)')
plt.savefig("bilder/task2/task2_R5.png")
plt.close()




#task 2 R6
t2_R6, V2_R6 = read_csv("daten/scope_15_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R6, V2_R6, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R6)')
plt.savefig("bilder/task2/task2_R6.png")
plt.close()




#task 2 R7
t2_R7, V2_R7 = read_csv("daten/scope_16_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R7, V2_R7, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R7)')
plt.savefig("bilder/task2/task2_R7.png")
plt.close()




#task 2 R8
t2_R8, V2_R8 = read_csv("daten/scope_17_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R8, V2_R8, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R8)')
plt.savefig("bilder/task2/task2_R8.png")
plt.close()




#task 2 R9
t2_R9, V2_R9 = read_csv("daten/scope_18_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R9, V2_R9, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R9)')
plt.savefig("bilder/task2/task2_R9.png")
plt.close()



#task 2 R10
t2_R10, V2_R10 = read_csv("daten/scope_19_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R10, V2_R10, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R10)')
plt.savefig("bilder/task2/task2_R10.png")
plt.close()




#task 2 R11
t2_R11, V2_R11 = read_csv("daten/scope_20_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R11, V2_R11, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (R11)')
plt.savefig("bilder/task2/task2_R11.png")
plt.close()




#task 2 kurz
t2_kurz, V2_kurz = read_csv("daten/scope_21_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_kurz, V2_kurz, 'blue')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (Kurzschluss)')
plt.savefig("bilder/task2/task2_kurz.png")
plt.close()





for i in range(len(V2_R1)):
    V2_R1[i] += 1
    V2_R2[i] += 0.967
    V2_R3[i] += 0.939
    V2_R4[i] += 0.887
    V2_R5[i] += 0.791
    V2_R6[i] += 0.676
    V2_R7[i] += 0.588
    V2_R8[i] += 0.499
    V2_R9[i] += 0.414
    V2_R10[i] += 0.228
    V2_R11[i] += 0.295
    



#summary
fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t2_R10, V2_R10, 'orange')
ax.plot(t2_R11, V2_R11, 'orange')
ax.plot(t2_R1, V2_R1, 'blue')
ax.plot(t2_R2, V2_R2, 'blue')
ax.plot(t2_R3, V2_R3, 'blue')
ax.plot(t2_R4, V2_R4, 'blue')
ax.plot(t2_R5, V2_R5, 'blue')
ax.plot(t2_R6, V2_R6, 'blue')
ax.plot(t2_R7, V2_R7, 'gray')
ax.plot(t2_R8, V2_R8, 'gray')
ax.plot(t2_R9, V2_R9, 'orange')
#ax.legend(['Kabeleingang', 'Kabelausgang'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 2 (Zusammenfassung)')
plt.savefig("bilder/task2/task2_summary.png")
plt.close()











#task 5
t5_s22, V5_s22 = read_csv("daten/scope_22_1.csv")
t5_s23, V5_s23 = read_csv("daten/scope_23_1.csv")


fig, ax = plt.subplots() 
#ax.axis([400, 800, 0, 1])
ax.plot(t5_s22, V5_s22, 'blue')
ax.plot(t5_s23, V5_s23, 'red')
ax.legend(['scope 22', 'scope 23'])
ax.set_xlabel('time / ns')
ax.set_ylabel('Voltage / V')
ax.set_title('Aufgabe 5')
plt.savefig("bilder/task5/task5.png")

