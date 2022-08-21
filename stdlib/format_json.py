import json

obiekt = [{"Ala": "kot", "Ola": "pies"}, 14, [1,2,3], True, False, None]
print(obiekt)
# napis = json.dumps(obiekt)
# print(napis)
# print(f"{type(napis) = }")
with open("dane.json", 'w') as plik:
    # plik.write(napis)
    json.dump(obiekt, plik, indent=2)

