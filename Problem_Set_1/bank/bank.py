#Pedimos un saludo al usuario
saludo = input("Saludo: ")
#Limpiamos el texto (quitamos espacios y pasamos a minuscula)
saludo = saludo.lower().strip()
#Evaluamos las condiciones
if saludo.startswith("hello"):
    print("$0")
elif saludo.startswith("h"):
    print("$20")
else:
    print("$100")

