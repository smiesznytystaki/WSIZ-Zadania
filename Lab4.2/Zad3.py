def powitanie(imie="Użytkowniku", jezyk="polski"):
    if jezyk == "polski":
        print(f"Cześć, {imie}")
    elif jezyk == "angielski":
        print(f"Hello, {imie}")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}")
    else:
        print(f"Witaj, {imie}")

powitanie("Ania", "polski")
powitanie("Patryk", "angielski")
powitanie("Krystian", "niemiecki")
powitanie("Janek", "francuski")
powitanie()