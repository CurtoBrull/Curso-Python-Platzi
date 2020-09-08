def run():
  mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
  }
  # Acceder a un valor determinado
  print(mi_diccionario['llave1'])
  print(mi_diccionario['llave2'])
  print(mi_diccionario['llave3'])
  print(mi_diccionario)

  poblacion_paises = {
    'Argentina' : 44938141,
    'Brasil' : 210222333,
    'España' : 43111222 
  }
  # Recorrer con un for solamente las llaves
  for pais in poblacion_paises.keys():
    print(pais)
  # Recorrer con un for solamente los valores
  for pais in poblacion_paises.values():
    print(pais)
  # Recorrer con un for todos los items por lo que tenemos que declarar 2 valores al for
  for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == "__main__":
    run()