def niebezpieczna_operacja(x):
    if x == 3:
        raise ValueError("Nie wolno przekazywac 3")
        # print("Nie wolno przekazywac 3")
    return 2 * x + 1


try:
    x = int(input("Podaj x:"))
    3 / x
    print(f"{niebezpieczna_operacja(x) = }")
# wewnątrz `except` obsługujemy wyjątek. Po obsłużeniu program wznawia normalne działanie
except ValueError as e:  # zapisujemy złapany wyjątek pod zmienną `e`
    print("Złapałem ValueError!", e)
except ZeroDivisionError:
    print("Nie dziel przez 0!")
    raise  # przepuszcza ten wyjątek, ktory właśnie złapaliśmy
finally:  # wykona się zawsze, nawet jak nie złapiemy wyjątku
    print("To się wykona zawsze!")


print("ciąg dalszy programu...")

