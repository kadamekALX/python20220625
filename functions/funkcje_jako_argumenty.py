def f(x):
    return 2 * x

def wywolaj_z_argumentem(fun, x):
    wynik = fun(x)
    print(f"Wynik funkcji = {wynik}")


print(f"{f(5) = }")
g = f
print(f"{g(10) = }")

wywolaj_z_argumentem(f, 15)
wywolaj_z_argumentem(print, "Siema")
wywolaj_z_argumentem(input, "Podaj dane:")

# Napisz funkcję `zaaplikuj`, która przyjmie funkcję F
# oraz listę wartości, a następnie zwróci listę
# wyników funkcji F dla wszystkich wartości z listy
# zaaplikuj(plus1, [1,2,3]) == [2,3,4]
# [a, b, c] -> [f(a), f(b), f(c)]
def zaaplikuj(f, lista):
    return [f(x) for x in lista]
    # wyniki = []
    # for x in lista:
    #     wyniki.append(f(x))
    # return wyniki

print(f"{zaaplikuj(f, [5, 10, 15]) = }")

