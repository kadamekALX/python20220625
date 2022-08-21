# Napisz program obsługujący bazę danych pracowników. W bazie
# danych przechowuj imię, nazwisko, rok urodzenia, pensję.
# Skorzystaj z modułu json.
# Przykład użycia:
# $ python employees.py
# Co chcesz zrobić? [d - dodaj, w - wypisz] d
# Imie: Jan
# Nazwisko: Nowak
# Rok urodzenia: 1980
# Pensja: 5000.0
# $ python employees.py
# Co chcesz zrobić? [d - dodaj, w - wypisz] w
# Pracownicy:
# - [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN

import json

try:
    with open("pracownicy.json") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

op = input("Co chcesz zrobić? [d-dodaj, w-wypisz]:")
if op == 'd':
    p = {}
    p["imie"] = input("Imię:")
    p["nazwisko"] = input("Nazwisko:")
    p["rok_ur"] = int(input("Rok urodzenia:"))
    p["pensja"] = float(input("Pensja:"))
    pracownicy.append(p)
    with open("pracownicy.json", 'w') as plik:
        json.dump(pracownicy, plik, indent=2)
elif op == 'w':
    for nr, p in enumerate(pracownicy, 1):
        print(f"[{nr}] - {p['imie']} {p['nazwisko']}")
