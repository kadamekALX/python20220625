from random import random  # random() daje losowy float z przedziału [0; 1)

punkty_wew_kola = 0
punktow = 1000000
i = 1
while i <= punktow:
    # losujemy punkt w kwadracie
    x = random()
    y = random()
    #sprawdzamy, czy punkt jest w kole
    if (x ** 2 + y ** 2) ** 0.5 <= 1:
        punkty_wew_kola += 1
    i += 1

pi = 4 * punkty_wew_kola / punktow
print(pi)