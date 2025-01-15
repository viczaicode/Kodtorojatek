# Mastermind Játék

Egyszerű konzolos kódtörő játék implementáció Python nyelven.

## A Játék Leírása

A kódtörő egy logikai játék, ahol a játékosnak ki kell találnia egy 4 színből álló titkos kódot. A játékos minden próbálkozás után visszajelzést kap:
- Fekete bábu: helyes szín a helyes pozícióban
- Fehér bábu: helyes szín, de rossz pozícióban


## Telepítés

Klónozd le a projektet:
```bash
git clone [repository URL]
```


## Használat

A játék indításához futtasd a `main.py` fájlt:
```bash
python main.py
```

### Játékmenet

1. A program véletlenszerűen kiválaszt 4 különböző színt
2. A játékosnak 9 próbálkozása van kitalálni a helyes színkombinációt
3. Minden tippnél vesszővel elválasztva kell megadni 4 színt
4. A program minden tipp után visszajelzést ad:
   - Fekete bábuk száma: helyes szín, helyes pozíció
   - Fehér bábuk száma: helyes szín, rossz pozíció

### Elérhető Színek
- piros
- kék
- zöld
- sárga
- narancs
- lila

### Példa Bemenet
```
Add meg a 4 színt vesszővel elválasztva: piros,kék,zöld,sárga
```

## Fejlesztői Információk


#### Szinek (szinek.py)
- Színek listájának kezelése
- Véletlenszerű színkombináció generálása
- Szín érvényességének ellenőrzése

#### Jatek (jatek.py)
- Játékmenet kezelése
- Tippek ellenőrzése
- Játékállapot követése

## Követelmények

- Python 3.x
- Nem igényel külső függőségeket
