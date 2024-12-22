import time

czas = int(input("Podaj czas w sekundach do odliczenia: "))

for sekunda in range(czas, 0, -1):
    print(f"Pozostało: {sekunda} sekund")
    time.sleep(1)

print("Czas upłynął!")