import sys

# Vamos a utlizar los dicionarios para cifrar y desfrirar palabras, para ello crearemos un diccionario
# "KEYS" donde pondremos el valor de cada palabra para cunado cifremos el mensaje.
# Después tendremos una funcion principal que sera "def run" y dentro de ella haremos llamar la funciones 
# de cifrar y descifrar dependiedno de lo que queramos hacer y estas dos funciones las desarrollaermos
# por separado con su respectivo bloque de código.

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '&',
}

# Esta es la función en cargada de cifrar el mensaje.
# -Con la variable "words" lo que haremosa será coger la frase guardada en "message" y separarla
# por sus espacios osea por sus palabras, lo haremos a traves de "split".
# -Crearemos la lista vacia "cypher_message[]" donde se irá guardando el resultado que salga del 
# ciclo "for" que se encargara de ver si cada letra de la palabra esta dentro del diccionario "KEYS"
# y poner el valor a que equivale esa letra en el diccionario.

def cypher(message):
  words = message.split(' ')
  cypher_message = []

# Con este ciclo vamos a iterar a lo largo de las palabras, crearemos una variable vacia que será
# "cypher_word".
# El  ciclo "for letter in word" lo que dice es que iterara cada letra de cada palabra, con cada una de 
# esas iteraciones a traves de "KEYS[letter]" lo que estamos diciendo es que de cada letra busque en 
# el diccionario las llaves que tenga el valor de esa letra y a través de "+=" iremos añadiendo ese resultado 
# a la varible vacía "cypher_word". 
# A traves de "append" añadiremos el resultado de "cypher_word" a "cypher_message" y en "return" a través 
# de la funcion "join" juntaremos estas palabras que habíamos separado con "split".

  for word in words:
      cypher_word = ''
      for letter in word:
        cypher_word += KEYS[letter]
      
      cypher_message.append(cypher_word)

  return ' '.join(cypher_message)

# Esta es la función que se encarga de descifrar el codigo cifrado, es lo mismo que la función de 
# cifrar pero del revés, tambien separaremos por palabras a través de "split" y crearemos una lista vacía 
# donde se añadira el resultado del ciclo "for".

def decipher(message):
  words = message.split(' ')
  decipher_message = []

# Creamos nuestra variable vacía "decipher_word" que iremos llenando con los valores del siguiente ciclo
# for, lo que decimos con este ciclo es que por cada palabra de las palabras tendremos una variable 
# vacía, volveremos a iterar ahora por cada letra de la palabra.

# El tercer "for" es más complicado porque ahora no podemos acceder al diccionario a través de su valor 
# tendremos que iterar a lo largo de todas las llaves y si encontramos el valor entonces podremos obtener la 
# llave. Para obtener tanto las llaves "key" como el valor de las llaves "value" utilizaremos "KEYS.items"
# con if lo que decimos es que una si el valores igual a la letra entonces encontramos la letra a la que 
# corresponde añadiremos a través de "+=" en la variable vacía "decipher_word".

# El diccionario consta de llaves y valores, ahora mismo tenemos el valor del diccionario 
# y necesitamos la llave que esquivale a ese valor, si nuestra letra equivale algún valor habremos encontrado 
# la llave junto con la letra a  la que representa y eso lo haremos con la función "items"
# Después solo tenemos que añadirlo a lista vacía "decipher_message" a través de "append" y con "join"
# unir las palabras.

  for word in words:
    decipher_word = ''

    for letter in word:
      
      for key, value in KEYS.items():
        if value == letter:
          decipher_word += key
    decipher_message.append(decipher_word)
  
  return ' '.join(decipher_message)

# Empezamos con la función principal "def run" dentro de ella ejecutaremos un "loop while" que ser infinito 
# por eso lo inicializamos en "True" para que itere hsata que se cumpla lo que queremos 
# Dentro de este "loop while" cremoa una primera variable "command" que sera la encargada de preguntarnos 
# en la consola que funcion queremso ejecutar para asi el codigo ejecutar la de cifrar mensaje o descifrar 
# el mensaje, despues creamos los condiciones para saber que hemos seleccionado y dentro de cada condicional 
# ira su repsectivo codigo que se encargue de ejecutar la funcion que tenga en funcion a lo que queramos 
# conseguir

def run():
  while True:
    command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

# Este condicional se encargar del codigo cuando elegimo cifrar, detro de ella tenemos dos variables 
# -message: que es la variable donde estara guarda el mensaje que hayamos escrito en la consola para cifrar
# -cypher_message: es donde esta guardad la funcion "cypher(message)" que se encargar de cifrar el mensjae 
# por eso la variable con el mensaje guardado esta como parametor de la función

    if command == 'c':
      print('Cifrar')
      message = str(input('Escribe el mensaje: '))
      cypher_message =  cypher(message)
      print(cypher_message)

# En este condiconal haremos lo mismo que en el "if" pero al  contrario, cogeremos el mensaje ya cifrado 
# por la funcion "cypher" y con la nueva funcion "decipher(message) se encargar de descifrar el mensaje cifrado

    elif command == 'd':
      print('Descifrar')
      message = str(input('Escribe el mensaje cifrado: '))
      decipher_message = decipher(message)
      print(decipher_message)

    elif command == 's':
      salir = str(input('Estás seguro ? s / n: ' ))
      if salir == 's':
        sys.exit()
      else:
          run()
      print('salir')
      break

    else:
      print('Comando no encontrado.')

if __name__ == "__main__":
    print('M E N S A J E S  C I F R A D O S')
    run()