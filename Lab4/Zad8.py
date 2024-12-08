stopnie = ("Szeregowy","Kapral","Sierżancie","Porucznik","Kapitan","Major","Pułkownik",)

ilosc_stopni = len(stopnie)

Major_index = stopnie.index("Major")

Pulkownik_wystepowanie = "Pułkownik" in stopnie

print("Liczba stopni wojskowych:", ilosc_stopni)
print("Indeks 'Major':", Major_index)
print("Czy 'Pułkownik' znajduje się w krotce?:", Pulkownik_wystepowanie)
