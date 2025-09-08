import pytest
from Ejercicio2 import consola

def test_cargar():
    assert consola ("cargar") == "Cargando archivo..."
def test_guardar_comando():
    assert consola("guardar") == "Guardando archivo..."
def test_salir():
    assert consola("salir") == "Saliendo del programa..."
def test_prueba():
    assert consola(" ") or consola(1) or consola("a") == "Comando no reconocido."