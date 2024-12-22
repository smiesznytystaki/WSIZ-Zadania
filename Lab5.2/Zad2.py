import pandas as pd

file_path = 'demografia.csv'
df = pd.read_csv(file_path)

df.replace('.', pd.NA, inplace=True)

df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

kraj_max_przyrost = df['2022'].idxmax()

print(f"Kraj z najwyższym przyrostem ludności w 2022 roku: {df.loc[kraj_max_przyrost, 'KRAJE']}")
