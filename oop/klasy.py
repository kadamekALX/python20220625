class MojaKlasa:
    pass

# tworzymy obiekt typu `MojaKlasa`
obiekt = MojaKlasa()

print(obiekt)
print(type(obiekt))


class Samochod:
    # __init__ - konstruktor, czyli pierwsza metoda, która jest automatycznie wywoływana w momencie tworzenia obiektu
    def __init__(self, mar, kolor):
        self.marka = mar
        self.kolor = kolor

    def jedz(self):
        print(f"{self.kolor} {self.marka}: Brum-brum")


fiat = Samochod("Fiat", "zielony")  # tu jest wywoływany __init__
fiat.jedz()

ferrari = Samochod("Ferrari", "czerwone")
ferrari.jedz()

