# Wczytujemy liczbe naturalna N_1, a nastepnie przeksztalcamy ja w liczbe N_2 w taki sposob, ze N_2 jest suma cyfr liczby N_1.
# Na przyklad dla N_1 = 5839 mamy N_2 = 5 + 8 + 3 + 9 = 25.
# Tak otrzymana wartosc N_2 przeksztalcamy w N_3 wedlug tego samego algorytmu (suma cyfr poprzedniej liczby daje nam nowa liczbe), i tak dalej.
# Ile razy musze dokonac takiego przeksztalcenia, aby uzyskac liczbe jednocyfrowa?
# Np. dla liczby 5839 odpowiedz brzmi: 2, ale dla liczby 1232 odpowiedz brzmi: 1.

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


if __name__ == "__main__":
    liczba = int(input("Podaj liczbę:"))
    licznik = 0
    while liczba > 9:
        liczba = suma_cyfr(liczba)
        licznik += 1  # to samo co: licznik = licznik + 1

    print(licznik)


def test_suma_cyfr():
    assert suma_cyfr(5) == 5
    assert suma_cyfr(0) == 0
    assert suma_cyfr(567) == 18
