nombre = input('Introduce nombre ')

# Método STRIP, elimina espacios

nombre = nombre.strip()
print(f'{nombre} sin espacios')

# Método UPPER

nombre = nombre.upper()
print(nombre)

# Método Capitalize

nombre = nombre.capitalize()
print(nombre)

# Método Lower

nombre = nombre.lower()
print(nombre)

# Método Replace

nombre = nombre.replace('a', 'o') #Reemplaza todas las letras que introducimos como primer valor y las sustituye por el segundo
print(nombre)

# Índice

letra = nombre[0]
letra = letra.capitalize()
print(letra)

# Length

lenght = len(nombre)
print(lenght)
print(nombre[len(nombre)-1])

# JOIN añade el valor
print(nombre)
print('2'.join(nombre))

str = "-"
seq = ("a", "b", "c")
print(str.join( seq ))
