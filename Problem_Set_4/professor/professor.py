import random


def main():
    #Obetemos el nivel
    nivel = get_level()
    puntuacion = 0

    #Generamos 10 problemas
    for _ in range(10):
        x = generate_integer(nivel)
        y = generate_integer(nivel)
        respuesta_correcta = x + y
        intentos = 0

        #Damos 3 oportunidades por problema
        while intentos < 3:
            try:
                #El formato que pide Hardvard
                respuesta_usuario = int(input(f"{x} + {y} = "))

                if respuesta_usuario == respuesta_correcta:
                    puntuacion += 1
                    break #Acerto, rompemos el bucle de intentos
                else:
                    print("EEE")
                    intentos += 1
            except ValueError:
                #Si introduce letras, tambien cuenta como fallo
                print("EEE")
                intentos += 1
            if intentos == 3:
                print(f"{x} + {y} = {respuesta_correcta}")
        #Imprimimos la puntuacion final
        print(f"Score: {puntuacion}")



def get_level():
    #Bucle infinito hasta que el usuario introduzca 1, 2 o 3
    while True:
        try:
            nivel = int(input("Level: "))
            if nivel in [1, 2, 3]:
                return nivel
        except ValueError:
            pass


def generate_integer(level):
    #Validamos que el nivel sea correcto, sino damos error
    if level not in [1, 2, 3]:
        raise ValueError

    #El nivel 1 va de 0 a 9
    #El nivel 2 va de 10 a 99
    #El nivel 3 va de 100 a 999
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
