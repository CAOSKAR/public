class Produkt:
    name = None

    def __str__(self):
        return "Produkt: " + self.name
kaese = Produkt()
kaese.name = "Käse"
print(kaese)