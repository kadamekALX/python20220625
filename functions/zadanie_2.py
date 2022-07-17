"""
Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
Przykład użycia:
> czy_jest_pierwsza(10)
False
> czy_jest_pierwsza(17)
True

Liczba pierwsza
- bedzie intem
- wieksza od 1
- dzieli sie tylko przez 1 i przez sama siebie
"""


def czy_jest_pierwsza(liczba: int) -> bool:
    """Funkcja sprawdza czy liczba jest pierwsza.

    https://pl.wikipedia.org/wiki/Liczba_pierwsza

    :param liczba:
    :return:
    """
    if liczba <= 1:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True


def test_czy_liczba_jest_pierwsza():
    # GWT - https://martinfowler.com/bliki/GivenWhenThen.html
    # Given
    liczba = 5

    # When
    wynik = czy_jest_pierwsza(liczba)

    # Then
    # asercja (ang. assert) - uznanie jakiegos zdania/wyrazenia za prawdziwe
    # https://pl.wikipedia.org/wiki/Asercja_(informatyka)
    # https://sjp.pl/asercja
    assert wynik is True


def test_wielu_liczb_pierwszych():
    liczby = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for liczba in liczby:
        assert czy_jest_pierwsza(liczba) is True


def test_wielu_liczb_nie_pierwszych():
    liczby = [-100, -10, 0, 1, 4, 8, 9, 30, 50, 100]
    for liczba in liczby:
        assert czy_jest_pierwsza(liczba) is False

def test_wielu_liczb_pierwszych2():
    liczby = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for liczba in liczby:
        assert czy_jest_pierwsza(liczba)


def test_wielu_liczb_nie_pierwszych2():
    liczby = [-100, -10, 0, 1, 4, 8, 9, 30, 50, 100]
    for liczba in liczby:
        assert not czy_jest_pierwsza(liczba)
