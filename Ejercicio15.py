# ejercicio15.py
import random


def crear_tablero() -> list[list[str]]:
    """
    Crea un tablero vacío de 5x5 para el juego Batalla Naval.

    Returns:
        list[list[str]]: Una matriz 5x5 llena de "~" representando agua.
    """
    return [["~"] * 5 for _ in range(5)]


def mostrar_tablero(tablero: list[list[str]]) -> None:
    """
    Muestra el tablero en consola con coordenadas de filas y columnas.

    Args:
        tablero (list[list[str]]): Tablero de juego.
    """
    print("  1 2 3 4 5")
    letras = "ABCDE"
    for i, fila in enumerate(tablero):
        print(letras[i], " ".join(fila))


def colocar_barco() -> list[tuple[int, int]]:
    """
    Coloca un barco de 3 casillas de forma horizontal o vertical aleatoria.

    Returns:
        list[tuple[int, int]]: Lista de coordenadas ocupadas por el barco.
    """
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":
        fila = random.randint(0, 4)
        col = random.randint(0, 2)
        return [(fila, col + i) for i in range(3)]
    else:
        fila = random.randint(0, 2)
        col = random.randint(0, 4)
        return [(fila + i, col) for i in range(3)]


def traducir_coordenada(coord: str) -> tuple[int, int] | None:
    """
    Convierte una coordenada en formato 'A3' a índices de fila y columna.

    Args:
        coord (str): Coordenada ingresada por el jugador.

    Returns:
        tuple[int, int] | None: Tupla (fila, columna) si es válida, None si no lo es.
    """
    letras = "ABCDE"
    if len(coord) != 2:
        return None
    fila = coord[0].upper()
    if fila not in letras or not coord[1].isdigit():
        return None
    col = int(coord[1])
    if col < 1 or col > 5:
        return None
    return letras.index(fila), col - 1


def jugar() -> None:
    """
    Ejecuta el juego Batalla Naval Simplificada:
    - El jugador tiene 10 turnos para hundir un barco de 3 casillas.
    - Se muestra el tablero y el estado de los disparos en cada turno.
    """
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 10
    aciertos = 0

    print("=== Batalla Naval 5x5 ===")
    print("Hundí el barco de 3 casillas en máximo 10 turnos.")
    mostrar_tablero(tablero)

    while intentos > 0 and aciertos < 3:
        tiro = input("Ingrese coordenada (ej: A3): ")
        pos = traducir_coordenada(tiro)

        if pos is None:
            print("❌ Entrada inválida. Intente de nuevo.")
            continue

        fila, col = pos
        if tablero[fila][col] != "~":
            print("⚠️ Ya disparaste ahí.")
            continue

        if pos in barco:
            print("🔥 ¡Tocado!")
            tablero[fila][col] = "X"
            aciertos += 1
        else:
            print("🌊 Agua.")
            tablero[fila][col] = "O"

        intentos -= 1
        print(f"Turnos restantes: {intentos}")
        mostrar_tablero(tablero)

    if aciertos == 3:
        print("🎉 ¡Felicidades! Hundiste el barco.")
    else:
        print("💀 Se acabaron los turnos. Perdiste.")
        print("El barco estaba en:", barco)


if __name__ == "__main__":
    jugar()
