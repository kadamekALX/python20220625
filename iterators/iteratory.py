class Iterowalna:
    # wywoływana raz na początku iteracji - musi zwrócić coś co posiada metodę __next__()
    def __iter__(self):
        print("__iter__")
        self.licznik = 0
        return self

    # kolejne wywołania metody __next__ powinny zwracac kolejne wartości
    # jeżeli nie ma wartości do zwrócenia to podnosimy wyjątek StopIteration
    def __next__(self):
        print("__next__")
        if self.licznik > 3:
            raise StopIteration
        wynik = self.licznik
        self.licznik += 1
        return wynik


x = Iterowalna()
print("-" * 20)
it = iter(x)  # to wywoła x.__iter__()
while True:
    try:
        i = next(it)  # to wywoła it.__next__()
        print(f"{i = }")
    except StopIteration:
        break
print("-" * 20)
for i in x:
    print(i)