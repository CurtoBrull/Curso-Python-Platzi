import random

numero = int(input('Introduce longitud de la contraseña: '))


def password_generator():
    mays = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
            'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v',
             'w', 'x', 'y', 'z']
    symbols = ['!', '#', '$', '%', '&', '*', '¡', ',', '_', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = mays + minus + symbols + numbers

    password = []

    for i in range(numero):
        # Usamos random + la funcion especial choice
        character_random = random.choice(characters)
        password.append(character_random)

    # Truco para convertir una lista en string
    # '' string vacio .join y el nombre de la lista original
    password = ''.join(password)
    return password


def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)


if __name__ == "__main__":
    run()
