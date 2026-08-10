def main():
    palabra = input("Input: ")
    resultado = shorten(palabra)
    print(f"Output: {resultado}")

def shorten(word):
    #Shorten se encarga de quitar vocales
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    texto_sin_vocales = ""

    for letra in word:
        if letra not in vocales:
            texto_sin_vocales += letra

    return texto_sin_vocales

if __name__ == "__main__":
    main()
