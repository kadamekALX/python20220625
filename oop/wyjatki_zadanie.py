# Pobierz od użytkownika liczbę całkowitą (int) X
# Jeśli użytkownik poda coś innego to pytaj do skutku
# Wypisz 2 * X + 1

def przyjmij_int():
    while True:
        try:
            x = int(input("Podaj liczbę całkowitą:"))
            return x
        except ValueError:
            print("To nie jest liczba całkowita!")


print(2 * przyjmij_int() + 1)
