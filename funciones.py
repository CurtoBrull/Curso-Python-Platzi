# def imprimir_mensaje():
#   print('Mensaje especial: ')
#   print('¡Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversation(mensaje):
  print('Hola')
  print('¿Cómo estás?')
  print(mensaje)
  print('Adiós')

option = int(input('Elige una opción (1, 2, 3): '))

if option == 1:
  conversation(f'Elegiste la opción {option}')
elif option == 2:
  conversation(f'Elegiste la opción {option}')  
elif option == 3:
  conversation(f'Elegiste la opción {option}')  
else:
  print('Elige una opción correcta')

# Ejemplo de como guardar un resultado de una función

def suma(a, b):
  print('Se suman dos números')
  resultado = a + b
  return resultado

suma_resultado = suma(5, 7)
print(suma_resultado)