from datetime import datetime

def formatuj_date(data):
    miesiace = {
        1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia", 5: "maja",
        6: "czerwca", 7: "lipca", 8: "sierpnia", 9: "września",
        10: "października", 11: "listopada", 12: "grudnia"
    }
    return f"{data.day} {miesiace[data.month]} {data.year}"

data_laboratoriow = datetime(2024, 12, 15)
data_kolokwium = datetime(2024, 12, 17)
dzisiaj = datetime.now()

if dzisiaj > data_laboratoriow:
    dni_od_laboratoriow = (dzisiaj - data_laboratoriow).days
    print(f"Od ostatnich laboratoriów ({formatuj_date(data_laboratoriow)}) upłynęło {dni_od_laboratoriow} dni.")
else:
    dni_do_laboratoriow = (data_laboratoriow - dzisiaj).days
    print(f"Do ostatnich laboratoriów ({formatuj_date(data_laboratoriow)}) zostało {dni_do_laboratoriow} dni.")

dni_do_kolokwium = (data_kolokwium - dzisiaj).days
print(f"Do kolokwium ({formatuj_date(data_kolokwium)}) zostało {dni_do_kolokwium} dni.")