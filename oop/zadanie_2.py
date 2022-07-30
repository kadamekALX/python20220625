# Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki
# godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
# jako nadgodziny (z podwójną stawką godzinową).
# Przykład użycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0
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

p = Pracownik("Jan", "Nowak", 100)
p.rejestruj_czas(5)
print(p.wyplata())
p.rejestruj_czas(5)
p.rejestruj_czas(5)
print(p.wyplata())
print(p.wyplata())
p.rejestruj_czas(10)
print(p.wyplata())

