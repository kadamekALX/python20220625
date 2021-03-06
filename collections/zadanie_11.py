"""
Stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
- (a) listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

- (b) zbiór tupli zawierających 3 elementy - daną liczbę,
jej kwadrat i jej sześcian - w przedziale od -10 do 10
{(-8, 64, -512), (-1, 1, -1), (9, 81, 729), (4, 16, 64), (5, 25, 125), (2, 4, 8), (-9, 81, -729), (3, 9, 27), (-6, 36, -216), (7, 49, 343), (-4, 16, -64), (0, 0, 0), (-7, 49, -343), (10, 100, 1000), (-5, 25, -125), (-2, 4, -8), (8, 64, 512), (-10, 100, -1000), (-3, 9, -27), (6, 36, 216), (1, 1, 1)}

- (c) słownik mapujący napisy na ich długość powstały ze zbioru napisów
{
    'a': 1,
    'Tom': 3,
    'Amy': 3,
    'To be or not to be': 18
}
"""
a = [liczba/10 for liczba in range(0, 11)]
print(a)

b = {(liczba, liczba ** 2, liczba ** 3) for liczba in range(-10, 11)}
print(b)

napisy = {'a', 'Tom', 'Amy', 'To be or not to be'}
c = {napis: len(napis) for napis in napisy}
print(c)