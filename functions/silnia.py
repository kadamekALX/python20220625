# Zaimplementuj funkcję obliczającą silnie dla zadanej wartości.
# 5! = 1 * 2 * 3 * 4 * 5
# n! = 1 * 2 * 3 * ... * (n - 1) * n
# 0! = 1

# definicja rekurencyjna
# 0! = 1
# n! = n * (n - 1)!

# silnia iteracyjnie
# def silnia(n):
#     wynik = 1
#     for i in range(1, n + 1):
#         wynik *= i
#     return wynik

# silnia rekurencyjnie
def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)


print(f"{silnia(0) = }")
print(f"{silnia(2) = }")
print(f"{silnia(5) = }")
print(f"{silnia(10) = }")
print(f"{silnia(13) = }")