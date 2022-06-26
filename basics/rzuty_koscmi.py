from random import randint

N = int(input("Podaj liczbę kości:"))
S = int(input("Podaj liczbę ścian:"))
M = int(input("Podaj modyfikator:"))

suma = M
i = 0
while i < N:
    suma += randint(1, S)
    i += 1

print(f"Wynik rzutu {N}k{S} + {M}: {suma}")
