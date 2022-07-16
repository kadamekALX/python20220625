"""
Napisz program wypisujący wszystkie liczby od 0 do 100,
podzielne przez 3 lub podzielne przez 5. Wypisz także jak dużo
takich liczb wystąpiło w tym przedziale.

Liczby podzielne przez 3 lub 5:
0
3
5
...
96
99
100
W przedziale 0-100 jest 48 liczb podzielnych przez 3 lub 5
"""

# PEP8: https://peps.python.org/pep-0008/

ile = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        ile += 1
        print(i)

print(f'W przedziale od 0-100 jest {ile} liczb podzielnych przez 3 lub 5')
