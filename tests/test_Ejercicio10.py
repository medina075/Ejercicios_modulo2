import pytest
from Ejercicio10 import transponer_matriz_for, transponer_matriz_comprehension

def test_transpuesta_basica():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_cuadrada():
    matriz = [[1, 2], [3, 4]]
    esperado = [[1, 3], [2, 4]]
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_una_fila():
    matriz = [[1, 2, 3, 4]]
    esperado = [[1], [2], [3], [4]]
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_una_columna():
    matriz = [[1], [2], [3]]
    esperado = [[1, 2, 3]]
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_vacia():
    matriz = [[]]
    esperado = []
    assert transponer_matriz_for(matriz) == esperado
    assert transponer_matriz_comprehension(matriz) == esperado
