def Validar_claves(clave: str) -> str:
    """
    Valida una contraseña según los siguientes criterios:
    - Mínimo 8 caracteres.
    - Al menos una letra mayúscula.
    - Al menos un número.

    Parámetros:
        contrasena (str): contraseña a validar.

    Retorna:
        str: "Contraseña válida." si cumple todas las reglas,
             o un mensaje con la primera regla incumplida.
    """
    if len(clave) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not any(c.isupper() for c in clave):
        return "La contraseña debe contener al menos una mayúscula."
    if not any(c.isdigit() for c in clave):
        return "La contraseña debe contener al menos un número."
    return "Contraseña es aceptable."


if __name__ == "__main__":
    intentos=3
    while True:
        pwd = input("Cree una contraseña: ")
        resultado = Validar_claves(pwd)
        print(resultado)
        if resultado == "Contraseña es aceptable.":
            break

    while True:
        confirmar = input("ingrese la clave: ")
        if pwd == confirmar:
            print("La clave correcta es correcta.")
            exit(0)
        else:
            print("La clave es incorrecta.")
            intentos= intentos-1
            print(f"Te quedan {intentos} intentos.")
        if intentos == 0:
            print("Te quedaste sin intentos tu no eres el dueño.")
            exit(0)