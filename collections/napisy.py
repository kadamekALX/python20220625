#        01234
napis = 'Ala ma kota a kot ma kompilator'

print(napis[0])
print(napis[0:3])
print(napis[4:])
print(napis[:3])
print(napis[:])
print(napis[-10:])
print(napis[-1])

print(napis.lower())
print(napis.upper())
print(napis.capitalize())
print(napis.title())

print(str.title(napis))

print(napis.split())
print(napis.split('a'))

podzielony_napis = napis.split()
print(podzielony_napis)
print(napis)
print( '<->'.join(podzielony_napis) )

print(napis.count('a'))
print(len(napis))

print(napis.replace('a', '*'))

for znak in napis:
    print(znak)


print('-' * 30)

print(napis.index('a'))

a = 'Ala'
b = a.replace('A', 'a')

print(a)
print(b)

samogloski = ['a', 'e', 'i', 'o', 'u', 'e']

print('a' in samogloski)
print('z' in samogloski)
