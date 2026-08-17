import sys
import csv
from tabulate import tabulate

def main():
    #Comprobamos la cantidad exacta de argumentos
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        #Comprobamos que el archivo tenga la extension correcta
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

        #Creamos una lista vacia para guardar los datos y abrimos el archivo
        menu = []
        try:
             with open(sys.argv[1], "r") as archivo:
                  #csv.reader lee el archivo y separa automaticamente los elementos por comas
                  lector = csv.reader(archivo)
                  for fila in lector:
                       menu.append(fila)
        except FileNotFoundError:
             sys.exit("File does not exist")

        #Imprimimos la tabla con el formato que pide Hardvard
        #headers="firstrow" usa la primera linea del CSV como encabezado
        #tablefmt="grid" dibuja los bordes estulo ASCII
        print(tabulate(menu, headers= "firstrow", tablefmt="grid"))

if __name__ == "__main__":
     main()
