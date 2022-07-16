"""
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.

Przykład:
0123456789
Ala <kota>, a kot ma Alę
4
1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam czy:
      - mam zliczac
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam
"""

napis = input('Podaj napis: ')

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Niepoprawna liczba nawiasow!')
    exit()

liczba_znakow = 0
czy_zliczac = False

for znak in napis:
    if znak == '<':
        czy_zliczac = True
    elif znak == '>':
        czy_zliczac = False
    elif czy_zliczac == True:
        liczba_znakow += 1

print(liczba_znakow)
