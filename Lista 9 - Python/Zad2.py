y = int(input("Podaj wartość większą od zera: "))
suma = 0

for i in range(y + 1):
    suma += i
print(f"Suma liczb z przediału od 0 do {y} równa się: {suma}")