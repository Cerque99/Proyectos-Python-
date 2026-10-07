from seasons import convert_to_words

def test_convert_to_words():
    #Probamos un año exacto (365 dias  * 24 * 60 = 525600)
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    #Probamos 2 años 1051200 minutos
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
