#Realizamos los tests
import pytest
from Problem_Set_5.test_fuel.fuel import convert, gauge

def test_convert_fracciones_validas():
    #Comprobamos divisiones basicas
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_errores():
    #Comprobamos que lance ZeroDivisionError si Y es 0
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    #Comprobamos que lance ValueError si X es mayor que Y
    with pytest.raises(ValueError):
        convert("5/4")

    #Comprobamos que lance ValueError si no son numeros
    with pytest.raises(ValueError):
        convert("tres/cuatro")

    #Comprobamos que lance ValueError si son numeros negativos
    with pytest.raises(ValueError):
        convert("-3/4")


def test_gauge():

    #Comprobamos el tanque vacio (1% o menos)
    assert gauge(0) == "E"
    assert gauge(1) == "E"

    #Comprobamos tanque lleno (99% o 100%)
    assert gauge(99) == "F"
    assert gauge(100) == "F"

    #Comprobamos porcentajes normales
    assert gauge(75) == "75%"
    assert gauge(40) == "40%"
