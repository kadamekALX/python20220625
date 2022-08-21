# Wykorzystując API NBP (api.nbp.pl) pobierz ceny złota z 30 ostatnich dni.
# Wypisz największą, najmniejszą (wypisz daty) oraz średnią cenę.
from urllib.request import urlopen
import json

with urlopen("https://api.nbp.pl/api/cenyzlota/last/30?format=json") as p:
    lista = json.load(p)

najwieksza = None
najmniejsza = None
data_max = None
data_min = None

for d in lista:
    if najwieksza is None or d['cena'] > najwieksza:
        najwieksza = d['cena']
        data_max = d['data']
    if najmniejsza is None or d['cena'] < najmniejsza:
        najmniejsza = d['cena']
        data_min = d['data']

print(f"Najwieksza cena: {najwieksza}, dnia {data_max}")
print(f"Najmniejsza cena: {najmniejsza}, dnia {data_min}")
print(f"Średnia: {sum(d['cena'] for d in lista) / len(lista)}")