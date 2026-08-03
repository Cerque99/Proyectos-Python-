#Pedimos el nombre del archivo al usuario
nombre = input("File name :")
#Limpiamos el input
nombre = nombre.strip().lower()
#Evaluamos la extension
if nombre.endswith(".gif"):
    print("image/gif")
elif nombre.endswith(".jpeg") or nombre.endswith(".jpg"):
    print("image/jpeg")
elif nombre.endswith(".png"):
    print("image/png")
elif nombre.endswith(".pdf"):
    print("application/pdf")
elif nombre.endswith(".txt"):
    print("text/plain")
elif nombre.endswith(".zip"):
    print("application/zip")
else:
    #Si no coincide con ninguna de las anteriores
    print("application/octet-stream")
