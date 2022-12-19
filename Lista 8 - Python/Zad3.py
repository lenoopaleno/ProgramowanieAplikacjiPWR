pi = 3.1415
promien = int(input("Podaj promien swojego okregu: "))
if promien < 0:
    print("Promien nie moze byc ujemny")
else:
    pole = pi * (promien**2)
    obwod = 2 * pi * promien
    print(f"Pole: {pole}, Obwod: {obwod}")

