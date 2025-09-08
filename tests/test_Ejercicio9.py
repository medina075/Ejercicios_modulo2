import pytest
from Ejercicio9 import iva  # cambia EjercicioIVA por el nombre real de tu archivo


def test_calculo_basico():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]
    resultado = iva(productos)
    assert resultado == {
        "Camisa": 59500.00,   # 50000 * 1.19
        "Pantalón": 95200.00  # 80000 * 1.19
    }


def test_precio_cero():
    productos = [{"nombre": "Gorra", "precio": 0}]
    resultado = iva(productos)
    assert resultado == {"Gorra": 0.00}


def test_precio_decimal():
    productos = [{"nombre": "Café", "precio": 1234.56}]
    resultado = iva(productos)
    assert resultado == {"Café": round(1234.56 * 1.19, 2)}


def test_lista_vacia():
    productos = []
    resultado = iva(productos)
    assert resultado == {}
