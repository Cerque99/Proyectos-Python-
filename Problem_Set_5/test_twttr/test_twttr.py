#Importamos la funcion que queremos testear
from Problem_Set_5.test_twttr.twttr import shorten

def test_minusculas():
    #Probamos palabras normales
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_mayusculas():
    #Probamos que el programa no ignore mayusculas
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("DAVID") == "DVD"

def test_numeros():
    #Probamos que los numeros queden intactos
    assert shorten("12345") == "12345"
    assert shorten("CS50") == "CS50"

def test_puntuacion():
    assert shorten("!?.,") == "!?.,"
    assert shorten("What's your name?") == "Wht's yr nm?"



