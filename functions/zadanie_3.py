"""
Napisz funkcję zwracającą zbiór wszystkich znaków
występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
> wiecej_niz('ala ma kota a kot ma ale', 3) {'a', ' '}

1. Definiujemy funkcje
2. Policzyc ile jest znakow (.count()) i dodac je do zbioru,
ktory na koncu zwracamy

Przypadki testowe?
pusty napis
2 dowolne napisy
"""

def wiecej_niz(napis: str, ile_znakow: int) -> set:
    wynik = set()

    for znak in napis:
        if napis.count(znak) > ile_znakow:
            wynik.add(znak)

    return wynik


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 1) == set()


def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaaabbc', 3) == {'a'}
    assert wiecej_niz('AAAabc', 2) == {'A'}
    assert wiecej_niz('AAAbbbcc', 2) == {'A', 'b'}


