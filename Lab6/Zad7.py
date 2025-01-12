import numpy as np

matrix = np.zeros((5, 5), dtype=int)
matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

def toggle_values(matrix):
    return np.where(matrix == 0, 1, 0)

toggled_matrix = toggle_values(matrix)

print(matrix)
print(toggled_matrix)
