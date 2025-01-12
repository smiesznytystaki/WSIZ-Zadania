import matplotlib.pyplot as plt

czas = [0, 1, 2, 3, 4, 5]
predkosc = [0, 10, 20, 15, 25, 30]

plt.figure(figsize=(8, 5))
plt.scatter(czas, predkosc, color='blue')

plt.title('Prędkość chwilowa pojazdu w czasie')
plt.xlabel('Czas (s)')
plt.ylabel('Prędkość (m/s)')

plt.tight_layout()
plt.show()
