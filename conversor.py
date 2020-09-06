euros = float(input('¿Cuántos Euros tienes? '))
valor_dolar = 0.84
dolares = str(round(euros / valor_dolar, 2))
print(f'Tienes {dolares}$')

dolar = float(input('¿Cuántos Dólares tienes? '))
valor_euro = 1.18
euro = str(round(dolar / valor_euro, 2))
print(f'Tienes {euro}€')

menu = """
Bienvenido al conversor de monedas 💵

1- Euros
2- Pesos colombianos
3- Pesos argentinos

Elige una opcion: """

option = int(input(menu))

if option == 1:
  euros = float(input('¿Cuántos Euros tienes? '))
  valor_dolar = 0.84
  dolares = str(round(euros / valor_dolar, 2))
  print(f'Tienes {dolares}$')
elif option == 2:
  pesos = float(input('¿Cuántos pesos colombianos tienes? '))
  valor_dolar = 3875
  dolares = str(round(pesos / valor_dolar, 2))
  print(f'Tienes {dolares}$')
elif option == 3:
  pesos_arg = float(input('¿Cuántos pesos argentinos tienes? '))
  valor_dolar = 65
  dolares = str(round(pesos_arg / valor_dolar, 2))
  print(f'Tienes {dolares}$')
else:
  print('Introduce una opción correcta')