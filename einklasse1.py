class EinfachKlasse:
    def __init__(self, *args):
        for arg in args:
            print(arg)

instanz = EinfachKlasse("Hallo", "Wert")
