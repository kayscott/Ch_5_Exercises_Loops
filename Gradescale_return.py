s = raw_input('enter grade:')
def computegrade(s):
    try:
        s = float(s)
        if s >= 0.9:
            return 'A'
        elif s >= 0.8:
            return 'B'
        elif s >= 0.7:
            return 'C'
        elif s >= 0.6:
            return 'D'
        elif s < 0.6:
            return 'F'
    except:
        return 'bad score'

print computegrade(s)