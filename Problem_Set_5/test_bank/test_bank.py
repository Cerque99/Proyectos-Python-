from Problem_Set_5.test_bank.bank import value

def test_hello():
    #Comprobamos que si empieza con hello devuelve 0
    #Sin importar mayusculas o minusculas
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO THERE") == 0

def test_empieza_h():
    #Comprobamos que si empieza con "h" pero no son "hello" devuelve 20
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("How are you doing?") == 20

def test_otro_inicio():
    #Comprobamos que cualquier otra cosa devuelve 100
    assert value("Whats happening?") == 100
    assert value("Good morning") == 100
    assert value("123456") == 100
