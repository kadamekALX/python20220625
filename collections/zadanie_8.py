"""
Napisz program wyliczający kwotę należną za zakupiony towar
na podstawie podanej przez użytkownika wagi i nazwy produktu.
Do przechowywania informacji o cenie za kilogram
danego produktu użyj słownika.
Wypisz wszystkie dostępne produkty w sklepie.


1. Robimy słownik z produktami, dodajmy:
      ziemniaki 1.2
      pomidory 4.5
      marchew 0.5
2. Wyświetlam słownik
3. Pytam użytkownika o produkt i sprawadzam czy jest w produktach
4. Wczytujemy ile kg uzytkownik chce kupic
5. Liczymy należność
"""

produkty = {
    'ziemniaki': 1.2,
    'pomidory': 4.5,
    'marchew': 0.5,
}

print('Lista produktow')
for produkt, cena in produkty.items():
    print(f'{produkt} - {cena:.2f} zł / kg')

co = input('Co chcesz kupić? ')

if co not in produkty:
    print('Nie mamy takiego produktu w sklepie!')
    exit()  # powoduje zamkniecie programu

liczba_kg = float(input(f'Ile kg produktu {co} chcesz kupic? '))
naleznosc = produkty[co] * liczba_kg

print(f'Za {liczba_kg} kg produktu {co} zapłacisz {naleznosc:.2f} zł.')
