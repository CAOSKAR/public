class Produkt:
    """ Basisklasse für Produkte.
    Überlädt Plus für die Addition von Produkten.
    """
    
    def __init__(self, name, preis):
        """ Initialisierung der Instanzvariablen name und preis.
        """
        self.name = name
        self.preis = preis    
    
    def __add__(self, instanz):
        return round(self.preis + instanz.preis,2)
    
banane = Produkt("Banane", 1.99)
""" reifen = Produkt("Reifen", 249.99)
apfel = Produkt("Apfel", 1.49)
benzin = Produkt("Benzin pro Liter", 1.70) 

print(banane + reifen)"""