import sys

def main():
    #Comprobamos la cantidad exacta de argumentos
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    #Comprobamos que el archivo tenga la extension correcta
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    #Intentamos abrir el archivo y procesarlo
    try:
        with open(sys.argv[1], "r") as archivo:
            lineas_codigo = 0

            for linea in archivo:
                #Limpiamos los espacios y saltos de linea a los lados
                linea_limpia = linea.strip()

                #Descartamos lineas vacias y comentarios
                if linea_limpia == "" or linea_limpia.startswith("#"):
                    continue
                #Si sobrevive a los filtros es codigo real
                lineas_codigo += 1
            #Imprimimos el recuento final
            print(lineas_codigo)
    #Capturamos el error si el archivo no existe
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
