from jatek import Jatek


jatek = Jatek()
jatek.uj_jatek()

while not jatek.jatek_vege():
    print(f"\n{jatek.probalkozasok_szama + 1}. próbálkozás:")
    
    while True:
        try:
            tipp = input("Add meg a 4 színt vesszővel elválasztva: ").lower().strip()
            tipp = [szin.strip() for szin in tipp.split(',')]
            
            if len(tipp) != 4:
                raise ValueError("Pontosan 4 színt adj meg!")
                
            if not all(jatek.szinek_obj.ervenyes_szin(szin) for szin in tipp):
                raise ValueError("Érvénytelen szín!")
                
            break
        except ValueError as e:
            print(f"Hiba: {e}")
    

    fekete, feher = jatek.tipp_ellenorzese(tipp)
    print(f"Eredmény: {fekete} fekete, {feher} fehér")
    

    if fekete == 4:
        print("\nGratulálok! Nyertél!")
        break

if jatek.jatek_vege() and fekete != 4:
    print("\nSajnos vesztettél!")
    print(f"A helyes megoldás: {', '.join(jatek.titkos_kod)}")