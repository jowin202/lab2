from math import sin
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
print(phi_average)


#gitterkonstante
g1 = 2 * na_lampe_lambda_1/sin(phi_average/360 * 2 * pi)
g2 = 2 * na_lampe_lambda_2/sin(phi_average/360 * 2 * pi)

g = (g1+g2)/2

print("Gitterkonstante: " + str(g))







#Hg-Lampe

farben = ['Violett', 'Blau', 'Türkis', 'Grün', 'Gelb']
R = [104.1, 101.8, 97.6, 93.4, 90.9]
L = [159.2, 161.7, 166.0, 170.8, 173.5, 173.8]

halber_winkel = [0] * 5
wellenlaenge_pro_farbe = [0] * 5
wellenlaenge_pro_farbe_in_nm = [0] * 5
for i in range(5):
    halber_winkel[i] = (L[i]-R[i])/2
    wellenlaenge_pro_farbe[i] = g * sin(halber_winkel[i] / 360 * 2 * pi)/2
    wellenlaenge_pro_farbe_in_nm[i] = wellenlaenge_pro_farbe[i] * 10**9
    
print(wellenlaenge_pro_farbe_in_nm)





#Auflösevermögen

b = 2 * 10**-2 # 2 cm Breite

print("Auflösung: " + str(b/g))

