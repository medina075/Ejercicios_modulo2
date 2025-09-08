import builtins
import pytest
import Ejercicio14


def test_mostrar_tablero():
    palabra = "python"
    letras_adivinadas = {"p", "o"}
    resultado = Ejercicio14.mostrar_tablero(palabra, letras_adivinadas)
    assert resultado == "p _ _ _ o _"


def test_validar_entrada_valida():
    assert Ejercicio14.validar_entrada("a", set()) is True


def test_validar_entrada_invalida_longitud(capsys):
    assert Ejercicio14.validar_entrada("ab", set()) is False
    salida = capsys.readouterr().out
    assert "⚠️ Debes ingresar una sola letra." in salida


def test_validar_entrada_repetida(capsys):
    assert Ejercicio14.validar_entrada("a", {"a"}) is False
    salida = capsys.readouterr().out
    assert "⚠️ Ya intentaste esa letra." in salida


def test_juego_ahorcado_ganar(monkeypatch, capsys):
    monkeypatch.setattr(Ejercicio14, "modo_juego", lambda: "hola")
    inputs = iter(["h", "o", "l", "a"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    Ejercicio14.juego_ahorcado()
    salida = capsys.readouterr().out
    assert "Adivinaste la palabra: hola" in salida


def test_juego_ahorcado_perder(monkeypatch, capsys):
    monkeypatch.setattr(Ejercicio14, "modo_juego", lambda: "hi")
    inputs = iter(["a", "b", "c", "d", "e", "f"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    Ejercicio14.juego_ahorcado()
    salida = capsys.readouterr().out
    assert "Te quedaste sin vidas" in salida
