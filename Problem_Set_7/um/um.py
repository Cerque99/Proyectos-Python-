import re

def main():
    print(count(input("Text: ")))

def count(s):
    # \b asegura que 'um' este rodeado por espacios o puntuacion, no letras
    #re.IGNORECASE hace que no sea sensible a las mayusculas
    coincidencias = re.findall(r"\bum\b", s, re.IGNORECASE)

    #re.findall devuelta una lista con todas las veces que lo encontro
    #Soo tenemos que devolver la longitud de la lista (len)
    return len(coincidencias)

if __name__ == "__main__":
    main()
