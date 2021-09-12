import math

class Murtoluku:
    def __init__(self, os, nim):
        self.os = os
        self.nim = nim
        
    def tulosta(self):
            print(f'{self.os} / {self.nim}')
    
    def sievenna(self):
        syt = self.syt()
        self.os //= syt
        self.nim //= syt
        
    def syt(self):
        return math.gcd(self.os, self.nim)
    
ml =Murtoluku(2,4)
ml.tulosta()
ml.sievenna()
ml.tulosta()