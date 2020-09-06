nombre = 'Javier'

# Slice colocamos entre [:] primero donde se inicia el corte y donde se termina. Si queremos empezar desde el caracter 0 se puede obviar [:4]
print(nombre[0:4])
print(nombre[4:])

# Si colocamos 3 números indicamos con el tercero la cantidad de pasos que quiero dar hasta que finalmente se llegue al segundo número.
# Javier [0:5:2] Desde el caracter 0 hasta el 5 dando saltos de 2 en 2
# J(0) a(1) v(2) i(3) e(4) r(5). Guarda el 0, el 2 y el 4

print(nombre[0:5:2])
print(nombre[0:5:3]) # Guarda el 0 y el 3

# En este caso especial le indicamos que queremos recorrer todo el texto pero empezando desde el final.
print(nombre[::-1])
