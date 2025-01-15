import random

class Szinek:
    def __init__(self):
        self.szinek = ['piros', 'kék', 'zöld', 'sárga', 'narancs', 'lila']
    
    def random_szinek(self):
        titkos = []
        lehetseges_szinek = self.szinek.copy() 
        
        for _ in range(4):
            szin = random.choice(lehetseges_szinek)
            titkos.append(szin)
            lehetseges_szinek.remove(szin)
            
        return titkos
    
    def szin_ellenorzes(self, szin):
        if szin in self.szinek:
            return True
        else:
            return False
