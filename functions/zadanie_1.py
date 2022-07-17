"""
Stwórz kalkulator oparty o funkcje:
1. Pobierz od użytkownika 2 liczby
2. Zapytaj o działanie: (+, -, *, /)
3. Na podstawie działania wykonujemy obliczenia i je pokazujemy
"""


def suma(a: float, b: float) -> float:
    return a + b


def roznica(a: float, b: float) -> float:
    return a - b


def iloczyn(a: float, b: float) -> float:
    return a * b


def iloraz(a: float, b: float) -> float:
    return a / b


liczba_1 = float(input('Podaj liczbę 1: '))
liczba_2 = float(input('Podaj liczbę 2: '))
dzialanie = input('Podaj działanie (+, -, *, /): ')

if dzialanie == '+':
    wynik = suma(liczba_1, liczba_2)
elif dzialanie == '-':
    wynik = roznica(liczba_1, liczba_2)
elif dzialanie == '*':
    wynik = iloczyn(liczba_1, liczba_2)
elif dzialanie == '/':
    wynik = iloraz(liczba_1, liczba_2)
else:
    print('Niepoprawne dzialanie.')
    exit()

print(f'{liczba_1}{dzialanie}{liczba_2}={wynik}')
