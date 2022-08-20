# Napisz program wczytujący listę adresów email z pliku i tworzący
# nowy plik z odfiltrowaną zawartością.
# Wejściowy plik może zawierać duplikaty adresów, ten sam adres
# pisany różną wielkością liter, linie zawierające białe znaki oraz
# błędne adresy email (brak znaku @ lub występuje on wiele razy).
# Wynikowy plik powinien zawierać unikalne, posortowane, poprawne
# adresy email.

# with open("emails.txt") as plik:
#     maile = set()
#     for wiersz in plik:
#         if wiersz.count("@") != 1:
#             continue
#         wiersz = wiersz.lower()
#         wiersz = wiersz.strip()  # usuwa białe znaki z początku i końca napisu
#         maile.add(wiersz)
#
# with open("clean_emails.txt", "w") as plik:
#     for x in sorted(maile):
#         plik.write(x)
#         plik.write('\n')

with open("emails.txt") as plik_in, open("clean_emails.txt", "w") as plik_out:
    plik_out.write("\n".join(sorted({w.lower().strip() for w in plik_in if w.count("@") == 1})))
