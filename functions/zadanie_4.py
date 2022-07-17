"""
Napisz funkcję zliczającą liczbę znaków w podanym przez użytkownika napisie
pomiędzy zadanymi przez użytkownika znakami (np. <>).
Nawiasy mogą wystąpić tylko raz.

Przykład użycia:
> policz_znaki('ala ma <kota> a kot ma ale')
4
> policz_znaki('ala ma kota a (kot) ma ale', '(', ')')
3

Sygnatura funkcji:
policz_znaki(napis: str, start: str = '<', end: str = '>') -> int
"""


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

import pytest

def test_policz_znaki_w_pustym_napisie():
    with pytest.raises(ValueError):
        assert policz_znaki('') == 0


def test_policz_znaki_gdy_brak_nawiasow():
    with pytest.raises(ValueError):
        assert policz_znaki('Ala ma kota') == 0


def test_policz_znaki_pomiedzy_nawiasami_jeden_poziom():
    assert policz_znaki('Ala <ma> kota') == 2
    assert policz_znaki('Ala (ma) kota', '(', ')') == 2
