import random

class Szinek:
    def __init__(self):
        self.szinek = ['piros', 'kék', 'zöld', 'sárga', 'narancs', 'lila']
    
    def random_szinek(self):
        return random.sample(self.szinek, 4)
    
    def ervenyes_szin(self, szin):
        return szin in self.szinek