def spitze_tal(Volt):
    Vmin =  10000000000000000000
    Vmax = -10000000000000000000
    for V in Volt:
        if V < Vmin:
            Vmin = V
        if V > Vmax:
            Vmax = V
    return Vmax-Vmin
