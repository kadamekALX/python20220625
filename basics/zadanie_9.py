rok_ur = int(input("Podaj rok urodzenia:"))
obecny_rok = 2022
if obecny_rok - rok_ur >= 18:
    print(f"Jesteś pełnoletni!")
else:
    print(f"Nie jesteś pełnoletni!")
