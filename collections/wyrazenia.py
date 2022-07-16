"""
wyrazenia / comprehensions
- skrocony, "prostszy" sposob tworzenia list, zbiorow, slownikow
- syntactic sugar

wyrazenia listowe (ang. list comprehensions)
"""

wynik = []
for liczba in range(0, 11):
    wynik.append(liczba + 10)

print(wynik)

wynik = [liczba + 10 for liczba in range(0, 11)]
print(wynik)

print('-' * 30)

wynik = []
for liczba in range(0, 11):
    wynik.append(liczba ** 2)

print(wynik)

wynik = [liczba ** 2 for liczba in range(0, 11)]
print(wynik)

print('-' * 30)

wynik = []
for i in range(2, 101, 2):
    wynik.append(i)

print(wynik)

wynik = [i for i in range(2, 101, 2)]
print(wynik)

print('-' * 30)
##################

wynik = []
for liczba in range(0, 101):
    if liczba % 2 == 0:
        wynik.append(1)
    else:
        wynik.append(-1)

print(wynik)


wynik = [1 if liczba % 2 == 0 else -1 for liczba in range(0, 101)]
print(wynik)

print('-' * 30)
##################

wynik = []
for liczba in range(-10, 11):
    if liczba > 0:
        wynik.append(liczba)
    else:
        continue

print(wynik)

wynik = [liczba for liczba in range(-10, 11) if liczba > 0]
print(wynik)

print('-' * 30)
##################

wynik = []
for liczba in range(-10, 11):
    if liczba > 0:
        if liczba % 2 == 0:
            wynik.append(1)
        else:
            wynik.append(-1)
    else:
        continue

print(wynik)

wynik = [1 if liczba % 2 == 0 else -1 for liczba in range(-10, 11) if liczba > 0]
print(wynik)

print('-' * 30)

# set comprehensions
wynik = {litera for litera in 'Ala ma kota'}
print(wynik)


# dict comprehensions
napis = 'Ala ma kota'
wynik = {litera: napis.count(litera) for litera in napis}
print(wynik)

