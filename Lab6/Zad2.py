import matplotlib.pyplot as plt

categories = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Sport']
sales = [120, 80, 150, 60, 90]

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink', 'purple'])

plt.title('Procentowy udział różnych kategorii w całkowitej sprzedaży', fontsize=14)

plt.tight_layout()
plt.show()