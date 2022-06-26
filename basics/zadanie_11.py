x = int(input("X:"))
y = int(input("Y:"))

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Poza planszą")
elif x <= 10:
    if y <= 10:
        print("Lewy dolny róg")
    elif y >= 90:
        print("Lewy górny róg")
    else:
        print("Lewa krawędź")
elif x >= 90:
    if y <= 10:
        print("Prawy dolny róg")
    elif y >= 90:
        print("Prawy górny róg")
    else:
        print("Prawa krawędź")
else:
    if y <= 10:
        print("Dolna krawędź")
    elif y >= 90:
        print("Górna krawędź")
    else:
        print("Środek")
