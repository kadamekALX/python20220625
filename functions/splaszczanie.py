# isinstance(3, int)
# True
# isinstance(3, float)
# False
# isinstance(3, (int, float))
# True
# isinstance(3, (float, int))
# True
# isinstance(3, (float, list))
# False

# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:
# >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
# [1, 2, 3, 4, 5, 6, 7]

def splaszcz(lista):
    wynik = []
    for x in lista:
        if isinstance(x, list):
            # for i in splaszcz(x):
            #     wynik.append(i)
            wynik.extend(splaszcz(x))  # dokładnie to samo co w komentarzu powyżej
        else:  # x jest liczbą
            wynik.append(x)
    return wynik

if __name__ == "__main__":
    input("wcisnij enter")

def test_brak_zagniezdzen():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_pojedyncze_zagniezdzenia():
    assert splaszcz([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_zadanie():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]



