import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))
max_element = matrix.max()
min_element = matrix.min()
max_in_rows = matrix.max(axis=1)
max_in_columns = matrix.max(axis=0)
row_sums = matrix.sum(axis=1)

print("Macierz:")
print(matrix)
print("\nNajwiększy element:", max_element)
print("Najmniejszy element:", min_element)
print("\nNajwiększe elementy w wierszach:", max_in_rows)
print("Największe elementy w kolumnach:", max_in_columns)
print("\nSuma wartości w wierszach:", row_sums)
