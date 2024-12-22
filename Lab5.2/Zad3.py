import pandas as pd

file_path = 'demografia.csv'
df = pd.read_csv(file_path)

df.replace('.', pd.NA, inplace=True)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

max_przyrost = df.iloc[:, 1:].max().max()
rok_max_przyrost = df.iloc[:, 1:].max().idxmax()
kraj_max_przyrost = df.loc[df[rok_max_przyrost] == max_przyrost, 'KRAJE'].iloc[0]

print(f"Największy przyrost ludności: {max_przyrost}")
print(f"Rok: {rok_max_przyrost}")
print(f"Kraj: {kraj_max_przyrost}")