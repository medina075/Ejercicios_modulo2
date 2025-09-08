import pytest
from Ejercicio3 import Validar_claves

def test_cant_caracteres():
    assert Validar_claves ("1234567") == "La contraseña debe tener al menos 8 caracteres."
def test_una_mayuscula():
    assert Validar_claves("ejemplo123") == "La contraseña debe contener al menos una mayúscula."
def test_un_numero():
    assert Validar_claves("Ejemplooo") == "La contraseña debe contener al menos un número."
def test_valida():
    assert Validar_claves("Ejemplo123") == "Contraseña es aceptable."

