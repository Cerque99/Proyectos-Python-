#Para este programa instalamos la libreria inflect
import inflect
#Incializamos el motor
p = inflect.engine()
#Creamos una lista para guardar los nombres
nombres = []

while True:
    try:
        #Pedimos nombre al usuario
        nombre = input("Name: ")
        nombres.append(nombre)
    except EOFError:
        #Cuando el usuario presiona Ctrl + D, imprimimos salto de linea
        print()
        break
#Fuera de bucle le pasamos nuestra lista de nombres a inflect
#Usamos el .join() que pone las comas y los "and" perfectamente
lista_final = p.join(nombres)
#Imprimimos los nombres
print(f"Adieu, adieu, to {lista_final}")
