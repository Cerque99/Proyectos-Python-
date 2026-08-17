import sys
import csv

def main():
    #Comprobamos la cantidad exacta de argumentos
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]

        #Lista para almacenar datos ya formateados
        datos_limpios = []

        #Intentamos leer el archivo de entrada
        try:
             with open(archivo_entrada, "r") as entrada:
                  #DictReader lee la primera linea como cabecera
                  lector = csv.DictReader(entrada)

                  for fila in lector:
                       #fila["name"] contiene algo como "Abbott, Hannah"
                       #Usamos split para romperlo en 2 variables
                       apellido, nombre = fila["name"].split(", ")

                       #Añadimos a nuestra lista un diccionario con la nueva estructura
                       datos_limpios.append({
                            "first": nombre,
                            "last": apellido,
                            "house": fila["house"]
                       })
        except FileNotFoundError:
             #Si el archivo no existe, abortamos con el mensaje de error
             sys.exit(f"Could not read {archivo_entrada}")

        #Escribimos el archivo de salida
        #newline="" es una buena practica en Python para evitar saltos de linea
        with open(archivo_salida, "w", newline="") as salida:
             #Definimos las columnas en el orden precisado
             columnas = ["first", "last", "house"]

             #DictWriter se encarga de formatearlo todo a CSV
             escritor = csv.DictWriter(salida, fieldnames=columnas)

             #Escribimos la primera fila (cabeceras)
             escritor.writeheader()

             #Escribimos el resto de los datos fila por fila
             for alumno in datos_limpios:
                  escritor.writerow(alumno)
if __name__ == "__main__":
     main()

