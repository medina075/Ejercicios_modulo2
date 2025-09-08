def clasificar_numero(numero: int) -> str:
    """
    Clasificacion de numeros pares e inpares y si es múltiplo de 5 sale otro mensaje

    Parámetros:
        numero (int): Número a clasificar.

    Retorna:
        str: Texto indicando si es par o impar y si es múltiplo de 5.
    """
    resultado: str = "Par" if numero % 2 == 0 else "Impar"
    if numero % 5 == 0 and resultado == "Par":
        return "Par y múltiplo de 5"
    elif numero % 5 == 0 and resultado == "Impar":
        return "Impar y múltiplo de 5"
    return resultado


if __name__ == "__main__":
 while True:
    try:
        numero_ingresado: int = int(input("Ingrese un número: "))
        print(clasificar_numero(numero_ingresado))
        break
    except ValueError:
        print("Debe ingresar un valor válido.")
