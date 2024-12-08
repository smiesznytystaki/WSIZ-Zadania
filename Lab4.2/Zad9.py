def fibonacci(n):
    if n <= 0:
        return "Podaj liczbę większą niż 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
print(f"Wyraz ciągu Fibonacciego o numerze {n} to {fibonacci(n)}")