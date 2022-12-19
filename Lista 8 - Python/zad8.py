liczba_punktow = int(input("Podaj liczbę uzyskanych punktów: "))
forma = int(input("Wybierz formę oceny [1 jeśli słownie, 2 jeśli cyfrowo]"))


if liczba_punktow <= 50:
    ocena_cyfrowa = 2
    ocena_slowna = "niedostateczny"
elif liczba_punktow < 60:
    ocena_cyfrowa = 3
    ocena_slowna = "dostateczny"
elif liczba_punktow < 70:
    ocena_cyfrowa = 3.5
    ocena_slowna = "dostateczny plus"
elif liczba_punktow < 80:
    ocena_cyfrowa = 4
    ocena_slowna = "dobry"
elif liczba_punktow < 90:
    ocena_cyfrowa = 4.5
    ocena_slowna = "dobry plus"
elif liczba_punktow < 100:
    ocena_cyfrowa = 5
    ocena_slowna = "bardzo dobry"
else:
    ocena_cyfrowa = 5.5
    ocena_slowna = "celujący"

if forma == 1:
    print(f"Twoja ocena to: {ocena_slowna}")
else:
    print(f"Twoja ocena to: {ocena_cyfrowa}")