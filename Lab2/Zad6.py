x = input("Wprowadz litere: ")

if len(x) != 1:
    print("Wprowadz tylko jedna litere")
else:
    if x.isupper():
        print("Duza")
    elif x.islower():
        print("Mala")
    else:
        print("To nie jest litera")
