def main():
    #Pedimos al usuario la frase
    texto_usuario = input()
    #Transformamos el texto
    texto_transformado = convert(texto_usuario)
    #Mostramos el texto en pantalla
    print(texto_transformado)

def convert(texto):
    #Hacemos los reemplazos de las caras por los emojis
    texto = texto.replace(":)","🙂")
    texto = texto.replace(":(","🙁")

#Devolvemos el texto modificado

    return(texto)

#Arrancamos el programa
main()
