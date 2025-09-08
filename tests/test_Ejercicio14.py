import builtins
import pytest
import Ejercicio14


def test_mostrar_tablero():
    palabra = "python"
    letras_adivinadas = {"p", "o"}
    tablero = Ejercicio14.mostrar_tablero(palabra, letras_adivinadas)
    assert tablero == "p _ _ _ o _"


def test_validar_entrada_valida():
    assert Ejercicio14.validar_entrada("a", set()) is True


def test_validar_entrada_invalida_longitud(capsys):
    assert Ejercicio14.validar_entrada("ab", set()) is False
    salida, _ = capsys.readouterr()
    assert "Debes ingresar una sola letra" in salida


def test_validar_entrada_repetida(capsys):
    assert Ejercicio14.validar_entrada("a", {"a"}) is False
    salida, _ = capsys.readouterr()
    assert "Ya intentaste esa letra" in salida


def test_modo_juego_computador(monkeypatch):
    inputs = iter(["1"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    palabra = Ejercicio14.modo_juego()
    assert isinstance(palabra, str)
    assert len(palabra) > 0


def test_modo_juego_persona(monkeypatch):
    inputs = iter(["2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("getpass.getpass", lambda _: "prueba")
    palabra = Ejercicio14.modo_juego()
    assert palabra == "prueba"
