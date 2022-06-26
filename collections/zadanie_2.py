liczby = []

while len(liczby) < 10:
    napis = input("Podaj liczbę lub 'koniec':")
    if napis == 'koniec':
        break
    liczba = int(napis)
    liczby.append(liczba)

print(liczby)
if liczby:  # jeśli lista liczb jest niepusta
    print(f"Średnia z liczb {liczby} wynosi {sum(liczby) / len(liczby)}")
