a = int(input("Podaj pierwszy bok trójkąta: "))
b = int(input("Podaj drugi bok trójkąta: "))
c = int(input("Podaj trzeci bok trójkąta: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Mozna stworzyc taki trojkat")
else:
    print("Nie mozna stworzyc takiego trójkąta")