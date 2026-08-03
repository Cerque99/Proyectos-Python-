def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Comprobamos si la longitud de la matricula esta entre 2 y 6
    if len(s) < 2 or len(s) > 6:
        return False
    #Comprobamos que empiece con almenos 2 letras
    if not s[0:2].isalpha():
        return False
    #Comprobamos que no haya espacios ni signos de puntuacion
    if not s.isalnum():
        return False
    #Comprobamos la posicion de los numeros y si hay 0 inicial
    numero_encontrado = False
    for caracter in s:
        if caracter.isdigit():
            if not numero_encontrado and caracter == '0':
                return False
            #Empezamos a contar numeros
            numero_encontrado = True
        else:
        #Si vemos una letra pero ya habiamos visto un numero antes es invalido
            if numero_encontrado:
                return False
    #Si ha superado todas las pruebas anteriores la matricula es valida
    return True



main()
