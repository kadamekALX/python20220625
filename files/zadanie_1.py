nazwa_pliku = input("Podaj plik:")

try:
    with open(nazwa_pliku) as plik:
        for nr, wiersz in enumerate(plik, 1):
            print(f"{nr:3}: {wiersz}", end="")
except FileNotFoundError:
    print("Nie ma takiego pliku!")
