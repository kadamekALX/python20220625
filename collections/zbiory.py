# zbiór (ang. set)
# mutowalny
# nieuporzadkowany

moj_zbior = {10, 20, 30, 40, 50}

print(type(moj_zbior))
print(moj_zbior)

cos = {}  # uwaga! to stworzy pusty slownik!!!
print(cos)
print(type(cos))

pusty_zbior = set()  # w ten sposb tworzymy pusty zbior
print(pusty_zbior)
print(type(pusty_zbior))

# w zbiorze mamy tylko unikalne elementy
moj_zbior.add(60)
print(moj_zbior)

moj_zbior.add(60)
moj_zbior.add(60)
moj_zbior.add(60)
moj_zbior.add(60)
moj_zbior.add(60)
moj_zbior.add(60)
print(moj_zbior)

# w zbiorze mozemy trzymac niemutowalne typy danych
# moge trzymac, np.: tuple, str, int, float, etc...
# nie moge np.: list, set
# moj_zbior.add([1,2,3])

moj_zbior.remove(60)
print(moj_zbior)

moj_zbior.update([1, 2, 3])
print(moj_zbior)

# zbior nie obsluguje operatora dostepu
# print(moj_zbior[0])

for liczba in moj_zbior:
    print(liczba)

print('-' * 30)

# przeksztalcanie jednego typu kolekcji na drugi
moja_lista = list(moj_zbior)  # zbior -> lista
print(moja_lista)
print(type(moja_lista))

moja_tupla = tuple(moja_lista)
print(moja_tupla)
print(type(moja_tupla))

moja_lista = [1,2,3,30,40,40,40,40,40,40,40,40]
moj_zbior = set(moja_lista)
print(moj_zbior)
print(type(moj_zbior))

print('-' * 30)

# operacje teoriomnogosciowe
a = {1, 2, 3}
b = {1, 2, 4, 5}

# suma zbiorow
print(a.union(b))
print(a | b)

# czesc wspolna
print(a.intersection(b))
print(a & b)

# roznica
print(a.difference(b))
print(a - b)

# roznica symetryczna
# od sumy zbiorow odejmujemy czesc wspolna
print(a.symmetric_difference(b))
print(a ^ b)

a = {1, 2, 3}
b = {1, 2, 4, 5}
c = {1, 2}
d = {6, 7}
e = {1, 2, 3}

print(a.isdisjoint(d))  # czy zbiory sa rozlaczne

print(c < a)  # czy c jest podzbiorem a
print(a > c)  # czy a jest nadzbiorem c

print(e < a)
print(e <= a)  # czy e jest podzbiorem a, zbiory moga miec te same elementy
