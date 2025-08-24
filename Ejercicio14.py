import random ,getpass


def modo_juego():

    palabras = ["python", "ahorcado", "programacion", "juego", "algoritmo", "computadora"]
    while True:
      opcion = input("Seleccione el modo de juego de acuerdo al numero: \n 1. El computador elige \n 2. Alguien elije la palabra \n")
      if opcion == "1":
        return random.choice(palabras)
        break
      elif opcion == "2":
        palabra = getpass.getpass("Escriba la palabra secreta: ")
        palabras=palabra
        return palabras



def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()


def validar_entrada(letra, letras_intentadas):
    if len(letra) != 1 or not letra.isalpha():
        print("⚠️ Debes ingresar una sola letra.")
        return False
    if letra in letras_intentadas:
        print("⚠️ Ya intentaste esa letra.")
        return False
    return True


def juego_ahorcado():
    palabra = modo_juego()
    letras_adivinadas = set()
    letras_intentadas = set()
    vidas = 6

    print("Bienvenido al juego del Ahorcado")
    print(f"La palabra tiene {len(palabra)} letras.")

    while vidas > 0:
        print("\nPalabra:", mostrar_tablero(palabra, letras_adivinadas))
        print("Letras intentadas:", " ".join(sorted(letras_intentadas)))
        print(f"❤️ Vidas restantes: {vidas}")

        letra = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra, letras_intentadas):
            continue

        letras_intentadas.add(letra)

        if letra in palabra:
            print(f"Bien La letra '{letra}' está en la palabra.")
            letras_adivinadas.add(letra)
            # Verificar si ya ganó
            if all(l in letras_adivinadas for l in palabra):
                print("\nAdivinaste la palabra:", palabra)
                return
        else:
            print(f"Error La letra '{letra}' no está en la palabra.")
            vidas -= 1

    print("\nTe quedaste sin vidas. La palabra era:", palabra)


if __name__ == "__main__":
    juego_ahorcado()
