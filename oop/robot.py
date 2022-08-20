# Wyobraźmy sobie robota, który może poruszać się naprzód i obracać w lewo lub prawo o 90 stopni.
# Napisz klasę Robot, która będzie przechowywała informację o położeniu robota na płaszczyźnie (2 liczby całkowite) oraz
# kierunku w jakim jest zwrócony (N - północ, S - południe, E - wschód, W - zachód).
# Klasa powinna udostępniać metody:
# - wypisz() - wypisuje położenie i zwrot robota,
# - lewo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku przeciwnym do ruchu wskazówek zegara (np. N zamieniamy na W),
# - prawo() - zmienia kierunek, w którym zwrócony jest Robot o 90 stopni w kierunku zgodnym z ruchem wskazówek zegara (np. N zamieniamy na E),
# - naprzod() - przemieszcza robota krok w kierunku, w którym obecnie jest zwrócony (przykładowo krok na wschód powoduje zmianę współrzędnych z (x, y) na (x + 1, y)),
# - wykonaj(ciag_instrukcji), gdzie ciąg instrukcji to napis złożony z liter N, P, L oznaczających odpowiednio: Naprzód, Prawo, Lewo (tzn. instkcja N odpowiada jednemu wywołaniu metody naprzod(), P - prawo(), L - lewo()).
# Wywołanie metody wykonaj() powinno przemieścić robota zgodnie z przekazanymi instrukcjami. Przykład:
# - początkowe położenie robota: (0, 0), zwrot: N,
# - ciąg instrukcji: NNPNLNPP,
# - końcowe położenie robota: (1, 3), zwrot: S.


class Robot:
    # pola klasowe
    kierunki = ("N", "E", "S", "W")
    ruchy = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self):
        self.x = 0
        self.y = 0
        self.zwrot = 0

    def prawo(self):
        self.zwrot = (self.zwrot + 1) % 4

    def lewo(self):
        self.zwrot = (self.zwrot + 3) % 4

    def naprzod(self):
        self.x += Robot.ruchy[self.zwrot][0]
        self.y += Robot.ruchy[self.zwrot][1]

    def wypisz(self):
        print(f"x={self.x}, y={self.y}, zwrot: {Robot.kierunki[self.zwrot]}")

    def wykonaj(self, ciag_instrukcji):
        metody = {'N': self.naprzod, 'P': self.prawo, 'L': self.lewo}
        for litera in ciag_instrukcji:
            metody[litera]()


r = Robot()
r.wypisz()
r.wykonaj("NNPNLNPP")
r.wypisz()
