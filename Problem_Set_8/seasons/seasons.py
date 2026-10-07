#pip install inflect
from datetime import date
import sys
import inflect

#Inicializamos el motor de la libreira inflect

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")

    #Validamos la fecha
    try:
        birth_date = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    #Obtenemos la fecha de hoy
    today = date.today()

    #Calculamos y mostramos el resultado
    minutes = get_minutes(birth_date, today)
    print(convert_to_words(minutes))

def get_minutes(birth_date, today_date):
    #Al restar dos objetos 'date' obtenemos un 'timedelta'
    delta = today_date - birth_date

    #Extraemos los dias y los convertimos a minutos
    return delta.days * 24 * 60

def convert_to_words(minutes):
    #andword="" elimina la palabra "and" del testo generado
    words = p.number_to_words(minutes, andword="")

    #Capitalizamos la primera letra y engadimos " minutes" al final
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
