from typing import List

def encontrar_indices(frase: str, cadena: str) -> List[int]:
    """
    Encuentra todas las posiciones de una cadena (letra o subcadena) en una frase.

    Parámetros:
        frase (str): Texto donde se buscará.
        cadena (str): Texto a buscar (puede ser una letra o más de un carácter).

    Retorna:
        List[int]: Lista de índices donde aparece la cadena.
    """
    if not cadena:
        return []

    indices: List[int] = []
    longitud = len(cadena)

    for i in range(len(frase) - longitud + 1):
        if frase[i:i+longitud].lower() == cadena.lower():
            indices.append(i)

    return indices


if __name__ == "__main__":
    frase_ingresada: str = input("Ingrese una frase: ")
    cadena_ingresada: str = input("Ingrese una letra o subcadena a buscar: ")
    print(encontrar_indices(frase_ingresada, cadena_ingresada))
