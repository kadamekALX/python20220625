"""
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
> formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10)
-> 'koszt 10 PLN\nkwota 10 brutto'

Scenariusz
1. Zdefiniować funkcję, która ma *args i **kwargs
2. W definicji funkcji
3. Zrobię sobie listę do trzymania przetworzonych napisów
4. Iteruję po napisach (*args)
      5. Iteruję po wszystkich **kwargsach
          6. Podmieniam wszystkie wystąpienia w napisie, szukam $cos
              i zamieniam na wartość z danej iteracji
      7. Przetworzony napis dodaję do listy przetworzonych napisów
8. Łączę napisy z listy przetworzonych napisów znakiem nowej linii i zwracam jako wynik działania funkcji.

Testy
- nie ma podstawienia Hello World! -> Hello World!
- dwa napisy ale bez podstawienia
    'Hello World!', 'Hello Python' -> 'Hello World!\nHello Python'
- napis z podstawieniem
    'Czesc $imie $nazwisko', imie="Jan", nazwisko="Kowalski" -> 'Czesc Jan Kowalski'
- jak zmienna nie uzyta 'Hello World', imie="Jan" -> 'Hello World'
- jak nie ma zmiennej 'Hello $imie' -> 'Hello $imie'
"""

