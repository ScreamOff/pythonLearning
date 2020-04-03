import random
i=0
y = int()
x = random.randint(0,100)
while(x!=y):
    i+=1
    y = int(input())
    if y>x:
        print("podałeś większą ",i)
    elif y<x:
        print("mniejsza niż powinna ",i)
print("zgadłes podana liczba to ",x," zgadłeś w ",i)