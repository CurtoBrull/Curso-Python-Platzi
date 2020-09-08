# def es_primo(numero):
#   contador = 0
#   if numero != 2 and numero % 2 == 0:
#     return False
#   for i in range(1, numero + 1): # Recordar que el range le quita 1
#     if i == 1 or i == numero:
#       continue
#     if numero % i == 0:
#       contador += 1
#   if contador == 0:
#     return True  
#   else:
#     return False


def es_primo(numero):
  if numero > 1: # Entra al ciclo si es >1 si no devuelve False
    contador = 0 # Si el contador da 0 devolverá true
    i = 2 # Iniciamos el ciclo en 2 ya que el 1 no es primo.

    # i debe ser menor que el número introducido y el contador debe ser 0 para mantenerse en el ciclo.
    while i < numero and contador == 0: 
      
      # Calculamos el resto de numero dividido por i. Si el resto da 0 sumamos al contador mientras sea menor a i.
      resto = numero % i
      if resto == 0:
        contador += 1
      # Sumamos 1 al ciclo para evitar un bucle infinto
      i += 1
    # En el momento que el contador se reinicie a 0 ya tenemos el numero primo.
    if contador == 0:
      return True 
    else:
      return False
  else:
    return False # Si introducimos un numero igual o menor a 1 no es primo.

def rango_primos(numero2):
  for numero2 in range(1, numero2):
    if numero2 > 1:
      contador = 0
      i = 2

      while i < numero2 and contador == 0:
        resto = numero2 % i

        if resto == 0:
          contador += 1
        i += 1
      if contador == 0:
        print(numero2, end=' ')

def run():
  numero = int(input('Introduce un número: '))
  if es_primo(numero):
    print('El número {} es primo'.format(numero))
  else:
    print('El número {} no es primo'.format(numero))
  numero2 = int(input('Introduce otro número: '))
  if rango_primos(numero2):
    print()
  else:
    print()


if __name__ == "__main__":
    run()