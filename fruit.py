from produkt1 import Produkt 
class Fruit(Produkt):
    def __init__(self, name, preis, haltbarkeitsdatum):
        self.haltbarkeitsdatum = haltbarkeitsdatum
    
        super().__init__(name, preis)

fruit= Fruit("Fruit", 1.99, "1.1.2050")
print(fruit)
print(fruit.haltbarkeitsdatum)