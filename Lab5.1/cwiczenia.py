import f_mat

from f_mat import kwadrat, szescian, dodaj

print("Import całego modułu:")
print(f"Kwadrat liczby 10: {f_mat.kwadrat(10)}")
print(f"Sześcian liczby 3: {f_mat.szescian(3)}")
print(f"Suma liczb 10 i 5: {f_mat.dodaj(10, 5)}")

print("\nImport wybranych funkcji:")
print(f"Kwadrat liczby 10: {kwadrat(10)}")
print(f"Sześcian liczby 3: {szescian(3)}")
print(f"Suma liczb 10 i 5: {dodaj(10, 5)}")