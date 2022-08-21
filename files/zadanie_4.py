import os
# Napisz funkcję (rekurencyjną), która wypisze zawartość zadanego katalogu.
# Zawartość podkatalogów powinna być wcięta o 1 tabulator więcej niż podkatalog.

def wypisz_katalog(katalog, wciecie=[]):
    lista = list(os.scandir(katalog))
    for x in lista:
        w = "".join(wciecie)
        if x is lista[-1]:
            w += "\\---"
        else:
            w += "|---"
        print(f"{w}{x.name}")
        if x.is_dir():
            if x is lista[-1]:
                wypisz_katalog(x, wciecie + [" " * 4])
            else:
                wypisz_katalog(x, wciecie + ["|   "])

wypisz_katalog('..')

