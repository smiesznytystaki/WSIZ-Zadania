import math
import keyword

def wypisz_funkcje(modul, nazwa_modulu):
    funkcje = [f for f in dir(modul) if callable(getattr(modul, f))]
    print(f"Funkcje w module {nazwa_modulu}:")
    print(", ".join(funkcje) if funkcje else "Brak funkcji w module.")
    print()

wypisz_funkcje(math, "math")
wypisz_funkcje(keyword, "keyword")