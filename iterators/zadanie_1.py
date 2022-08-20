class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self):
        if self.licznik > self.limit:
            raise StopIteration
        wynik = self.licznik
        self.licznik += 1
        return wynik


for x in Counter(5):
    print(x)
