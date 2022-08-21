import os
# Napisz funkcję (rekurencyjną), która wypisze zawartość zadanego katalogu.
# Zawartość podkatalogów powinna być wcięta o 1 tabulator więcej niż podkatalog.

def wypisz_katalog(katalog, wciecie=0):
    for x in os.scandir(katalog):
        w = '\t' * wciecie
        print(f"{w}{x.name}")
        if x.is_dir():
            wypisz_katalog(x, wciecie + 1)
        # print(x.name, x.is_dir(), x.path)

wypisz_katalog('C:\\')

# .idea
# basics
#     plik1
#     plik2
#     plik3
#     katalog
#         plik4
# collections
