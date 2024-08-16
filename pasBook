import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters+digits+special_chars
password_lenght = 16

def passwordgeneration():
    password=''
    for i in range(password_lenght):
        password+=''.join(secrets.choice(alphabet))
    print(password)
    return password





def szyfruj(txt):
    zaszyfrowny = ""
    KLUCZ = input('Podaj klucz: ')
    for i in range(len(txt)):
        zaszyfrowny += chr(ord(txt[i]) + int(KLUCZ))
    return zaszyfrowny

def deszyfruj(tekst):
    odszyfrowany = ""
    KLUCZ = input('podaj klucz')
    for znak in tekst:
        odszyfrowany += chr(ord(znak) - int(KLUCZ))
    return odszyfrowany

def savingfile(passwordciphered):
    f = open('passwords.txt','a')
    nameofwebsite = input("Podaj domene do hasla: ")
    f.write(nameofwebsite + "\n")
    login = input('Podaj nazwe uzytkownika: ')
    f.write(login + '\n')
    f.write(passwordciphered + '\n')
    f.close()

def readingfile():
    i = 0
    f = open('passwords.txt','r')
    for line in f:
        i=i+1
        if i%3==0:
            print(deszyfruj(line) , end = " ")
        else:
            print(line , end = " ")
    f.close()

def menu():
    while True:
        print("Wybierz opcje:")
        print('1.Zapis nowego hasla')
        print('2.Odczytanie bazy hasel')
        opcja = int(input("Wybor : "))
        if opcja == 1:
            savingfile(szyfruj(passwordgeneration()))
            break
        if opcja == 2:
            readingfile()
            break
menu()
