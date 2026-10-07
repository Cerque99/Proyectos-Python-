from um import count

def test_conteo_basico_y_mayusculas():
    #Comprobamos palabras sueltas y variaciones mayusculas/minusculas
    assert count("um") == 1
    assert count("um um um") == 3
    assert count("Um UM uM um") == 4

def test_subcadenas_trampa():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("Yummy um album") == 1

def test_con_puntuacion():
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Hello, um, world") == 1
    assert count("um...") == 1

