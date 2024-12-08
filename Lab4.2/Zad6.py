import math

def pole_trojkata():
    try:
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        c = float(input("Podaj długość boku c: "))

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki muszą być większe od zera.")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Podane boki nie tworzą trójkąta.")

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return pole

    except ValueError as e:
        return f"Błąd: {e}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"

print(pole_trojkata())