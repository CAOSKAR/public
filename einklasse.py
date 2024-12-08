class EinfachKlasse:
    def __init__(self, param):
        self.instanzvar = param

instanz =EinfachKlasse("neuer Wert")
print(instanz.instanzvar)       