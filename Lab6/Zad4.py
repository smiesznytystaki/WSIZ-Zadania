import numpy as np

lista_poteg = [128, 64, 32, 16, 8, 4, 2, 1]
wagi = np.array(lista_poteg)
liczba_bin = np.random.randint(0, 2, size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wartosc = wartosc_liczby_bin(wagi, liczba_bin)

print("Tablica wag:", wagi)
print("Tablica liczby binarnej:", liczba_bin)
print("Wartość liczby binarnej w systemie dziesiętnym:", wartosc)
