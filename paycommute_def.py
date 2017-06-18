h1 = raw_input('Enter hours:')
r1 = raw_input('Enter rate:')
def computepay(h1,r1): 
    h1 = float(h1)
    r1 = float(r1)
    if h1 <= 40 : 
        return h1 * r1 
    else :
        if h1 > 40 : 
            return (40 * r1) + ((h1 - 40) * (r1 * 1.5))

print computepay(h1, r1)