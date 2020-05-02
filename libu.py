import os
from librus import LibrusSession

# whitelista
whitelist = []
whitelisttoformat = ["",]
for i in whitelisttoformat:
    whitelist.append(f"{i} ({i})")
# logowanie
librus = LibrusSession()
librus.login(os.environ.get("LIBRUS_USER"), os.environ.get("LIBRUS_PASSWORD"))
# oceny
oceny = open("oceny.txt", "w+")
for grades in librus.list_grades():
    oceny.write(f"{grades.grade}    {grades.title}      {grades.teacher}\n")
# wiadomosci i katalogowanie
for message in librus.list_messages(get_content=True):
    if message.sender in whitelist:
        continue
    if os.path.exists(f"{message.sender}"):
        plik = open(f"{message.sender}\{message.subject}.txt", "w+")
        plik.write(f"{message.content}")
        plik.close()
    else:
        os.mkdir(f"{message.sender}")
        plik1 = open(f"{message.sender}\{message.subject}.txt", "w+")
        plik1.write(f"{message.content}")
        plik1.close()
