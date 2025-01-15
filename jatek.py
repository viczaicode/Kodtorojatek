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
        print("Új játék kezdődött! A lehetséges színek:", ", ".join(self.szinek_obj.szinek))
    
    def tipp_ellenorzese(self, tipp):
        self.probalkozasok_szama += 1
        
        fekete = 0  
        feher = 0  
        

        for i in range(4):
            if tipp[i] == self.titkos_kod[i]:
                fekete += 1
        

        for szin in tipp:
            if szin in self.titkos_kod:
                feher += 1
        

        feher = feher - fekete
        
        return fekete, feher
    
    def jatek_vege(self):
        return self.probalkozasok_szama >= self.max_probalkozas
