# Napisz funkcję zwracającą n-tą liczbę Fibonacciego
# Fib(0) = 0
# Fib(1) = 1
# Fib(n) = Fib(n - 1) + Fib(n - 2)
# 0 1 1 2 3 5 8 13 21 34 55 ...

# rekurencyjnie
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# iteracyjnie - czas: O(n), pamięć: O(1)
def fib(n):
    a, b = 0, 1
    for i in range(n):
        tmp = a + b
        a = b
        b = tmp
    return a


print(f"{fib(0) = }")
print(f"{fib(1) = }")
print(f"{fib(6) = }")
print(f"{fib(10) = }")
print(f"{fib(40) = }")
print(f"{fib(100) = }")
print(f"{fib(10000) = }")