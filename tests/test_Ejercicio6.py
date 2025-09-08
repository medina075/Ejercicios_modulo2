import pytest
from Ejercicio6 import encontrar_indices


def test_encontrar_indices_basico():
    assert encontrar_indices("hola mundo", "o") == [1, 9]
    assert encontrar_indices("banana", "a") == [1, 3, 5]
    assert encontrar_indices("banana", "b") == [0]


def test_mayusculas_minusculas():
    assert encontrar_indices("Hola Mundo", "h") == [0]
    assert encontrar_indices("Hola Mundo", "H") == [0]
    assert encontrar_indices("AAAaaa", "a") == [0, 1, 2, 3, 4, 5]


def test_caracter_inexistente():
    assert encontrar_indices("python", "z") == []
    assert encontrar_indices("12345", "a") == []


def test_subcadenas():
    assert encontrar_indices("probando", "ro") == [1]
    assert encontrar_indices("banana", "na") == [2, 4]
    assert encontrar_indices("abracadabra", "abra") == [0, 7]


def test_frase_vacia_o_cadena_vacia():
    assert encontrar_indices("", "a") == []
    assert encontrar_indices("texto", "") == []
