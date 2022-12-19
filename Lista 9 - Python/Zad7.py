for i in range(1, 6):
    for j in range(1, 6):
        if j != i:
            for k in range(1, 6):
                if (k != j) and (k != i):
                    print(f"{i}, {j}, {k}")
            