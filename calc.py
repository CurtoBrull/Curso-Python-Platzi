def run():
  print('Conversor de Euros a Dólares')
  ammount = float(input('Introduce cantidad de Euros: '))

  result = conversor(ammount)

  print(f'{ammount}€  son {result}$')

def conversor(ammount):
  dolar = 1.65
  return round(dolar * ammount, 2)

if __name__ == "__main__":
    run()