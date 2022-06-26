najwieksza = None
najmniejsza = None
while True:
    napis = input("Podaj liczbę lub 'koniec':")
    if napis == "":
        continue
    if napis == "koniec":
        break
    liczba = int(napis)
    # if najwieksza is None:  # dostaliśmy wlasnie pierwszą wartość
    #     najwieksza = liczba
    if najwieksza is None or liczba > najwieksza:
        najwieksza = liczba
    if najmniejsza is None or liczba < najmniejsza:
        najmniejsza = liczba

if najwieksza is not None:
    print(f"Największa wprowadzona liczba to {najwieksza}")
    print(f"Najmniejsza wprowadzona liczba to {najmniejsza}")
else:
    print("Nie podałeś żadnej liczby")