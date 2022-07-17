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

if True is True:
    print('PRAWDA')
else:
    print('FALSZ')


print('-' * 30)


# argumenty domyslne
# najpierw podajemy argumenty obowiazkowe, pozniej te z wartoscia domyslna
def opakowywacz(napis: str, prefix: str = '>>', sufix: str = '<<') -> str:
    return prefix + napis + sufix

# wywolania pozycyjne
print(opakowywacz('Ala ma kota', '--'))
print(opakowywacz('Ala ma kota', '--', '..'))
print(opakowywacz('Ala ma kota', '>>', '..'))
print(opakowywacz('Ala ma kota', '..'))

# wywolania nazwane
print(opakowywacz(napis='Ala ma kota', prefix='--', sufix='..'))
print(opakowywacz(prefix='--', napis='Ala ma kota', sufix='..'))
print(opakowywacz(napis='Ala ma kota', sufix='..'))

# wywolania pozycyjnego i nazwanego
# najpierw podajemy argumenty w sposob pozycyjny, pozniej w sposob nazwany
print(opakowywacz('Ala ma kota', sufix='..'))

print(False == 0)


print('-' * 30)

# dowolnie wiele argumentów

# *args - argumenty pozycyjne
# **kwargs (key-worded arguments) - argumenty nazwane
def zliczacz(*args, **kwargs):
    print('---')
    print(f'{args = }')
    print(f'{kwargs = }')
    print('---')


zliczacz(1, 2, 3, a=10, b=20, c=30)
zliczacz()
zliczacz(1, 2, 3)
zliczacz(param1=123, param2=456)

# argumenty pozycyjny, *args, **kwargs - mozemy ze soba laczyc w dowolnej konfiguracji
# kolejnosc: pozycyjne, *args, **kwags

def moja_funkcja(a, b, c=10, *args, **kwargs):
    print('---')
    print(f'{a=}')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{args = }')
    print(f'{kwargs = }')
    print('---')

moja_funkcja(10, 20, 30, 40, 50, 60, param1=123, param2=456)

print('-' * 30)

# jednolinijkowy if

osoba = {
    'imie': 'Piotr',
    'nazwisko': 'GG',
    # 'pesel': 123,
}

if 'pesel' in osoba:
    czy_ma_pesel = True
else:
    czy_ma_pesel = False

print(czy_ma_pesel)


czy_ma_pesel = True if 'pesel' in osoba else False
print(czy_ma_pesel)