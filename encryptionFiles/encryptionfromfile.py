from encryption import encryption as en

y = open("dec.txt", "w")
f = open("text.txt", 'r')
k = int(input("insert a key: "))
for l in f:
    print(l, end="")
    y.write((en(l, k) + "\n"))
