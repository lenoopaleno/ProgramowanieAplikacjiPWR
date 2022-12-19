import time

#czas na zegarze CPU
st = time.process_time()

line =''
for i in range(10):
    line = line + "* "
for i in range(10):
    print(line)


#druga wersja, pewnie taka powinna być

linia =''
for i in range(10):
    linia = linia + "\n"
    for j in range(10):
        linia = linia + "* "
print(linia)

#rónica w czasie na zegarze CPU = czas procesu
et = time.process_time()
print(et-st)