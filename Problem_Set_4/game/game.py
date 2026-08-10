#En este programa solo usaremos random
import random
#Obtenemos el nivel del juego, los numeros iran del 1 al numero introducido
while True:
    try:
        n = int(input("Level: "))
        #El nivel debe ser un entero positivo
        if n > 0:
            break
    except ValueError:
        #Si el usuario escribe texto o simbolos ignoramos el error
        pass
#Generamos el numero entre 1 y n
numero = random.randint(1,n)
#Hacemos el bucle para adivinar el numero
while True:
    try:
        intento = int(input("Guess: "))

        #El intento debe ser un entero positivo tambien
        if intento > 0:
            if intento < numero:
                print("Too small!")
            elif intento > numero:
                print("Too large!")
            else:
                #Si concuerda con el numero random
                print("Just right!")
                break
    except ValueError:
        pass
