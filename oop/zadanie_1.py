# Zaimplementuj klasę Product przechowującą informację o cenie,
# nazwie oraz ID produktu. Zaimplementuj metodę wypisującą
# informację o produkcie na konsolę.
# Przykład użycia:
# >>> product = Product(1, 'Woda', 10.99)
# >>> product.print_info()
# Produkt "Woda", id: 1, cena: 10.99 PLN

class Produkt:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def wypisz_info(self):
        print(f"Produkt '{self.nazwa}', id: {self.id}, cena: {self.cena:.2f} PLN")

p = Produkt(1, "Woda", 2.50)
p2 = Produkt(2, "Banan", 3.99)
lista = [p, p2]
lista.append(Produkt(3, "Ziemniak", 0.98))
for x in lista:
    x.wypisz_info()
