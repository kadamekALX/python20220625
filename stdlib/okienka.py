import tkinter as tk  # nadajemy alias 'tk' modułowi tkinter
import tkinter.filedialog as fd
import tkinter.messagebox

def fun():
    tekst = entry.get()
    print(f"Obecna treść pola: {tekst}")
    nazwa_pliku = fd.askopenfilename()
    label.configure(text=nazwa_pliku)

def wyswietl_popup():
    tkinter.messagebox.showinfo(title="Tytul okna", message="Tresc wiadomości")

root = tk.Tk()

przycisk = tk.Button(master=root, text="Click me!", command=lambda: print("Wciśnięto przycisk!"))
przycisk.grid(row=0, column=0)
przycisk2 = tk.Button(master=root, text="Click me 2!", command=wyswietl_popup)
przycisk2.grid(row=1, column=1)

label = tk.Label(master=root, text="To jest label")
label.grid(row=1, column=0)

entry = tk.Entry(master=root)
entry.grid(row=0, column=1)

root.mainloop()

