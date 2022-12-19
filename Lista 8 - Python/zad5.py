imie = input("Podaj imię: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = 2022 - rok_urodzenia

if wiek >= 18:
    print(f"{imie}, masz {wiek} lat, jesteś pełnoletni")
else:
    print(f"{imie}, masz {wiek} lat, jesteś niepełnoletni")

