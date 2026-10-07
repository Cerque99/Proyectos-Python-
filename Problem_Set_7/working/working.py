import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #La expresion regular busco dos bloques identicos separados por " to "
    #([1-9]|1[0-2]) atrapa las horas del 1 al 12
    # (?::([0-5][0-9]))? atrapa opcionalmente los dos puntos y los minutos del 00 al 59
    patron = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"

    coincidencia = re.search(patron, s)

    if not coincidencia:
        #Si el formato esta mal escrito o los minutos pasan de 59, el regex falla
        raise ValueError

    #Extramos los 6 modulos de info
    h1, m1, ampm1, h2, m2, ampm2 = coincidencia.groups()

    #Formateamos ambas horas
    hora_inicio = convertir_a_24h(h1,m1,ampm1)
    hora_fin = convertir_a_24h(h2,m2,ampm2)

    return f"{hora_inicio} to {hora_fin}"

def convertir_a_24h(hora, minuto, ampm):
    hora = int(hora)

    #Logica de conversion AM/PM a reloj de 24 horas
    if ampm == "AM":
        if hora == 12:
            hora = 0
    else:
        if hora != 12:
            hora += 12

    #Si el usuario introdujo "9 AM" en lugar de "9:00 AM", el minuto sera None
    if minuto is None:
        minuto = "00"

    #Formateamos asegurando que la hora siempre tenga 2 digitos
    return f"{hora:02}:{minuto}"

if __name__ == "__main__":
    main()
