#Importamos la libreria emoji que debemos instalar previamente (pip install emoji)
import emoji
#Pedimos texto al usuario
texto = input("Input: ")
#Convertimos los codigos a emojis
texto_convertido = emoji.emojize(texto, language='alias')
#Imprimimos el resultado
print(f"Output: {texto_convertido}")
