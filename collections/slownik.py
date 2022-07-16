# Slownik (dict)
# https://realpython.com/python-dicts/
# slownik jest mutowalny

dane = {
#   klucz: wartosc,
    'imie': 'Piotr',
    'nazwisko': 'GG',
    'ulubiona_liczba': 5,
    'imie': 'Tomek',  # druga wartosc zastepuje piersza
    10: 'Ala',
    2.5: 'Ola',
    True: 'Krysia',
    (1, 2): 'Tola',
}

print(dane['imie'])

dane['imie'] = 'Mateusz'
print(dane['imie'])
dane['drugie_imie'] = 'Krystian'
print(dane)
print(dane[10])
print(dane[2.5])
print(dane[True])
print(dane[(1,2)])

print('-'  * 30)

# iterowanie po kluczach
for klucz in dane:
    print(klucz, dane[klucz])

print('-'  * 30)

# iterowanie po kluczach z wartosciami
for klucz, wartosc in dane.items():
    print(klucz, wartosc)

print(dane.items())  # para klucz, wartosc
print(dane.keys())  # tylko klucze
print(dane.values())  # tylko wartosci

print('-' * 30)

autor, tytul = ('Mickiewicz', 'Pan Tadeusz')
print(autor)
print(tytul)

