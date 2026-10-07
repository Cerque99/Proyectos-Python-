#pip install validators en la terminal previamente
import validators

def main():
    #Pedimos el correo al usuario
    correo = input("What's your email address? ")

    #validators.email() devuelve True si el formato cumple el estandar
    if validators.email(correo):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
