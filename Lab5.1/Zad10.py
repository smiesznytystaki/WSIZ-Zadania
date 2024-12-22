import random

min_val = int(input("Podaj dolną granicę przedziału: "))
max_val = int(input("Podaj górną granicę przedziału: "))

krotka = tuple(random.randint(min_val, max_val) for _ in range(10))
print(f"Losowa krotka: {krotka}")

iloczyn = 1
for liczba in krotka:
    iloczyn *= liczba

srednia_geometryczna = iloczyn ** (1 / len(krotka))
print(f"Średnia geometryczna krotki: {srednia_geometryczna}")
