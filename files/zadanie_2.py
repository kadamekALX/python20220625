# Napisz program wczytujący plik z logami aktywności użytkowników
# w systemie. Na podstawie wczytanych danych wyświetl informację o
# sumarycznym czasie przebywania każdego użytkownika w systemie.
# Przykład użycia:
# $ python read_logs.py logs.txt
# Czas przebywania w systemie:
# - user-1: 92 s
# - user-2: 51 s
# - user-3: 20 s

ostatnie_logowanie = {}
suma_czasu = {}

with open("logs.txt") as plik:
    # wiersze = plik.readlines()
    # print(wiersze)
    for wiersz in plik:
        user, op, czas = wiersz.split(";")
        czas = int(czas)
        if op == "LOGIN":
            ostatnie_logowanie[user] = czas
        elif op == "LOGOUT":
            dlugosc_ostatniej_sesji = czas - ostatnie_logowanie[user]
            if user not in suma_czasu:
                suma_czasu[user] = 0
            suma_czasu[user] += dlugosc_ostatniej_sesji

for user, czas in sorted(suma_czasu.items()):
    print(f"{user}: {czas}s")
