def oblicz_bmi():
    waga = float(input("Podaj wagę (kg): "))
    wzrost = float(input("Podaj wzrost (m): "))

    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi < 25:
        zakres = "pożądana masa ciała"
    elif 25 <= bmi < 30:
        zakres = "nadwaga"
    elif 30 <= bmi < 35:
        zakres = "otyłość I stopnia"
    elif 35 <= bmi < 40:
        zakres = "otyłość II stopnia"
    else:
        zakres = "otyłość III stopnia"

    print(f"BMI: {bmi:.2f}, Zakres: {zakres}")

oblicz_bmi()
