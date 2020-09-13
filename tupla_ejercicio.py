# "abacabad" c

# {
#   'a': (0,4),
#   'b': (1,2),
#   'c': (3,1)
# }
# "abacabaabacaba" _
# "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
#"bcccccccccccccyb" y

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    # enumerate retorna una tupla que contiene un contador (empieza en 0 por defecto) y los valores iterados. 
    # Guardamos en un diccionario la letra y con los valores en una tupla indicando el índice y las veces que se ha visto el caracter, en este caso al no verse más que una vez el valor es 1
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) # Guardamos en un diccionario la letra y con los valores en una tupla indicando el índice y las veces que se ha visto el caracter, en este caso el segundo valor son las veces vista + 1 ya que se empieza por 0

# Ejemplo:

# "abacabad"
# seen_letters = {
              #   'a': (0,4),
              #   'b': (1,2),
              #   'c': (3,1)
              # }
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__ == "__main__":

    char_sequence = str(input('Introduce secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
      print('Se repiten TODOS los caracteres')
    else:
      print(f'El primer carácter que NO se repite es {result}')
