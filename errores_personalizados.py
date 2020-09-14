countries = {
  'mexico': 122,
  'colombia': 49,
  'argentina': 43,
  'chile': 18,
  'peru': 31,
}

while True:
  country = str(input('Escribe el nombre de un país: ')).lower() # Lo que introduzcamos se convierte a minúsculas

  try:
    print(f'La población de {country.capitalize()} es: {countries[country]}')
  except KeyError:
    print(f'No tenemos el dato de {country.capitalize()}')
