import pytest
from Ejercicio1 import entradas

def test_menor_no_estudiante():
    assert entradas(10, "no") == 10000

def test_menor_estudiante():
    assert entradas(10, "si") == 9000

def test_joven_no_estudiante():
    assert entradas(15, "no") == 15000

def test_joven_estudiante():
    assert entradas(15, "si") == 13500

def test_adulto_no_estudiante():
    assert entradas(25, "no") == 20000

def test_adulto_estudiante():
    assert entradas(25, "si") == 18000

def test_edad_invalida():
    with pytest.raises(ValueError, match="La edad no puede ser negativa o igual a 0."):
        entradas(0, "no")

    with pytest.raises(ValueError):
        entradas(-5, "si")

def test_valores_borde():
    # Justo en los límites
    assert entradas(11, "no") == 10000
    assert entradas(12, "no") == 15000
    assert entradas(17, "si") == 13500
    assert entradas(18, "no") == 20000

