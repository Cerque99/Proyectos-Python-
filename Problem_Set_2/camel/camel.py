#Pedimos al usuario la variable cameCase
texto_camel = input("camelCase: ")
#Construimos una variable vacia donde iremos construyendo el texto
texto_snake = ""
#Recorremos el texto introduciendo letra a letra
for letra in texto_camel:
    #Comprobamos si la letra actual esta en mayus
    if letra.isupper():
    #Añadimos un guion bajo y la letra en minuscula
        texto_snake += "_" + letra.lower()
    else:
        texto_snake += letra
#Imprimimos la palabra
print(f"snake_case:{texto_snake}")si
