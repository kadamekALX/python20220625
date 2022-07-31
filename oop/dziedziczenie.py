class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Jestem", self.imie)


class Uczen(Osoba):  # klasa Uczen dziedziczy po klasie Osoba
    def __init__(self, imie):
        super().__init__(imie)  # `super()` pozwala na wołanie metod z nadklasy nawet jeśli są nadpisane w klasie dziedziczącej
        self.oceny = [3, 4, 5, 5]

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny) # if self.oceny else None


x = Uczen("Adam")
x.przedstaw_sie()
print(type(x))
print(x.srednia_ocen())
print(f"{isinstance(x, Osoba) = }")

class MojaLista(list):
    def append(self, x) -> None:
        print(f"UWAGA, dodaję obiekt {x}")
        super().append(x)


x = MojaLista()
x.append(5)
x.append(10)
x.append(15)
print(x)