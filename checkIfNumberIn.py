import random

x = []
for i in range(10):
    x.append(random.randint(0, 10))


def checkifnumberin(tablica):
    powtorzone = []
    for i in range(len(tablica)):
        k = i + 1
        for j in range(k, len(tablica)):
            if tablica[i] == tablica[j]:
                powtorzone.append(tablica[i])
    print(sorted(tablica))
    print(list(set(powtorzone)))
    return list(set(powtorzone))


checkifnumberin(x)
