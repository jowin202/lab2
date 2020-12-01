def phasenverschiebung(t, V1, V2, offset):
    t0_V1 = 0
    t0_V2 = 0
    for i in range(offset, len(V1)-1):
        if V1[i] == 0:
            t0_V1 = t[i]
            break
        if V1[i] < 0 and V1[i+1] > 0:
            t0_V1 = (t[i] + t[i+1])/2
            break
    for i in range(len(V2)-1):
        if V2[i] == 0:
            t0_V2 = t[i]
            break
        if V2[i] < 0 and V2[i+1] > 0:
            t0_V2 = (t[i] + t[i+1])/2
            break
    
    return t0_V1-t0_V2
