def custom_round(num,n=2):
    if n == 1:
        return '{:.1f}'.format(round(num,1))
    if n == 3:
        return '{:.3f}'.format(round(num,3))
    else:
        return '{:.2f}'.format(round(num,2))
    
    
R = 8.31446261815324 # Wikipedia


z = 1 # silber ist 1-wertig
t = 1800 #s = halbe std
I = 0.1 #100 mA
Delta_I = 0.002 #mA
Delta_t = 1 #s
delta_m = 0.1/1000 #g

molmasse = 107.8682/1000 #molmasse silber in kg
R = 8.31446261815324 # Wikipedia

avogadro = 6.02214076*10**23






anode_vorher = 9.639 #g
anode_nachher = 9.486 #g
diff_anode_in_kg = abs(anode_vorher - anode_nachher)/1000

kathode_vorher = 9.641 #g
kathode_nachher = 9.861 #g
diff_kathode_in_kg = abs(kathode_vorher - kathode_nachher)/1000

print("Silbercoulombmeter (JW):")
F_Kathode = I*t*molmasse/(diff_kathode_in_kg*z)
F_Anode = I*t*molmasse/(diff_anode_in_kg*z)
Delta_F_Kathode = Delta_I*t*molmasse/(diff_kathode_in_kg*z) + I*Delta_t*molmasse/(diff_kathode_in_kg*z) + I*t*molmasse/(diff_kathode_in_kg**2*z)*delta_m
Delta_F_Anode = Delta_I*t*molmasse/(diff_anode_in_kg*z) + I*Delta_t*molmasse/(diff_anode_in_kg*z) + I*t*molmasse/(diff_anode_in_kg**2*z)*delta_m
print(str(round(F_Kathode,2)) + "   "  + str(Delta_F_Kathode))
print(str(round(F_Anode,2)) + "   "  + str(Delta_F_Anode))

e_kathode = F_Kathode/avogadro
delta_e_kathode = Delta_F_Kathode/avogadro
e_anode = F_Anode/avogadro
delta_e_anode = F_Anode/avogadro

f = open("silber_jw.tex", "w")
f.write("\\begin{align*}\n")
f.write("F_\\text{Kathode} &= (" + str(round(F_Kathode/1000)) + " \\pm " + str(round(Delta_F_Kathode/1000)) + ")~\\text{kC/mol}\\\\\n")
f.write("F_\\text{Anode} &= (" + str(round(F_Anode/1000)) + " \\pm " + str(round(Delta_F_Anode/1000)) + ")~\\text{kC/mol} \\\\\n")
f.write("e_\\text{Kathode} &= (" + str(custom_round(e_kathode*10**19,2)) + " \\pm " + str(custom_round(delta_e_kathode*10**19,2)) + ")\\cdot 10^{-19}~C \\\\\n")
f.write("e_\\text{Anode} &= (" + str(custom_round(e_anode*10**19,2)) + " \\pm " + str(custom_round(delta_e_anode*10**19,2)) + ")\\cdot 10^{-19}~C  \n")
f.write("\\end{align*}\n")




anode_vorher = 6.756 #g
anode_nachher = 6.237 #g
diff_anode_in_kg = abs(anode_vorher - anode_nachher)/1000

kathode_vorher = 9.406 #g
kathode_nachher = 9.613 #g
diff_kathode_in_kg = abs(kathode_vorher - kathode_nachher)/1000

print("Silbercoulombmeter (TM):")
F_Kathode = I*t*molmasse/(diff_kathode_in_kg*z)
F_Anode = I*t*molmasse/(diff_anode_in_kg*z)

Delta_F_Kathode = Delta_I*t*molmasse/(diff_kathode_in_kg*z) + I*Delta_t*molmasse/(diff_kathode_in_kg*z) + I*t*molmasse/(diff_kathode_in_kg**2*z)*delta_m
Delta_F_Anode = Delta_I*t*molmasse/(diff_anode_in_kg*z) + I*Delta_t*molmasse/(diff_anode_in_kg*z) + I*t*molmasse/(diff_anode_in_kg**2*z)*delta_m
print(str(round(F_Kathode,2)) + "   "  + str(Delta_F_Kathode))
print(str(round(F_Anode,2)) + "   "  + str(Delta_F_Anode))

e_kathode = F_Kathode/avogadro
delta_e_kathode = Delta_F_Kathode/avogadro
e_anode = F_Anode/avogadro
delta_e_anode = F_Anode/avogadro

f = open("silber_tm.tex", "w")
f.write("\\begin{align*}\n")
f.write("F_\\text{Kathode} &= (" + str(round(F_Kathode/1000)) + " \\pm " + str(round(Delta_F_Kathode/1000)) + ")~\\text{kC/mol}\\\\\n")
f.write("F_\\text{Anode} &= (" + str(round(F_Anode/1000)) + " \\pm " + str(round(Delta_F_Anode/1000)) + ")~\\text{kC/mol} \\\\\n")
f.write("e_\\text{Kathode} &= (" + str(custom_round(e_kathode*10**19,2)) + " \\pm " + str(custom_round(delta_e_kathode*10**19,2)) + ")\\cdot 10^{-19}~C \\\\\n")
f.write("e_\\text{Anode} &= (" + str(custom_round(e_anode*10**19,2)) + " \\pm " + str(custom_round(delta_e_anode*10**19,2)) + ")\\cdot 10^{-19}~C  \n")
f.write("\\end{align*}\n")

