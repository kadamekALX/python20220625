class Postac:
    def __init__(self, imie, zdrowie):
        pass

    # Postac traci `ile` punktow zdrowia. Zdrowie nie powinno spaść poniżej 0.
    def otrzymaj_obrazenia(self, ile):
        pass

    # np. "Rufus, 57/100 HP"
    def wypisz_info(self):
        pass

    def czy_zyje(self):
        pass

    # przywraca `ile` punktów zdrowia. Zdrowie nie powinno przekroczyć maksymalnej wartości.
    def wylecz(self, ile):
        pass


p = Postac("Rufus", 120)
p.wypisz_info()  # Rufus, 120/120 HP
p.otrzymaj_obrazenia(50)
p.wypisz_info()  # Rufus, 70/120 HP
p.wylecz(5)
p.wypisz_info()  # Rufus, 75/120 HP
p.otrzymaj_obrazenia(500)
p.wypisz_info()  # Rufus, nie żyje

