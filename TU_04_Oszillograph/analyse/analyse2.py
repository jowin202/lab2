import numpy as np
import matplotlib.pyplot as plt

f = open("data2.csv", "r")

data = f.read()

lines = data.split("\n")

msecs = []
channel1 = []


for line in lines:
    parts = line.split(",")
    
    if line != "":
        msecs.append(float(parts[1]))
        channel1.append(float(parts[2]))
        #print(str(msecs[-1]) + " " + str(channel1[-1]))

f.close()



plt.plot(msecs, channel1)
plt.savefig('channel2.png')



def find_max(msecs, data, time_from, time_to):
    current_max = -100
    current_max_time = -100
    for i in range(len(msecs)):
        if msecs[i] >= time_from/1000.0 and msecs[i] <= time_to/1000.0 :
            if data[i] > current_max:
                current_max = data[i]
                current_max_time = msecs[i]
    return [current_max_time, current_max]


print(find_max(msecs, channel1, -15, -10))
print(find_max(msecs, channel1, 5, 10))
print(find_max(msecs, channel1, 25, 30))



