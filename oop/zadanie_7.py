# Zaimplementuj klasę PremiumEmployee, która będzie klasą
# pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
# przyznawanie bonusów pracownikowi.
# >>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.give_bonus(1000.0)
# >>> employee.pay_salary()
# 1500.0

class Pracownik:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.przepracowane_godziny = 0

    def rejestruj_czas(self, czas):
        self.przepracowane_godziny += czas
        if czas > 8:
            self.przepracowane_godziny += czas - 8

    def wyplata(self):
        wyplata = self.przepracowane_godziny * self.stawka
        self.przepracowane_godziny = 0
        return wyplata


class PracownikPremium(Pracownik):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def daj_bonus(self, kwota):
        self.bonus += kwota

    def wyplata(self):
        wynik = self.bonus + super().wyplata()
        self.bonus = 0
        return wynik


p = PracownikPremium("Jan", "Kowalski", 100)
p.rejestruj_czas(5)
p.daj_bonus(1000)
print(p.wyplata())