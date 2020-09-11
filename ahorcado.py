# Definimos la constante con mayúsculas

import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
  'ordenador',
  'telefono',
  'internet',
  'python',
  'toalla',
  'galleta',
  'sabana',
  'edificio',
  'albornoz',
  'teclado',
  'router',
  'azucar',
  'canica'
]


def random_word():
  # Elegir un numero aleatorio para seleccionar el índice desde 0 a la longitud -1
  idx = random.randint(0, len(WORDS) - 1)
  return WORDS[idx]

# Esta funcion imprime la imagen correspondiente al try en el que estemos
def display_board(hidden_word, tries):
  print(IMAGES[tries])
  print('')
  print(hidden_word)
  print('----- * ---------- * ---------- * ---------- * -----')


def run():
  word = random_word()
  # Creamos la palabra escondida multiplicando el símbolo por la longitud de la "word"
  hidden_word = ['_'] * len(word)
  # Los intentos empiezan en 0 y a cada fallo accedemos al indice correspondiente de la lista IMAGES
  tries = 0
  
  while True:
    display_board(hidden_word, tries)
    current_letter = str(input('Escoge una letra: '))

    # Buscamos la letra introducida en el indice y lo almacenamos
    letter_indexes = []
    for idx in range(len(word)):
      if word[idx]== current_letter:
        letter_indexes.append(idx)
    
    # Si no está en el índice sumamos 1 intento
    if len(letter_indexes) == 0:
      tries += 1

      if tries == len(IMAGES) -1:
        display_board(hidden_word, tries)
        print('')
        print(f'Has perdido!!!, La palabra correcta era "{word.capitalize()}"')
        break

      # si está en el índice sustituimos, con la letra introducida, el índice que corresponda 
    else:
      for idx in letter_indexes:
        hidden_word[idx] = current_letter

      # Vaciamos la lista de nuevo para empezar otra vez
      letter_indexes = []
    
    try:
      hidden_word.index('_') # Preguntamos si queda algun símbolo igual en el índice.
      
    except ValueError: # Si lo anterior nos da un error (no quedan símbolos) ejecutamos lo siguiente:
      print('')
      print('FELICIDADES, HAS GANADO!!!')
      print(f'La palabra es: {word.capitalize()}')
      break


if __name__ == "__main__":
    print('')
    print('BIENVENIDOS AL')
    print('A H O R C A D O')
    run()