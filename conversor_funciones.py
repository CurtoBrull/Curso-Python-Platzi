def conversor(tipo_moneda, valor_dolar):
  euros = float(input(f'¿Cuántos {tipo_moneda} tienes? '))
  dolares = str(round(euros / valor_dolar, 2))
  print(f'Tienes {dolares}$')

menu = """
Bienvenido al conversor de monedas 💵

1- Euros
2- Pesos colombianos
3- Pesos argentinos

Elige una opcion: """

option = int(input(menu))

if option == 1:
  conversor('euros', 0.84)
elif option == 2:
  conversor('pesos colombianos', 3875)
elif option == 3:
    conversor('pesos argentinos', 65)
else:
  print('Introduce una opción correcta')