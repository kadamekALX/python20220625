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

import pytest


def policz_znaki(napis: str, start: str = '<', end: str = '>') -> int:
    pass

def test_policz_znaki_w_pustym_napisie():
    pass


def test_policz_znaki_gdy_brak_nawiasow():
    pass


def test_policz_znaki_pomiedzy_nawiasami_jeden_poziom():
    pass


def test_policz_znaki_pomiedzy_nawiasami_jeden_poziom_wiele_nawiasow():
    pass