def run():
  # for contador in range(1000):
  #   if contador % 2 != 0: # Solo numeros pares
  #     continue # Si la condición se cumple el "continue" hace que se salte la línea que le sigue.
  #   print(contador)

  # for i in range(10000):
  #   print(i)
  #   if i == 5678:
  #     break

  texto = input('Escribe un texto: ')
  for letra in texto:
    print(letra)
    if letra == 'o':
      break

if __name__ == "__main__":
  run()