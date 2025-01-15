from jatek import Jatek


jatek = Jatek()
jatek.uj_jatek()

nyert = False

while not jatek.jatek_vege():
    print(f"\n{jatek.probalkozasok_szama + 1}. próbálkozás:")
    tipp = jatek.tipp_bekeres()
    fekete, feher = jatek.tipp_ellenorzese(tipp)
    print(f"Eredmény: {fekete} fekete, {feher} fehér")
    if fekete == 4:
        print("\nGratulálok! Nyertél!")
        nyert = True
        break

if not nyert:
    print("\nSajnos vesztettél!")
    print("A helyes megoldás:", end=" ")
    for szin in jatek.titkos_kod:
        print(szin, end=", ")
    print()
