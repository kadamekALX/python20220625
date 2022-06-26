# zamiast podzielnych przez 7 wypisz "Bum" (i wszystkie zasady wynikające z tego)

# print("asdf", end="")
# print("qwer")

for i in range(1, 101):
    napis = ""
    if i % 3 == 0:
        napis += "Hopsasa"
    if i % 5 == 0:
        napis += "Tralala"

    if napis:  # czy napis jest niepusty
        print(napis)
    else:
        print(i)