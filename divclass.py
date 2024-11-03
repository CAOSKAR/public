from produkt1 import Produkt
from fruit import Fruit

class Fruit(Produkt):
    def mehrwertsteuer(self):
        return round(self.preis - self.preis/1.07, 2)

class Reifen(Produkt):
    def mehrwertsteuer(self):
        return round(self.preis - self.preis/1.19,2)
    
        #super().__init__(name, preis)
banane = Fruit("Banane", 1.99)
reifen = Reifen("Reifen", 249.99)

print(banane.mehrwertsteuer())
print(reifen.mehrwertsteuer())