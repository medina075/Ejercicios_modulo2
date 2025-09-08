import pytest
from Ejercicio4 import jugar  # cambia "tu_archivo" por el nombre real del archivo .py


def test_empate():
    assert jugar("piedra", "piedra") == ("piedra", "piedra", "empate")
    assert jugar("papel", "papel") == ("papel", "papel", "empate")
    assert jugar("tijeras", "tijeras") == ("tijeras", "tijeras", "empate")


def test_gana_jugador():
    assert jugar("piedra", "tijeras") == ("piedra", "tijeras", "jugador")
    assert jugar("papel", "piedra") == ("papel", "piedra", "jugador")
    assert jugar("tijeras", "papel") == ("tijeras", "papel", "jugador")


def test_gana_computadora():
    assert jugar("piedra", "papel") == ("piedra", "papel", "computadora")
    assert jugar("papel", "tijeras") == ("papel", "tijeras", "computadora")
    assert jugar("tijeras", "piedra") == ("tijeras", "piedra", "computadora")


def test_opcion_invalida():
    with pytest.raises(ValueError):
        jugar("perro", "pistola")
