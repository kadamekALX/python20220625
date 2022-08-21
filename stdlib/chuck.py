import tkinter as tk
from urllib.request import urlopen, Request
import json

zapytanie = Request("https://api.chucknorris.io/jokes/categories", headers={"User-Agent": "hax0r"})
with urlopen(zapytanie) as p:
    kategorie = json.load(p)

root = tk.Tk()

strvar = tk.StringVar()
strvar.set(kategorie[0])
lista = tk.OptionMenu(root, strvar, *kategorie)
lista.grid(row=0, column=0)


root.mainloop()