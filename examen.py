matriz = [
    [73,12,89,34],
    [5,61,27,94],
    [46,18,80,3]
]

for i in matriz:
    if 80 in i:
        print(f"El 80 esta en la fila {i}")
        break

for fila in matriz:
    for numero in fila:
        if numero == 80:
            print(f"El 80 esta en {fila}")