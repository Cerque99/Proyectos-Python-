# Pedimos el texto original al usuario
texto = input("Input: ")
#Generamos la palabra vacia para luego llenarla
resultado = ""
#Recorremos el texto letra por letra
for letra in texto:
    #Comprobamos si la letra convertida a minuscula es vocal
    if letra.lower() not in "aeiou":
        #Si no es vocal la concatenamos al resultado
        resultado += letra
#Escribimos la palabra
print(f"Output: {resultado}")
