import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    #Buscamos el iframe y capturamos especificamente el ID del video
    coincidencia = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"',s)

    if coincidencia:
        #El grupo 1 contiene exactamente lo que encerramos entre los parentesis
        id_video = coincidencia.group(1)
        return f"https://youtu.be/{id_video}"

    #Si no entcuentra nada o el formato no coincide, devuelve None
    return None

if __name__ == "__main__":
    main()
