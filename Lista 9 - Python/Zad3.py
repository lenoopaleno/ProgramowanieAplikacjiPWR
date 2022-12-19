x = int(input("Podaj mniejszą wartość: "))
y = int(input("Podaj większą wartość: "))
suma = 0

for i in range(x,y+1):
    suma += i
    print(suma)
    print(i)
print(f"Suma liczb z przediału od {x} do {y} równa się: {suma}")