liczba = 273
strzal = 0
while(strzal != liczba):
    strzal = int(input("Jakiej liczby szukasz: "))
    if strzal < liczba:
        print("Szukana liczba jest większa")
    else: print("Szukana liczba jest mniejsza")
print(f"Udało Ci się znaleźć liczbę, jest ona równa {liczba}")