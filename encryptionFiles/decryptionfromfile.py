from encryption import deciprh as dc

y = open("dec.txt", "r")
f = open("text.txt", 'w')
r = int(input("insert a key: "))
for l in y:
    f.write(dc(l, r) + "\n")
