import json

with open("dane.json") as plik:
    obiekt = json.load(plik)

print(obiekt)
print(type(obiekt))