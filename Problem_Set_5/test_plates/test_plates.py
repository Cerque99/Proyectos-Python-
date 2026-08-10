from Problem_Set_5.test_plates.plates import is_valid

def test_longitud():
    #Probamos matriculas demasiado cortas o demasiado largas
    assert is_valid("A") == False
    assert is_valid("GOOD") == True
    assert is_valid("OUTATIME") == False

def test_empieza_letras():
    #Comprobamos que empiece con 2 letras
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False
    assert is_valid("55") == False

def test_numeros_medio():
    #Comprobamos que no haya letras despues de los numeros
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_primer_numero_cero():
    #Comprobamos que el primer numero no puede ser 0
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_puntuacion():
    #Probamos que rechace espacios y caracteres especiales
    assert is_valid("PI3.12") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False




