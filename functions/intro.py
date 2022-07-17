# Funkcje

# definicja funkcji
def powiedz_czesc():
    print('Cześć!')

# uruchomienie funkcji
powiedz_czesc()

# jezeli funkcja potrzebuje danych do pracy
# powinnismy je przekazac jako argumenty
def powiedz_czesc_komus(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')


powiedz_czesc_komus('Piotr', 'GG')

moje_imie = 'Jan'
moje_nazwisko = 'Kowalski'
powiedz_czesc_komus(moje_imie, moje_nazwisko)

# moje_imie = input('Podaj imie: ')
# moje_nazwisko = input('Podaj nazwisko: ')
# powiedz_czesc_komus(moje_imie, moje_nazwisko)


def suma(a, b):
    return a + b
    # print('Ala ma kota')  # nic po returnie sie nie wykona


wynik = suma(2, 3)
print(wynik)


def czy_duza_liczba(liczba):
    if liczba > 1000:
        return 'duza'
    else:
        return 'mala'

wynik = czy_duza_liczba(1)
print(wynik)

wynik = czy_duza_liczba(2000)
print(wynik)


# Dokumentowanie funkcji
# type hinting
# opis dzialania funkcji
# https://realpython.com/documenting-python-code/
def suma(a: int, b: int) -> int:
    """Dodaje dwie liczby i zwaraca ich sumę.

    Tutaj mozemy opisać w szczegółach jak nasza funkcja działa.
    Co powinniśmy przekazywać, jak, czego się spodziewać.

    Ala ma kota.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik dodawania a i b
    """
    return a + b


print(suma(3, 4))

print('-' * 30)

# co jest falszem a co prawda

print(bool('Ala ma kota'))  # True
print(bool(''))  # False
print(bool('False'))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool([]))  # False
print(bool(['Ala ma kota']))  # True
print(bool([False]))  # True
print(bool(None))  # False

if 10:
    print('PRAWDA')
else:
    print('FALSZ')

if 1 == True:
    print('PRAWDA')
else:
    print('FALSZ')

if 1 is True:
    print('PRAWDA')
else:
    print('FALSZ')

if True is True:
    print('PRAWDA')
else:
    print('FALSZ')