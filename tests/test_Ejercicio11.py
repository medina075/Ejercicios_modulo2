import pytest
from Ejercicio11 import validar_cedula

def test_cedula_valida_par():
    assert validar_cedula("2468") is True

def test_cedula_invalida_impar():

    assert validar_cedula("123") is True

def test_cedula_invalida_texto():

    assert validar_cedula("12a45") is False

def test_cedula_vacia():

    assert validar_cedula("") is False

def test_cedula_grande():

    assert validar_cedula("1111111") is False
