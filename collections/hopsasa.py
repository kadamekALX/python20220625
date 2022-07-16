# zamiast podzielnych przez 7 wypisz "Bum" (i wszystkie zasady wynikające z tego)

# print("asdf", end="")
# print("qwer")

for i in range(1, 101):
    napis = ""
    if i % 3 == 0:
        napis += "Hopsasa"
    if i % 5 == 0:
        napis += "Tralala"
    if i % 7 == 0:
        napis += "Bum"

    if napis:  # czy napis jest niepusty
        print(napis)
    else:
        print(i)


# for i in range(1, 101):
#     cos_wypisane = False
#     if i % 3 == 0:
#         print("Hopsasa", end="")
#         cos_wypisane = True
#     if i % 5 == 0:
#         print("Tralala", end="")
#         cos_wypisane = True
#     if i % 7 == 0:
#         print("Bum", end="")
#         cos_wypisane = True
#
#     if not cos_wypisane:
#         print(i, end="")
#     print()
# test