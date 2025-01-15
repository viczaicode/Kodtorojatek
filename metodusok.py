import random

def gep_tippel():
    szamok_lista = []
    for i in range(4):
        randomszam = random.randint(1,6)
        szamok_lista.append(randomszam)
    print(szamok_lista)
    return szamok_lista

def bekeres():
    print("1-Piros; 2-Kék; 3-Citromsárga; 4-Zöld; 5-Narancssárga; 6-Lila")
    valasz = int(input("Kérlek adj meg egy számot: "))
    while not(valasz > 0 and valasz < 7):
        valasz = int(input("Kérlek adj meg egy számot: "))
    return valasz
    