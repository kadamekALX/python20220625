# Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w
# określonej liczbie do koszyka. Zaimplementuj metodę obliczającą
# całkowitą wartość koszyka oraz wypisującą informację o zawartości
# koszyka. Dodanie dwa razy tego samego produktu do koszyka
# powinno stworzyć tylko jedną pozycję.
# Przykład użycia:
# >>> basket = Basket()
# >>> product = Product(1, 'Woda', 10.00)
# >>> basket.add_product(product, 5)
# >>> basket.count_total_price()
# 50.0
# >>> basket.generate_report()
# 'Produkty w koszyku:\n
# - Woda (1), cena: 10.00 x 5\n
# W sumie: 50.00'
#
# Na początek robimy wersję, gdzie wkładamy do koszyka tylko pojedyncze produkty i włożenie 2 takich samych może generować 2 osobne pozycje

class Produkt:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def wypisz_info(self):
        print(f"Produkt '{self.nazwa}', id: {self.id}, cena: {self.cena:.2f} PLN")


class WpisKoszyka:
    def __init__(self, p, ile):
        self.produkt = p
        self.ilosc = ile

    def wartosc(self):
        return self.produkt.cena * self.ilosc

    # metoda __str__() jest wywoływana przy konwertowaniu na napis
    def __str__(self):
        return f"{self.produkt.nazwa}, {self.produkt.cena} PLN x{self.ilosc}"

class Koszyk:
    def __init__(self):
        self.zawartosc = []  # lista obiektów WpisKoszyka

    def dodaj_produkt(self, prod: Produkt, ile=1):
        if not isinstance(prod, Produkt):
            return  # nie wkładamy do koszyka rzeczy typów innych niż Produkt
        self.zawartosc.append(WpisKoszyka(prod, ile))

    def laczna_cena(self):
        suma = 0
        for wk in self.zawartosc:
            suma += wk.wartosc()
        return suma

    def podsumowanie(self):
        print("Produkty w koszyku:")
        for wk in self.zawartosc:
            print(f" - {wk}")  # w tym miejscu jest wywoływane wk.__str__()
        print(f"Suma: {self.laczna_cena()} PLN")


k = Koszyk()
p = Produkt(1, "Woda", 5.50)
k.dodaj_produkt(p, 4)
k.dodaj_produkt(Produkt(2, "Banan", 2.99))
k.podsumowanie()