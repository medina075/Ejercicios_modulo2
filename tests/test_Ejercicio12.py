import pytest
from Ejercicio12 import simulador_dados

def test_total_lanzamientos():
    lanzamientos = 1000
    resultados = simulador_dados(lanzamientos)
    # La suma de todas las frecuencias debe ser igual a la cantidad de lanzamientos
    assert sum(resultados.values()) == lanzamientos

def test_rango_sumas():
    resultados = simulador_dados(500)
    # Todas las claves deben estar entre 2 y 12
    for suma in resultados.keys():
        assert 2 <= suma <= 12

def test_no_faltan_claves():
    resultados = simulador_dados(2000)
    # Verifica que aparezcan todas las sumas posibles (2 a 12)
    for suma in range(2, 13):
        assert suma in resultados

def test_distribucion_razonable():
    lanzamientos = 10000
    resultados = simulador_dados(lanzamientos)
    # La suma 7 es la más probable (debe ser mayor que extremos 2 y 12)
    assert resultados[7] > resultados[2]
    assert resultados[7] > resultados[12]
