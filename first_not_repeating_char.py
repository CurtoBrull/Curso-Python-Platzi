def first_not_repeating_char(char_sequence): # 3=> Definimos la función a la que hay que introducir un valor
    status_chars = {} # Creamos un diccionario vacío

    for letter in char_sequence: # Recorremos la secuencia escrita
        if status_chars.get(letter) == None: # Si la letra que estamos recorriendo no se encuentra:
            status_chars[letter] = 0 # Introducimos la letra como clave del diccionario y con valor 0

        status_chars[letter] += 1 # Si la letra ya se encuentra sumamos 1 a su valor en el diccionario

    for i,value in enumerate(char_sequence): # Recorremos los valores y con la funcion enumerate contamos
        if status_chars[value] == 1: # si el valor de la llave es 1:
            return value # Devolvemos el valor

    return "_" # Si todos las claves tienen valor repetido




if __name__ == "__main__":
    char_sequence = input('Ingresa una secuencia de caracteres:') # 1=> Ingresamos secuencia caracteres

    result = first_not_repeating_char(char_sequence) # 2 => Guardamos en una variable el resultado de la función.

    if result == "_": # Todas las claves tienen valor repetido
        print ("Todos los caracteres se repiten")
    else: # Devuelve el valor de la clave con valor 1 (no repetida)
        print ("El primer caracter no repetido es: {}".format(result))
