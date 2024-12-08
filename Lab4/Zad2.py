lista = ["Krystian", "Tomek", "Ania", "Marek"]

#a
lista.sort()
print(lista)

#b
lista.append("Piotr")
lista.append("Patryk")
ostatnia_osoba = lista.pop()
print(lista)
print(ostatnia_osoba)

#c
lista.insert(2, "Ewa")
print(lista)

#d
lista.reverse()
lista = lista * 2
print(lista)
