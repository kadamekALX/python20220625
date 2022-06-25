miastoA = input("Podaj miasto A:")
miastoB = input("Podaj miasto B:")
dystans = float(input(f"Dystans {miastoA}-{miastoB}:"))
cena_paliwa = float(input("Cena paliwa:"))
spalanie = float(input("Spalanie na 100km:"))

koszt = dystans / 100 * spalanie * cena_paliwa
print(f"Koszt przejazdu z {miastoA} do {miastoB} wynosi {koszt:.2f} PLN.")