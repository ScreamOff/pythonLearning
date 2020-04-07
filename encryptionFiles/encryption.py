def encryption(x, k):
    y = []
    ciprhed = ''
    for i in range(len(str(x))):
        if (ord(x[i]) + k) > 122:
            y.append(chr((ord(x[i]) + k - 26)))
        else:
            y.append(chr((ord(x[i]) + k)))
    for x in y:
        ciprhed += str(x)
    print(ciprhed)
    return ciprhed


def deciprh(x, k):
    l = []
    endword = ''

    for g in range(len(str(x))):
        if (ord(x[g]) - k) < 97:
            l.append(chr(ord(x[g]) - k + 26))
        else:
            l.append(chr(ord(x[g]) - k))
    for u in l:
        endword += str(u)
    print(endword)
    return (endword)
