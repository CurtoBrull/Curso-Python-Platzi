# La búsqueda binaria es una forma eficiente de buscar un valor dentro de una lista o de una secuencia ordenada.

def binary_search(numbers, number_to_find, low, high): # 4 parámetros explicados abajo.

    if low > high: # si el índice bajo es más alto que el índice alto significa que el número buscado no está en la lista.
      return False
    
    mid = (low + high) // 2 # Para declarar la variable de "mitad" => (índice alto + bajo) /2. En python con // nos da resultado entero (nos dará entero)

    if numbers[mid] == number_to_find: # si el indice en la mitad == al numero buscado hemos encontrado el número
      return mid
      return True
    elif numbers[mid] > number_to_find: # Si el numero en la mitad es mayor al que buscamos
      # Volvemos a ejecutar la busqueda con los siguientes parámetros:
      return binary_search(numbers, number_to_find, low, mid - 1) # el índice alto ya no es el último, ahora es el de la mitad -1.
    else:
      return binary_search(numbers, number_to_find, mid + 1, high) # el índice alto ya no es el último, ahora es el de la mitad +1.


if __name__ == '__main__':
    numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]

    number_to_find = int(input('Ingresa numero: ')) # Número a encontrar

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1) # 4 parámetros, la lista, el numero a buscar, por donde empezar y donde terminar.

    if result is True:
      print(f'El número ha sido encontrado en el índice {mid}')
    else:
      print('El número no está en la lista')

# buscamos el 5
# la lista tiene 14 indice
# mid sera igual a 7 (valor 11)
# Entramos en el caso: mid es mayor al numero buscado 7>5
# volvemos a realizar la busqueda con los parámetros: (lista, 5, 0, mid -1) Ahora vale 7, al recalcular mid = (0+7)/2 = 3 => 3 en la lista es 5
# Entramos en el caso de que numbers[mid "3"] == number_to_find "5" y hemos resuelto la búsqueda
