import pandas as pd

# Tworzymy DataFrame
data = {
    'Numer identyfikacyjny': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja (w PLN)': [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(data)

# a)
praca_pensja_wieksza_5000 = df[df['Pensja (w PLN)'] > 5000]
print("Pracownicy z pensją większą niż 5000 PLN:")
print(praca_pensja_wieksza_5000)

# b)
posortowani_wiek = df.sort_values(by='Wiek')
print("\nPracownicy posortowani według wieku:")
print(posortowani_wiek)

# c)
srednia_pensja_po_stanowisku = df.groupby('Stanowisko')['Pensja (w PLN)'].mean()
print("\nŚrednia pensja według stanowiska:")
print(srednia_pensja_po_stanowisku)

# d)
data_zmiana_stanowiska = {
    'Numer identyfikacyjny': [1, 2, 3],
    'Stanowisko': ['Konsultant', 'Manager', 'Programista'],
    'Wiek': [36, 29, 41],
    'Pensja (w PLN)': [8500, 7500, 6500]
}

df_zmiana = pd.DataFrame(data_zmiana_stanowiska)
df_po_awansie = pd.merge(df, df_zmiana, on='Numer identyfikacyjny', suffixes=('_pierwsze', '_po_awansie'))
print("\nDane pracowników po awansie:")
print(df_po_awansie)

# e)
df_po_awansie.to_csv('pracownicy_po_awansie.csv', index=False)

# f)
df_wczytane = pd.read_csv('pracownicy_po_awansie.csv')
print("\nDane wczytane z pliku CSV:")
print(df_wczytane)
