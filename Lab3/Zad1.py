paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Czas: {czas}s, Pozostałe paliwo: {paliwo} litrów")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1
    if paliwo <= 0:
        print("Koniec lotu.")
        break