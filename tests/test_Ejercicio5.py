import pytest
from Ejercicio5 import clasificar_numero
def test_impar_mult_5():
    assert clasificar_numero(5) == "Impar y múltiplo de 5"
def test_par_mult_5():
    assert clasificar_numero(10) == "Par y múltiplo de 5"
def test_dato_no_valido():
    with pytest.raises(ValueError, match="Debe ingresar un valor válido."):
        clasificar_numero(" ")