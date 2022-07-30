# Napisz funkcję `filtruj`, która przyjmie funkcję F
# oraz listę wartości K, a następnie zwróci listę
# elementów z K, dla których funkcja F zwraca True
# filtruj(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]

def filtruj(fun, lista):
    return [x for x in lista if fun(x)]
    # wynik = []
    # for x in lista:
    #     if fun(x):
    #         wynik.append(x)
    # return wynik


print(f"{filtruj(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) = }")

from random import randint
print(f"{filtruj(lambda x: randint(0, 1) == 0, [1,2,3,4,5]) = }")

#map i filter to wbudowane funkcje
print(list(map(lambda x: x + 1, [1,2,3])))
print(list(filter(lambda x: x % 2 == 1, [1,2,3,4,5])))

print(sum(map(int, input("Podaj liczby:").split())))
