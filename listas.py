# Se crea una lista con una variable y []
print('')
print('---Crear lista---')
print('')

objetos = [1, 3.4, True, 'Hola']
print(objetos)

# Seleccionar un valor concreto en lista
print('')
print('---Seleccionar con el índice---')
print('')

mostrar_indice_1 = objetos[1]
print(mostrar_indice_1)

# Meter valores al final de la lista con append
print('')
print('---APPEND---')
print('')

objetos.append(False)
print(objetos)

# Quitar valores con pop y el índice deseado
print('')
print('---POP---')
print('')

objetos.pop(3)
print(objetos)

# Ver la lista inversa con [::-1]
print('')
print('---Lista inversa---')
print('')

print(objetos[::-1])

# Slices en listas
print('')
print('---Slices---')
print('')

objetos.append(False)
objetos.append('Hola')
objetos.append('Adios')
print(objetos[3:6])

# Recorrer una lista con for
print('')
print('---Recorrer con for---')
print('')

for elemento in objetos:
  print(elemento)


# Operaciones con listas
print('')
print('---SUMAR LISTAS---')
print('')

objetos2 = [10, 11, 12]
objeto_final = objetos + objetos2
print(objeto_final)

print('')
print('---Multiplicar---')
print('')

print(objeto_final*5)


# Modificar un objeto particular de la lista

print('')
print('---MODIFICAR LISTAS---')
print('')
objetos[0] = 'Modificado'
print(objetos)

# Borrar un elemento particular de la lista
print('')
print('---BORRAR OBJETO LISTAS---')
print('')
del objetos[3]
print(objetos)

# Ordenar lista
print('')
print('---ORDENAR OBJETOS LISTAS---')
print('')

objetos3 = [234, 42, 4, 50]
print(objetos3)
objetos3.sort()
print(objetos3)
objetos4 = ['Javier', 'Curto', 'Brull']
objetos4.sort()
print(objetos4)

