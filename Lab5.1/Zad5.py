import random

liczby = list(range(1, 50))

wylosowane_liczby = random.sample(liczby, 6)

wylosowane_liczby.sort()

print(f"Wynik losowania 'Dużego Lotka': {wylosowane_liczby}")