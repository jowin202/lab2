

def read_from_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    
    lines = data.split("\n")
    
    maximum_i = 0
    maximum_x = 0
    maximum = -10000
    
    for i in range(1,len(lines)):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y > maximum:
            maximum = y
            maximum_i = i
            maximum_x = x
            
            
            
    minimum_1 = 100000
    minimum_2 = 100000
    for i in range(maximum_i-150,maximum_i):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y < minimum_1:
            minimum_1 = y
            
            
            
    for i in range(maximum_i,maximum_i+150):
        line = lines[i]
        
        parts = line.split(",")
        if parts[0] != '' and parts[1] != '':
            x = float(parts[0])
            y = float(parts[1])
            
        if y < minimum_2:
            minimum_2 = y
            
            
            
    return maximum_x,maximum, minimum_1,minimum_2
    
    

    
    
print(read_from_file("moodle/img2.csv"))
print(read_from_file("moodle/img3.csv"))
print(read_from_file("moodle/img4.csv"))
