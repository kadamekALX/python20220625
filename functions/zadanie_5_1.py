"""
Napiszmy funkcję do liczenia sredniej, ktora
wykorzysta mechanizm *args

np. srednia(10, 20, 30) -> 20

Testy
jezeli nie ma argumetow srednia() to wynikiem bedzie None
"""

def srednia(*args):
    # if len(args) == 0:
    #     return None

    # if not args:
    #     return None
    #
    # return sum(args) / len(args)

    return sum(args) / len(args) if args else None


def test_srednia_bez_argumentow():
    assert srednia() is None


def test_srednia():
    assert srednia(10, 20, 30) == 20

