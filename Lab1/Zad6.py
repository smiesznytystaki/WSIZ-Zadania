import random

droga = float(input("Podaj pokonaną drogę przez samochód: "))
spalanie = float(input("Podaj średnie spalanie samochodu w litrach na 100km: "))
zuzycie_paliwa = (droga*spalanie) / 100
koszt_podrozy = zuzycie_paliwa * 6.5
print("Przewidywane zużycie paliwa wynosi: "+str(zuzycie_paliwa)+" litrów")
print("Koszt podróży wynosi: "+str(koszt_podrozy)+" zł")


droga = random.randint(100,1000)
spalanie = float(input("Podaj średnie spalanie samochodu w litrach na 100km: "))
cena_paliwa = float(input("Podaj cene paliwa: "))
zuzycie_paliwa = (droga*spalanie) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa
print("Przewidywane zużycie paliwa wynosi: "+str(zuzycie_paliwa)+" litrów")
print("Koszt podróży wynosi: "+str(koszt_podrozy)+" zł")

droga = random.randint(100, 1000)
spalanie = float(input("Podaj średnie spalanie samochodu w litrach na 100 km: "))
cena_paliwa = float(input("Podaj cene paliwa: "))
zuzycie_paliwa = (droga * spalanie) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa
print(f"Przewidywane zużycie paliwa wynosi: {zuzycie_paliwa:.2f} litrów")
print(f"Koszt podróży wynosi: {koszt_podrozy:.2f} zł")
