# Los decoradores son funciones que añaden funcionalidades a otras funciones
# Estructura:
# 3 funciones(A, B y C) donde A recibe como parámetro B y devuelve C.
# Los decoradores devuelven otra funcion.

# def funcion_decorador_A (funcion_B):
#   def funcion_interna_C ():
#     codigo de la funcion interna
#   return funcion_interna_C

def funcion_decoradora(funcion_parametro):
  
  # Si se necesitan parámetros incluir *args como parámetro o **kwargs si son clave + valor
  def funcion_interior(*args, **kwargs):
    # Acciones adicionales que agregan funcionalidad
    print('Vamos a calcular')
    funcion_parametro(*args, **kwargs)

    # Acciones adicionales que agregan funcionalidad
    print('Hemos terminado el cálculo')

  return funcion_interior

# Con la @ indicamos que lo siguiente tiene una funcion decoradora
@funcion_decoradora
def suma(num1, num2, num3):
  print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
  print(num1-num2)

@funcion_decoradora
def potencia(base, exponente): 
  print(pow(base, exponente))

suma(7,5,8)

resta(12,10)

# aqui los parámetros tienen clave + valor y necesitamos el uso de **kwargs
potencia(base=5, exponente=3)