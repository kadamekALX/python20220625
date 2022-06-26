# Tupla jest uporządkowana - każdy element ma przypisany indeks (od 0)
# Tupla jest niemutowalna - raz stworzonej tupli nie możemy modyfikować
x = (10, "napis", True, None, (1, 2, 3))
print(x)
print(type(x))

# sprawdzenie dlugosci
print(f"{len(x) = }")

# dostęp do elementów
print(x[2])
print(x[4])
print(x[4][0])
print(f"{x[len(x) - 1] = }")
print(f"{x[-1] = }")  # ujemne indeksy są liczone od końca

# x[2] = False  # Błąd, bo tupla jest niemutowalna

# tworzenie pustej tupli
pusta1 = ()
pusta2 = tuple()

# tworzenie 1-elementowej tupli
jeden_element = (1,)

# nawiasy w większości przypadków możemy pominąć
y = 1, 2, 3
print(f"{y = }")

# tuple assignment
a, b = 10, 20
print(f"{a = }")
print(f"{b = }")
a, b = b, a
print(f"{a = }")
print(f"{b = }")

# slicing - pozwala "wyciąć" wskazany fragment tupli
# Wynikiem jest nowa tupla zawierająca tylko wskazane elementy
# tab[B:E:S] - wycinek zaczynający się od indeksu B, kończący się przed indeksem E,
# wybierający co S-ty element
print(f"{x = }")
print(f"{x[1:3] = }")
print(f"{x[1:] = }") # pominięcie drugiego indeksu oznacza wycinek "do końca"
print(f"{x[:3] = }") # pominięcie pierwszego indeksu oznacza wycinek "od początku"
print(f"{x[:] = }")
print(f"{x[1:4:2] = }")
