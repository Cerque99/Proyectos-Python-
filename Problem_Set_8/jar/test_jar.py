import pytest
from jar import Jar

def test_init():
    #Comprobamos la inicializacion correcta
    jar = Jar()
    assert jar.capacity == 12

    jar2 = Jar(5)
    assert jar2.capacity == 5

    #Comprobamos que rechace capacidades invalidas
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("12")

def test_str():
    jar = Jar()
    #Comprobamos el tarro vacio
    assert str(jar) == ""

    #Comprobamos el tarro con galletas
    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    #Comprobamos que salte el error al pasarse de la capacidad
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    jar.withdraw(3)
    assert jar.size == 5

    #Comprobamos que salte el error al intentar sacar mas de lo que hay
    with pytest.raises(ValueError):
        jar.withdraw(6)
