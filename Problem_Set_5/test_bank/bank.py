#Hacemos el programa bank.py pero defiendo la funcion
#Tomamos de referencia el archivo del Problem_Set_1
def main():
    #Pedimos el saludo y le pasamos la funcion que crearemos
    saludo = input("Greeting: ")
    resultado = value(saludo)

    #Imprimimos el resultado con el dolar
    print(f"${resultado}")

def value(greeting):
    #Limpiamos los espacios y lo pasamos a minuscula
    saludo_limpio = greeting.lower().strip()

    #Evaluamos las condiciones requeridas
    if saludo_limpio.startswith("hello"):
        return 0
    elif saludo_limpio.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
