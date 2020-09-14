
pares = []

for num in range(1, 31):
  if num % 2 == 0:
    pares.append(num)
print(pares)

# List comprehension => creamos la función dentro de la lista
# ['output expression' for 'variable' in 'input sequence' 'optional predicate']
even = [num for num in range(1 ,31) if num % 2 == 0]
print(even)

cuadrados = {}

for num in range(1, 11):
    cuadrados[num] = num**2
print(cuadrados)

# Dictionary comprhension => Declaramos la llave antes de los : y el valor después
square = {num: num**2 for num in range(1, 11)}
print(square)