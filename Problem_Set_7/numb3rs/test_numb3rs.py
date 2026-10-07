from numb3rs import validate

def test_formato():
    #Comprobamos estructuras incorrectas y texto
    assert validate("1.2.3") == False  #Faltan bloques
    assert validate("1.2.3.4.5") == False  #Sobran bloques
    assert validate("gato.perro.3.3") == False  #Letras en lugar de numeros
    assert validate("1 .2 .3 .4") == False  #Espacios invalidos

def test_rango_correcto():
    #Comprobamos los limites validos
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True


def test_rango_incorrecto():
    #Comprobamos numeros por encima de 255 en distintas posiciones
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("275.3.6.28") == False
