import re

napis = "abc-123_QWE"

wyrazenie = re.compile(r"-(\d+)")
wynik = wyrazenie.search(napis)
print(wynik)
print(re.sub(wyrazenie, r"XXX\1YYY", napis))
print(re.sub(r"([a-z]+)-(\d+)", r"\2-\1", napis))

with open("tekst.txt") as plik:
    tekst = plik.read()

kody = re.compile(r"\b\d{2}-\d{3}\b")
print(kody.findall(tekst))
print(re.findall(r"\b\d{2}-\d{3}\b", tekst))
# \d{2} (?:Jan|Feb|Mar) \d{4}
# [\w\-]+@[\w\-]+(?:\.[\w\-]+)+