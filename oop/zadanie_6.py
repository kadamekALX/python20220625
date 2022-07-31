# Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
# swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
# mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),
# porównywania (po długości) oraz powinny posiadać czytelną
# reprezentację napisową.
# Przykład użycia:
# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# vector_3 = vector_1 + vector_2
class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"[{self.x}, {self.y}]"


v = Wektor(1, 2)
w = Wektor(3, 4)

# z = v.__add__(w)  # `v` będzie `self`, a `w` będzie `other`
z = v + w  # `v + w` wywoła v.__add__(w)
print(v)
print(w)
print(z)
print(f"{v} + {w} = {v + w}")
# Chcemy, żeby poniższe 2 wiersze działały
# q = v * 5
# if v < w: