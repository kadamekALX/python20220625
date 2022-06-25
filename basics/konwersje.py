napis = "123"
liczba = int(napis)
print(liczba)
print(type(liczba))
znow_napis = str(liczba)
print(type(znow_napis))

# x = int("Ala ma kota") # błąd

# a = int("3.14") # błąd
# a = float("3.14") # OK
# a = int(3.14) # OK
a = int(float("3.14"))
print(a)

# konwersja na bool - 0 i pusty napis konwertują się na False, reszta na True
print(f"{bool(3) = }")
print(f"{bool(0) = }")
print(f"{bool('') = }")
print(f"{bool('False') = }")
