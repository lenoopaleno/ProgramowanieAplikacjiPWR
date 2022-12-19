# def Wklejanie():
#     zmienna = input("Podaj wartość: ")
#     if zmienna.isnumeric:
#         zmienna = int(zmienna)
#         suma += zmienna
#         Wklejanie()
#     elif zmienna == 'end':
        
suma = 0
zmienna = 0
while(zmienna != 'end'):
    zmienna = input("Podaj wartość: ")    
    if zmienna.isnumeric:
        zmienna = int(zmienna)
        suma += zmienna
    else:
        print("Podaj wartość cymbale, albo end.")
        break
print(suma)