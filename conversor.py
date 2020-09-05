euros = float(input('¿Cuántos Euros tienes? '))
valor_dolar = 0.84
dolares = str(round(euros / valor_dolar, 2))
print(f'Tienes {dolares}$')

dolar = float(input('¿Cuántos Dólares tienes? '))
valor_euro = 1.18
euro = str(round(dolar / valor_euro, 2))
print(f'Tienes {euro}€')