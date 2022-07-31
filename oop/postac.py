class Postac:
    def __init__(self, imie, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie

    # Postac traci `ile` punktow zdrowia. Zdrowie nie powinno spaść poniżej 0.
    def otrzymaj_obrazenia(self, ile):
        self.zdrowie -= ile
        if self.zdrowie < 0:
            self.zdrowie = 0

    # np. "Rufus, 57/100 HP"
    def wypisz_info(self):
        print(f"{self.imie}, zdrowie: {self.zdrowie}/{self.max_zdrowie}")

    def czy_zyje(self):
        return self.zdrowie > 0

    # przywraca `ile` punktów zdrowia. Zdrowie nie powinno przekroczyć maksymalnej wartości.
    def wylecz(self, ile):
        if self.czy_zyje():
            self.zdrowie += ile
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie


p = Postac("Rufus", 120)
p.wypisz_info()  # Rufus, 120/120 HP
p.otrzymaj_obrazenia(50)
p.wypisz_info()  # Rufus, 70/120 HP
p.wylecz(5)
p.wypisz_info()  # Rufus, 75/120 HP
p.otrzymaj_obrazenia(500)
p.wypisz_info()  # Rufus, nie żyje

