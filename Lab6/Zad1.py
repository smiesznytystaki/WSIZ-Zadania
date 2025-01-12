import matplotlib.pyplot as plt

categories = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Sport']
sales = [120, 80, 150, 60, 90]

plt.figure(figsize=(8, 5))
plt.bar(categories, sales, color='skyblue', edgecolor='black')

plt.title('Ilość sprzedanych produktów w różnych kategoriach')
plt.xlabel('Kategorie')
plt.ylabel('Ilość sprzedanych produktów')

for i, value in enumerate(sales):
    plt.text(i, value + 3, str(value), ha='center',)

plt.tight_layout()
plt.show()
