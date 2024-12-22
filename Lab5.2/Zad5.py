import pandas as pd

# Tworzymy DataFrame
data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}

df = pd.DataFrame(data)

# a)
studenci_4_wzrost = df[df['Ocena'] > 4]
print("Studenci z oceną większą niż 4:")
print(studenci_4_wzrost)

# b)
studenci_posortowani_wiek = df.sort_values(by='Wiek')
print("\nStudenci posortowani według wieku:")
print(studenci_posortowani_wiek)

# c)
sredni_wiek_po_ocenie = df.groupby('Ocena')['Wiek'].mean()
print("\nŚredni wiek według ocen:")
print(sredni_wiek_po_ocenie)

# d)
data_oceny_poprawa = {
    'Nr_albumu': [1, 2, 3],
    'Ocena_poprawa': [5.0, 4.5, 4.0]
}

df_poprawa = pd.DataFrame(data_oceny_poprawa)
df_polaczone = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')
print("\nDane połączone z protokołem ocen z poprawy:")
print(df_polaczone)

# e)
df_polaczone.to_csv('studenci.csv', index=False)

# f)
df_wczytane = pd.read_csv('studenci.csv')
print("\nDane wczytane z pliku CSV:")
print(df_wczytane)

# g)
nowy_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imię': ['Piotr'],
    'Nazwisko': ['Adamski'],
    'Ocena': [4.2],
    'Wiek': [22]
})

df_polaczone = pd.concat([df_polaczone, nowy_student], ignore_index=True)
print("\nDane po dodaniu nowego studenta:")
print(df_polaczone)

# h)
unikalne_oceny = df_polaczone['Ocena'].unique()
print("\nUnikalne wartości w kolumnie 'Ocena':")
print(unikalne_oceny)

# i)
liczba_studentow_z_5 = df_polaczone[df_polaczone['Ocena'] == 5].shape[0]
print("\nLiczba studentów z oceną 5:", liczba_studentow_z_5)
