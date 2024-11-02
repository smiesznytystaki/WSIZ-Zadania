x1 = 1+2
print(type(x1))
#<class 'int'>

x2 = 1+4.5
print(type(x2))
#<class 'float'>

x3 = 3/2
print(type(x3))
#<class 'float'>

x4 = 4/2
print(type(x4))
#<class 'float'>

x5 = 3//2
print(type(x5))
#<class 'int'>

x6 = -3//2
print(type(x6))
#<class 'int'>

x7 = 11%2
print(type(x7))
#<class 'int'>

x8 = 2**10
print(type(x8))
#<class 'int'>

x9 = 8**(1/3)
print(type(x9))
#<class 'float'>

b1 = int(3.0)
#Instrukcja ta zamienia liczbę zmiennoprzecinkową 3.0 na liczbę całkowitą.
b2 = float(3)
#Instrukcja ta zamienia liczbę całkowitą 3 na liczbę zmiennoprzecinkową.
b3 = float("3")
#Instrukcja ta konwertuje wartość tekstową "3" na liczbę zmiennoprzecinkową.
b4 = str(12.4)
#Instrukcja ta zamienia liczbę zmiennoprzecinkową 12.4 na ciąg znaków.
b5 = bool(0)
#Instrukcja ta sprawdza czy liczba 0 jest prawdą w kontekście logicznym.

print(b1,b2,b3,b4,b5)