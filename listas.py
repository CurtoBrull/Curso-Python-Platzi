# Se crea una lista con una variable y []
print('---Crear lista---')
objetos = [1, 3.4, True, 'Hola']
print(objetos)

# Seleccionar un valor concreto en lista
print('---Seleccionar con el índice---')
mostrar_indice_1 = objetos[1]
print(mostrar_indice_1)

# Meter valores al final de la lista con append
print('---APPEND---')
objetos.append(False)
print(objetos)

# Quitar valores con pop y el índice deseado
print('---POP---')
objetos.pop(3)
print(objetos)

# Ver la lista inversa con [::-1]
print('---Lista inversa---')
print(objetos[::-1])

# Slices en listas
print('---Slices---')
objetos.append(False)
objetos.append('Hola')
objetos.append('Adios')
print(objetos[3:6])

# Recorrer una lista con for
print('---Recorrer con for---')
for elemento in objetos:
  print(elemento)


# Operaciones con listas
print('---SUMAR LISTAS---')
objetos2 = [10, 11, 12]
objeto_final = objetos + objetos2
print(objeto_final)

print('---Multiplicar---')
print(objeto_final*5)
