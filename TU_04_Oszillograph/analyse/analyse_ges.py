import numpy as np
import matplotlib.pyplot as plt



def extract_data_from_file(filename):
    f = open(filename, "r")
    data = f.read()
    lines = data.split("\n")
    msecs = []
    channel = []
    for line in lines:
        parts = line.split(",")
        
        if line != "":
            msecs.append(float(parts[1]))
            channel.append(float(parts[2]))
    f.close()
    return [msecs, channel]


msecs1, channel1 = extract_data_from_file("data1.csv")
msecs2, channel2 = extract_data_from_file("data2.csv")


plt.plot(msecs1, channel1)
plt.plot(msecs2, channel2)
plt.savefig('plots.png')



def find_max(msecs, data, time_from, time_to):
    current_max = -100
    current_max_time = -100
    for i in range(len(msecs)):
        if msecs[i] >= time_from/1000.0 and msecs[i] <= time_to/1000.0 :
            if data[i] > current_max:
                current_max = data[i]
                current_max_time = msecs[i]
    return [current_max_time, current_max]


print(find_max(msecs1, channel1, -20, -15)) 
print(find_max(msecs1, channel1, 0, 5))  
print(find_max(msecs1, channel1, 20, 25))  
# [-0.0166, 3.6], [0.00324, 3.6],  [0.0228, 3.6]


print(find_max(msecs2, channel2, -15, -10))
print(find_max(msecs2, channel2, 5, 10)) 
print(find_max(msecs2, channel2, 25, 30))  
 # [-0.0124, 1.06], [0.00744, 1.06], [0.0268, 1.06]
