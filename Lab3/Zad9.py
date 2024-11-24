imie = input("Podaj swoje imię: ")
print(f"Witaj {imie}")

wiek = int(input("Podaj swój wiek: "))
print(f"Twój wiek to: {wiek}")

nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0] + nazwisko[0]
print(f"Inicjały: {inicjaly}")

lancuch = input("Podaj łańcuch tekstowy: ")
print(lancuch * 5)

lancuch1 = input("Podaj drugi łańcuch: ")
polaczone = lancuch + lancuch1
print(f"Połączony łańcuch: {polaczone}")

pierwsza_polowa = lancuch[:len(lancuch) // 2] + lancuch1[:len(lancuch1) // 2]
print(f"Połączona pierwsza połowa obu łańcuchów: {pierwsza_polowa}")
