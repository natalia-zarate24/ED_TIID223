#Declarando un arreglo
numeros=[10,20,30,40,50]

print(numeros[2])

#Reasignar valor de la posicion 2 a 15
numeros[2]=15
print(numeros)

#Agregar un valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminar por posicion
numeros.pop(1)
print(numeros)

#Eliminar por valor 
numeros.remove(40)
print(numeros)

#Eliminar por valor
frutas=["Mango","Manzana", "Uva", "Pera", "Maracuya"]
frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("Kiwi")

frutas[2]="Fresa"
print(frutas)

arreglo=[]
n = int(input("Ingresa el tamano del arreglo: "))
n1=int(input("Ingresa el valor 0: "))
arreglo.append(n1)
print(arreglo)