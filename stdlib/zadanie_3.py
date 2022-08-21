# Wyświetl możliwe kategorie dowcipów o Chucku Norrisie i każ użytkownikowi wybrać jedną z nich.
# Po wybraniu kategorii wyświetl losowy dowcip z wybranej kategorii.
# https://api.chucknorris.io

from urllib.request import urlopen, Request
import json

zapytanie = Request("https://api.chucknorris.io/jokes/categories", headers={"User-Agent": "hax0r"})
with urlopen(zapytanie) as p:
    kategorie = json.load(p)

print(*kategorie)  # print("animal", "career", ...)
wybor = None
while wybor not in kategorie:
    wybor = input("Wybierz kategorię:").lower()

zapytanie = Request(f"https://api.chucknorris.io/jokes/random?category={wybor}", headers={"User-Agent": "hax0r"})
with urlopen(zapytanie) as p:
    print(json.load(p)['value'])
