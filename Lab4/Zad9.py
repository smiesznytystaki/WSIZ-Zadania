lista_zakupow = {"Chleb": 4.50,"Mleko": 3.40,"Masło": 5.80,"Ser": 13.50}

print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"{artykul}: {kwota} zł")

suma_wydatkow = sum(lista_zakupow.values())
print(f"\nSuma wydatków: {suma_wydatkow} zł")
