def encryption(x, k):
    y = []
    ciprhed = ''
    for i in range(len(str(x))):
        y.append(chr((ord(x[i]) + k)))
    for x in y:
        ciprhed += str(x)
    print(ciprhed)
    return ciprhed


def deciprh(x, k):
    l = []
    endWord = ''

    for g in range(len(str(x))):
        l.append(chr(ord(x[g]) - k))
    for u in l:
        endWord += str(u)
    print(endWord)
    return(endWord)

encryption("power", 5)
y = encryption("power", 5)
deciprh(y, 5)
