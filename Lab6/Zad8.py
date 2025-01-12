import numpy as np

matrix = np.random.randint(0, 51, (5, 5))
greater_than_20 = matrix[matrix > 20]
count_greater_than_20 = greater_than_20.size
mean_value = np.mean(matrix)

print(matrix)
print(f"Liczba elementów większych niż 20: {count_greater_than_20}")
print(f"Średnia dla całej tablicy: {mean_value}")
