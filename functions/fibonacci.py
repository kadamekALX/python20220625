# Napisz funkcję zwracającą n-tą liczbę Fibonacciego
# Fib(0) = 0
# Fib(1) = 1
# Fib(n) = Fib(n - 1) + Fib(n - 2)
# 0 1 1 2 3 5 8 13 21 34 55 ...


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(f"{fib(0) = }")
print(f"{fib(1) = }")
print(f"{fib(6) = }")
print(f"{fib(10) = }")
print(f"{fib(40) = }")