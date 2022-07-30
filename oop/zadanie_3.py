# Zaimplementuj klasę ElectricCar odwzorowującą zachowanie
# samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
# zadanego dystansu, który nie może przekroczyć maksymalnego
# zasięgu zdefiniowanego dla samochodu. Samochód powinien
# mieć także możliwość naładowania baterii.
# >>> car = ElectricCar(100)
# >>> car.drive(70)
# 70
# >>> car.drive(50)
# 30
# >>> car.drive(50)
# 0
# >>> car.charge()
# >>> car.drive(50)
# 50

class Samochod:
    def __init__(self, zasieg):
        self.zasieg = zasieg
        self.max_zasieg = zasieg

    def jedz(self, dystans):
        # wynik = min(self.zasieg, dystans)
        # self.zasieg -= wynik
        # return wynik
        wynik = dystans
        if self.zasieg >= dystans:
            self.zasieg -= dystans
        else:
            wynik = self.zasieg
            self.zasieg = 0
        return wynik

    def tankuj(self):
        self.zasieg = self.max_zasieg

s = Samochod(120)
print(f"{s.jedz(70) = }")
print(f"{s.jedz(70) = }")
print(f"{s.jedz(20) = }")
s.tankuj()
print(f"{s.jedz(20) = }")

