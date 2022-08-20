# Zaimplementuj generator zwracający listę wszystkich możliwych
# rozgrywek na podstawie dostarczonej listy graczy. Uwzględnij
# rewanże.
# Przykładowe użycie:
# for player_1, player_2 in tournament(['A', 'B', 'C']):

def tournament(gracze):
    for i in range(len(gracze)):
        for j in range(i + 1, len(gracze)):
            yield gracze[i], gracze[j]

for para in tournament(['A', 'B', 'C']):
    print(para)

for player_1, player_2 in tournament(['A', 'B', 'C']):
    print(f"{player_1} vs {player_2}")

# A vs B
# A vs C
# B vs C
