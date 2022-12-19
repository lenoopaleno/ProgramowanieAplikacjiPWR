dzielnik = int(input("Podaj dzielnik: "))

#W zaleności czy chcesz 100 uwzględnić w zbiorze

for i in range(50,101):
    if i % dzielnik == 0:
        print(i)
