#Necesitamos installar pyfiglet (pip install pyfiglet)
#Llamamos sys y random tambien
import sys
import random
from pyfiglet import Figlet
#Inicializamos figlet
figlet = Figlet()
#Obtenemos la lista de todas las fuentes validas de la libreria
fuentes_validas = figlet.getFonts()

#Comprobacion de argumentos (sys.argv)
#sys.argv[0] es el nombre del archivo
#Primer output, si el usuario no pasa un elemento extra
if len(sys.argv) == 1:
    fuente_elegida = random.choice(fuentes_validas)
#Si el usuario pasa exactamente 2 elementos
elif len(sys.argv) == 3:
    #Comprobamos que el primer elemento sea correcto (-f o --font)
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        #Comprobamos que el nombre de la fuente existe
        if sys.argv[2] in fuentes_validas:
            fuente_elegida = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
#Si el usuario pone un numero incorrecto de elementos
else:
    sys.exit("Invalid usage")
#Aplicamos la fuente elegida
figlet.setFont(font=fuente_elegida)

texto = input("Input: ")

#Imprimimos el resultado final
print("Output: ")
print(figlet.renderText(texto))
