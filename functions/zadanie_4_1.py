def policz_znaki(napis: str, start: str = '<', end: str = '>') -> int:
    if napis.count(start) != 1 or napis.count(end) != 1:
        raise ValueError('Nieprawidlowa liczba nawiasow')

    liczba_znakow = 0
    czy_zliczac = False

    for znak in napis:
        if znak == start:
            czy_zliczac = True
        elif znak == end:
            czy_zliczac = False
        elif czy_zliczac == True:
            liczba_znakow += 1

    return liczba_znakow

try:
    print(policz_znaki('Ala <ma> kota'))
except ValueError:
    print('Wystapil blad! Podales nieprawidłowe dane!')


print('Na koncu programu')