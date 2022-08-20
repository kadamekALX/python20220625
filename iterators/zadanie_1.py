class CounterIterator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __next__(self):
        if self.a == self.b:
            raise StopIteration
        w = self.a
        self.a += 1
        return w

class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return CounterIterator(0, self.limit)


for x in Counter(5):
    print(x)
