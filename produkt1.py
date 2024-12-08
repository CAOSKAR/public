class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis    

    def __str__(self):
        return "Produkt: " + self.name + " kostet" + str(self.preis)
    
""" banane = Produkt("Banane", 1.99)
reifen = Produkt("Reifen", 249.99)
apfel = Produkt("Apfel", 1.49)
benzin = Produkt("Benzin pro Liter", 1.70)

items = (banane,reifen,apfel,benzin)

for item in items:
    print(item) """
