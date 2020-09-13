# Las tuplas son inmutables, no se pueden añadir o quitar elementos
mi_tupla = (1, 2, 3, 4, 5)
print(type(mi_tupla))

# Para declarar una tupla y no un entero

mi_tupla2 = (1)
print(type(mi_tupla2)) # No indica que es un int

mi_tupla3 = (1,) # La "," al final aunque no siga nada indica que es una tupla
print(type(mi_tupla3))