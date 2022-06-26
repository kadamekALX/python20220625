dni = 7
suma = 0
i = 0
while i < dni:
    suma += float(input(f"Podaj temperaturę dnia {i}: "))
    i += 1

srednia = suma / dni
print(f"Średnia temperatura z {dni} dni wynosi {srednia}.")