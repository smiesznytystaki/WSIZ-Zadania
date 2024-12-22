import pandas as pd

file_path = 'demografia.csv'

df = pd.read_csv(file_path, na_values=['NA', 'n/a', 'NaN'])

print(df)
