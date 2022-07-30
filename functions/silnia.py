# Zaimplementuj funkcję obliczającą silnie dla zadanej wartości.
# 5! = 1 * 2 * 3 * 4 * 5
# n! = 1 * 2 * 3 * ... * (n - 1) * n
# 0! = 1

def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

print(f"{silnia(0) = }")
print(f"{silnia(2) = }")
print(f"{silnia(5) = }")
print(f"{silnia(10) = }")