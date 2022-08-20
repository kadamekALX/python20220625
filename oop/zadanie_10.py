# Zaimplementuj mechanizm automatycznego generowania kolejnych
# ID dla produktów. Informację o kolejnym ID przechowuj jako pole
# klasowe.
# Przykład użycia:
# >>> product_1 = Product('Woda', 1.99)
# >>> product_1.id
# 1
# >>> product_2 = Product('Chleb', 2.50)
# >>> product_2.id
# 2

class Produkt:
    NASTEPNE_ID = 1

    def __init__(self, nazwa, cena):
        self.id = Produkt.NASTEPNE_ID
        Produkt.NASTEPNE_ID += 1
        self.nazwa = nazwa
        self.cena = cena

    def wypisz_info(self):
        print(f"Produkt '{self.nazwa}', id: {self.id}, cena: {self.cena:.2f} PLN")

p = Produkt("Woda", 1.99)
p2 = Produkt("Banan", 1.99)
p3 = Produkt("Czekolada", 1.99)
p.wypisz_info()
p2.wypisz_info()
p3.wypisz_info()