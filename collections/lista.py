# Lista jest uporządkowana
# Lista jest mutowalna - możemy modyfikować zawartość listy oraz dodawać do niej nowe elementy

x = [10, 20, 30, 40]
print(x)
print(type(x))

# tworzenie pustej
pusta1 = []
pusta2 = list()

print(f"{x = }")

# modyfikacja elementów jest możliwa
x[2] = 100
print(f"{x = }")

# dodawanie nowych elementów
print(f"{len(x) = }")
x.append(200)  # append() dostawia nową wartość na końcu listy
print(f"{x = }")
print(f"{len(x) = }")

# wstawianie elementu na dowolnej pozycji
# niezalecane, bo im więcej elementów na prawo tym wolniej będzie działać
x.insert(0, 900)
print(f"{x = }")

print(f"{sum(x) = }")
