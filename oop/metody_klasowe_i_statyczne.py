from random import randint

class Bazowa:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"X = {self.x}"

    @classmethod
    def losowa(cls):
        k = randint(1, 20)
        return cls(k) # tworzymy obiekt klasy, na której została wywołana ta metoda

    @staticmethod
    def metoda_statyczna(arg):
        print(f"Metoda statyczna nie jest wywoływana na żadnym obiekcie klasy (nie ma self). {arg=}")

    @classmethod
    def metoda_klasowa(cls):
        print(f"Metoda klasowa dostaje jako pierwszy argument (cls) klasę, na której została wywołana {cls=}")

class Dziedziczaca(Bazowa):
    pass

Bazowa.metoda_statyczna(17)
b = Bazowa(5)
b.metoda_statyczna(20)
Bazowa.metoda_klasowa()
print(b)
losowy = Bazowa.losowa()
print(losowy)
d = Dziedziczaca.losowa()
print(d)
print(f"{type(d) = }")