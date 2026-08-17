import sys
import os
from PIL import Image, ImageOps

def main():
    #Comprobamos la cantidad exacta de argumentos
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]

        #Comprobar extensiones
        extensiones_validas = [".jpg", ".jpeg", ".png"]

        #Extraemos las extensiones y las forzamos a minusculas
        ext_entrada = os.path.splitext(archivo_entrada)[1].lower()
        ext_salida = os.path.splitext(archivo_salida)[1].lower()

        if ext_salida not in extensiones_validas:
             sys.exit("Invalid output")
        elif ext_entrada not in extensiones_validas:
             sys.exit("Invalid output")
        elif ext_entrada != ext_salida:
             sys.exit("Input and output have different extensions")

        #Procesamos las imagenes
        try:
             #Abrimos la imagen del usuario y la imagen de la camiseta
             imagen_usuario = Image.open(archivo_entrada)
             camiseta = Image.open("shirt.png")

             #Obtenemos el tamaño exacto de la camiseta (ancho y alto)
             tamano_camiseta = camiseta.size

             #Recortamos la imagen del usuario para que tenga las medidas adecuadas
             #ImageOps.fit hace el recorte desde el centro sin deformar la imagen
             imagen_ajustada = ImageOps.fit(imagen_usuario, tamano_camiseta)

             #Pegamos la camiseta encima dela imagen ya recortada
             #Pegamos camiseta dos veces. El segundo actua como una mascara
             #para que el fondo transparente de la camiseta no tape la cara del usuario
             imagen_ajustada.paste(camiseta, camiseta)

             #Guardamos la imagen final
             imagen_ajustada.save(archivo_salida)
        except FileNotFoundError:
             sys.exit("Input does not exist")

if __name__ == "__main__":
    main()

