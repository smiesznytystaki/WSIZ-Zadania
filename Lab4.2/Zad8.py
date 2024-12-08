#A
def wyswietl_wartosci(*args):
    for arg in args:
        print(arg)

wyswietl_wartosci(1, 2, 3, 4, 5)
#B
def znajdz_maximum(*args):
    if args:
        return max(args)

print(znajdz_maximum(1, 2, 3, 4, 5))