import pytest
from Ejercicio7 import combinar_listas, generar_reporte


def test_combinar_listas_basico():
    nombres = ["Ana", "Luis", "Carlos"]
    notas = [4.5, 3.8, 5.0]
    resultado = combinar_listas(nombres, notas)
    assert resultado == {"Ana": 4.5, "Luis": 3.8, "Carlos": 5.0}


def test_combinar_listas_longitudes_diferentes():
    # zip solo une hasta la menor longitud
    nombres = ["Ana", "Luis"]
    notas = [4.5, 3.8, 5.0]
    resultado = combinar_listas(nombres, notas)
    assert resultado == {"Ana": 4.5, "Luis": 3.8}


def test_generar_reporte_basico():
    estudiantes = {"Ana": 4.5, "Luis": 3.8}
    reporte = generar_reporte(estudiantes)
    assert "El estudiante Ana tiene una nota de 4.5" in reporte
    assert "El estudiante Luis tiene una nota de 3.8" in reporte


def test_generar_reporte_diccionario_vacio():
    estudiantes = {}
    reporte = generar_reporte(estudiantes)
    assert reporte == []
