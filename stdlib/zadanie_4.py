# Napisz program z graficznym interfejsem użytkownika (GUI) do
# obliczania kosztów przejazdu na zadanym dystansie na podstawie
# spalania samochodu oraz ceny paliwa.
# Skorzystaj z modułu tkinter.

import tkinter as tk
import tkinter.messagebox as msg


def oblicz():
    d = float(entry_dystans.get())
    s = float(entry_spalanie.get())
    c = float(entry_cena.get())
    wynik = d * s * c / 100
    msg.showinfo(title="Koszt przejazdu", message=f"{wynik:.2f} PLN")


root = tk.Tk()

root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

label_dystans = tk.Label(master=root, text="Dystans w km")
label_dystans.grid(row=0, column=0, sticky=tk.E)
entry_dystans = tk.Entry(master=root)
entry_dystans.grid(row=0, column=1, sticky=tk.EW)

label_spalanie = tk.Label(master=root, text="Spalanie na 100km")
label_spalanie.grid(row=1, column=0, sticky=tk.E)
entry_spalanie = tk.Entry(master=root)
entry_spalanie.grid(row=1, column=1, sticky=tk.EW)

label_cena = tk.Label(master=root, text="Cena za litr paliwa")
label_cena.grid(row=2, column=0, sticky=tk.E)
entry_cena = tk.Entry(master=root)
entry_cena.grid(row=2, column=1, sticky=tk.EW)

przycisk = tk.Button(master=root, text="Oblicz", command=oblicz)
przycisk.grid(row=3, column=0, sticky=tk.NSEW)

root.mainloop()
