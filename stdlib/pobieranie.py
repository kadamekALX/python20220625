from urllib.request import urlopen


with urlopen("http://api.nbp.pl/api/cenyzlota/?format=json") as plik:
    print(plik.read().decode("utf-8"))

with urlopen("https://pbs.twimg.com/profile_images/1496955167312388097/-Z2IzSXJ_400x400.jpg") as plik:
    with open("pepe.jpg", 'wb') as obrazek:
        obrazek.write(plik.read())
