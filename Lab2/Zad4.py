gol = float(input("Podaj liczbe zdobytych bramek: "))
bonus = float(input("Podaj liczbe dodatkowych punktow bonusowych: "))

punkty_z_bramek = gol * 10

# A)
if gol > 10:
    wynikA = punkty_z_bramek + 10 + bonus
elif gol > 5:
    wynikA = punkty_z_bramek + 5 + bonus
else:
    wynikA = punkty_z_bramek + bonus

print("A - Calkowity wynik druzyny:", wynikA)

# B)
wynikB = punkty_z_bramek + bonus
if gol > 5:
    wynikB += 5
if gol > 10:
    wynikB += 10

print("B - Calkowity wynik druzyny:", wynikB)

