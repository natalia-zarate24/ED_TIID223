matriz=[
    [1,2,3],
    [4,5,6]
]

print("Mostrar la matriz")
for fila in matriz:
    print(fila)

print("Mostrar el seis")
print(matriz[1][2])

print("Mostrar primera fila")
print(matriz[0])

print("Modificar valor en especifico")
matriz[1][1]=8
print(matriz)

print("Agregar una fila nueva")
matriz.append([7,8,9])
print(matriz)

print("Eliminar un dato")
matriz[0].pop(2)
print(matriz)