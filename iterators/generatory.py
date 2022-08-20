# jeżeli `yield` pojawi się gdziekolwiek wewnątrz funkcji to funkcja staje się generatorem

def Generator():
    yield 1
    yield 2
    yield 3

def parzyste_do(x):
    for i in range(0, x, 2):
        print(f"yield {i}")
        yield i

# print(Generator())
g = Generator()
# it = iter(g)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
for x in g:
    print(x)
for i in parzyste_do(11):
    print(f"{i = }")

