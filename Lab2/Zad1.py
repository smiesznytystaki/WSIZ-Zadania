x = float(input("Podaj liczbe uzyskanych punktow: "))

if x > 80:
    print("Zaliczyles egzamin w terminie 0.")
elif 50 <= x <= 80:
    print("Mozesz poprawic wynik egzaminu.")
else:
    print("Musisz poprawic egzamin.")