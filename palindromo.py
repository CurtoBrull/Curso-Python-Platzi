# Palíndromo: palabra o frase que se lee igual al derecho y al revés
# ( Luz azul )

# Primero creamos una funcion principal llamada run o main
def palindromo(palabra):
  palabra = palabra.replace(' ', '') # Reemplazamos todos los espacios por un nada ''
  palabra = palabra.lower()
  # Usamos slice -1 para invertir la palabra
  if palabra == palabra[::-1]:
    return True
  else:
    return False


def run():
  palabra = input('Escribe una palabra: ')
  es_palindromo = palindromo(palabra)
  if es_palindromo == True:
    print('Es palíndromo.')
  else:
    print('No es palíndromo.')


if __name__ == '__main__': # Entry point
  run()