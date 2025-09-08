import pytest
from Ejercicio8 import procesar_lista

def test_lista_mixta():
    numeros = [-5, 10, -15, 20, -25, 30]
    positivos, negativos, cuadrados, etiquetas = procesar_lista(numeros)

    assert positivos == [10, 20, 30]
    assert negativos == [-5, -15, -25]
    assert cuadrados == [25, 100, 225, 400, 625, 900]
    assert etiquetas == ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]


def test_solo_positivos():
    numeros = [1, 2, 3, 4]
    positivos, negativos, cuadrados, etiquetas = procesar_lista(numeros)

    assert positivos == [1, 2, 3, 4]
    assert negativos == []
    assert cuadrados == [1, 4, 9, 16]
    assert etiquetas == ["positivo", "positivo", "positivo", "positivo"]


def test_solo_negativos():
    numeros = [-1, -2, -3]
    positivos, negativos, cuadrados, etiquetas = procesar_lista(numeros)

    assert positivos == []
    assert negativos == [-1, -2, -3]
    assert cuadrados == [1, 4, 9]
    assert etiquetas == ["negativo", "negativo", "negativo"]


def test_lista_vacia():
    numeros = []
    positivos, negativos, cuadrados, etiquetas = procesar_lista(numeros)

    assert positivos == []
    assert negativos == []
    assert cuadrados == []
    assert etiquetas == []
