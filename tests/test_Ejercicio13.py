import builtins
import pytest
from Ejercicio13 import juego_aventura

def test_ganar_con_carro(monkeypatch, capsys):
    inputs = iter(["1", "1"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    juego_aventura()
    salida = capsys.readouterr().out

    assert "¡Has escapado" in salida or "Ganaste" in salida

def test_perder_en_puerta(monkeypatch, capsys):
    inputs = iter(["2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    try:
        juego_aventura()
    except StopIteration:
        pass  # ya no hay más entradas, pero está bien para el test

    out, _ = capsys.readouterr()
    assert "¡Has perdido!" in out
