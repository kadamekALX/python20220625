"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi
w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu zbiorów.


1 czesc - ile unikalnych liczb uzytkownik wprowadzil
w petli (while) wczytujemy dane do zbioru, koniec przerywa petle
po petli pokazujemy ile unikalnych liczb zostalo wczytanych i jakie to byly

2 czesc - ile wprowadzonych liczb bylo parzystych w zakresie od 0 do 100
trzeba sobie zrobic zbior liczb parzystych - mozna uzyc petli for i funkcji range(0, 101, 2)
robimy iloczyn teoriomnogosciowy na dwoch zbiorach, zeby pokazac ktore wprowadzone, byly parzyste

Przykład:
Podaj liczbę: 1
Podaj liczbę: 2
Podaj liczbę: 3
Podaj liczbę: 4
Podaj liczbę: 5
Podaj liczbę: koniec
Liczba unikalnych liczb: 5
Liczba liczb parzystych od 0 do 100: 2
"""

# while True:
#     dane = input('')
#     if dane == 'koniec':
#         break
#     else:
#         pass


# for liczba in range(0, 101, 5):
#     print(liczba)

# liczby_parzyste = set()
#
# for liczba in range(0, 101, 2):
#     liczby_parzyste.add(liczba)

liczby_parzyste = set(range(0, 101, 2))

liczby_uzytkownika = set()

while True:
    dane = input('Podaj liczbe: ')
    if dane == 'koniec':
        break
    liczby_uzytkownika.add(int(dane))

print(f'Liczba unikalnych liczb: {len(liczby_uzytkownika)}')
print(f'Liczba liczb parzystych z zakresu 0-100: {len(liczby_parzyste.intersection(liczby_uzytkownika))}')
print(f'Liczba liczb parzystych z zakresu 0-100: {len(liczby_parzyste & liczby_uzytkownika)}')
