#Ejercicio 1
calificaciones = [70, 85, 90, 65]

#Agregar un elemento al final
calificaciones.append(95)
#Agregar un elemento entre dos elementos
calificaciones.insert(2, 80)


#Ejercicio 2
colores = ["Azul", "Amarillo", "Rosa"]

#Agregar elementos a un arreglo ya definido
colores.extend(["Verde", "Morado", "Rojo", "Negro"])


#Ejercicio 3
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])


posicion95 = numeros.index(95)
posicion67 = numeros.index(67)
print("Posición del número 95:",posicion95)
print("Posición del número 67:",posicion67)