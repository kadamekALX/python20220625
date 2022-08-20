# Zaimplementuj iterator zwracający jedynie samogłoski z zadanego
# ciągu znaków:
# Przykładowe użycie:
# for char in Vowels('ala ma kota a kot ma ale'):

# napis = "asdf"
# for x in napis:
#     print(x)
# a
# s
# d
# f
# for x in range(len(napis)):
#     print(x)
# 0
# 1
# 2
# 3

class Vowels:
    def __init__(self, napis):
        self.napis = napis

    def __iter__(self):
        self.pozycja_wznowienia = 0
        return self

    def __next__(self):
        for i in range(self.pozycja_wznowienia, len(self.napis)):
            if self.napis[i].lower() in "aeiouy":
                self.pozycja_wznowienia = i + 1
                return self.napis[i]
        raise StopIteration


v = Vowels("Ala ma kota a kot ma Ale")
for x in v:
    print(x)
