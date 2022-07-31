def niebezpieczna_operacja(x):
    if x == 3:
        raise ValueError("Nie wolno przekazywac 3")
        # print("Nie wolno przekazywac 3")
    return 2 * x + 1


try:
    x = int(input("Podaj x:"))
    3 / x
    print(f"{niebezpieczna_operacja(x) = }")
except ValueError:  # wewnątrz `except` obsługujemy wyjątek. Po obsłużeniu program wznawia normalne działanie
    print("Złapałem ValueError!")
except ZeroDivisionError:
    print("Nie dziel przez 0!")
    raise  # przepuszcza ten wyjątek, ktory właśnie złapaliśmy


print("ciąg dalszy programu...")

