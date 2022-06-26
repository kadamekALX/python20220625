lista = [3, 5, -2, 0, -4, -1, 7, 6]
dodatnie, ujemne = 0, 0

for liczba in lista:
    if liczba > 0:
        dodatnie += 1
    elif liczba < 0:
        ujemne += 1

print(f"{dodatnie = }")
print(f"{ujemne = }")