from szinek import Szinek

class Jatek:
    def __init__(self):
        self.szinek_obj = Szinek()
        self.titkos_kod = []
        self.probalkozasok_szama = 0
        self.max_probalkozas = 9
    
    def uj_jatek(self):
        self.titkos_kod = self.szinek_obj.random_szinek()
        self.probalkozasok_szama = 0
        print("Új játék kezdődött!")
        print("A lehetséges színek:", end=" ")
        for szin in self.szinek_obj.szinek:
            print(szin, end=", ")
        print()
    
    def tipp_ellenorzese(self, tipp):
        self.probalkozasok_szama = self.probalkozasok_szama + 1
        
        fekete = 0
        feher = 0 
        

        for i in range(4):
            if tipp[i] == self.titkos_kod[i]:
                fekete = fekete + 1
        

        for szin in tipp:
            if szin in self.titkos_kod:
                feher = feher + 1
        

        feher = feher - fekete
        
        return fekete, feher
    
    def tipp_bekeres(self):
        print("\nAdd meg a 4 színt vesszővel elválasztva!")
        print("Például: piros,kék,zöld,sárga")
        
        while True: 
            szoveg = input("Tipp: ")
            

            tipp = []
            for szin in szoveg.split(','):
                tiszta_szin = szin.strip()
                tiszta_szin = tiszta_szin.lower()
                tipp.append(tiszta_szin)
            
            if len(tipp) != 4:
                print("Hiba: Pontosan 4 színt adj meg!")
                continue
            
            hibas_szin = False
            for szin in tipp:
                if not self.szinek_obj.szin_ellenorzes(szin):
                    print(f"Hiba: {szin} nem megfelelő szín!")
                    hibas_szin = True
                    break
            
            if hibas_szin:
                continue
                
            return tipp
    
    def jatek_vege(self):
        return self.probalkozasok_szama >= self.max_probalkozas
