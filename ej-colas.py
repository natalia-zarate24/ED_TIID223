from collections import deque

#Crear la cola (fila de personas)
cola = deque(["Ana","Carlos"])

cola.append("Jorge")
cola.append("Andres")
print("Cola actual:", cola)

atendido = cola.popleft()
print("Se atendio a: {atendido}")
print("Cola restante:", cola)

atendido = cola.popleft()
print("Se atendio a: {atendido}")
print("Cola restante:", cola)