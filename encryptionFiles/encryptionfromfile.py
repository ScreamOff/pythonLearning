from encryption import encryption as en


fileToWrite = open("dec.txt", "w")
fileToRead = open("text.txt", 'r')
k = int(input("insert a key: "))
for l in fileToRead:
    print(l, end="")
    fileToWrite.write((en(l.strip(), k) + '\n'))
