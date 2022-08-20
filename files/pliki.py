# plik = open("plik.txt")
# print(plik)
# napis = plik.read()
# print(napis)
# print(type(napis))
# # plik.seek(0)
# # x = plik.read()
# # print(f"{x = }")
# plik.close()  # każdy otwarty plik musimy zamknąć

# przy wychodzeniu z bloku `with` otwarty plik zostanie automatycznie zamknięty
# otwarcie nieistniejącego pliku do odczytu powoduje błąd
with open("plik.txt") as p:
    # napis = p.read()
    # napis = p.readlines()
    for linia in p:
        print(linia, end="")

# print(napis)

# zapis do pliku - 'w' usuwa całą poprzednią zawartość, 'a' - dopisuje na koniec\
# otwarcie nieistniejącego pliku do zapisu tworzy ten plik
with open("zapis.txt", 'w') as plik:
    plik.write("Ala ma kota\nKot ma czkawkę.\n")
