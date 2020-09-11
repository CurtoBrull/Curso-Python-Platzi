def run():
  mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
  }
  # Acceder a un valor determinado
  print('')
  print(mi_diccionario['llave1'])
  print(mi_diccionario['llave2'])
  print(mi_diccionario['llave3'])
  print('')
  print(mi_diccionario)
  # Añadir al diccionario
  print('')
  print('----AÑADIDO ELEMENTO----')
  mi_diccionario['llave4'] = 4
  print(mi_diccionario)


  poblacion_paises = {
    'Argentina' : 44938141,
    'Brasil' : 210222333,
    'España' : 43111222 
  }
  # Recorrer con un for solamente las llaves
  print('')
  print('----Keys----')
  for pais in poblacion_paises.keys():
    print(pais)
  # Recorrer con un for solamente los valores
  suma_poblacion = 0
  print('')
  print('----Values----')
  for hab in poblacion_paises.values():
    print(hab)
    suma_poblacion += hab
  print('')
  print('Suma de todos los valores: ')
  print(suma_poblacion)
  print('')
  print('Promedio de todos los valores: ')
  print(suma_poblacion // len(poblacion_paises))

  # Recorrer con un for todos los items por lo que tenemos que declarar 2 valores al for
  print('')
  print('----Items----')
  for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == "__main__":
    run()