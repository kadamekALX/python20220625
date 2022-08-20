def czy_pierwsza(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def pierwsze():
    i = 1
    while True:
        if czy_pierwsza(i):
            yield i
        i += 1

for i, x in enumerate(pierwsze(), 1):
    # if i > 10:
    #     break
    print(f"{i}: {x}")

