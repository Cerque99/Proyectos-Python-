#Pedimos el input al usuario
respuesta = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
#Limpiamos el texto
respuesta = respuesta.strip().lower()
#Evaluamos la respuesta para ver si coincide con alguna de las válidas
if respuesta == "42" or respuesta == "forty two" or respuesta == "forty-two":
    print("Yes")
else:
    print("No")
