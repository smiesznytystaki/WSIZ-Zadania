x = float(input("Podaj pierwsza liczbe "))
y = float(input("Podaj druga liczbe "))
z = float(input("Podaj trzecia liczbe "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("Liczby w kolejnosci od najmniejszej do najwiekszej:", x, y, z)