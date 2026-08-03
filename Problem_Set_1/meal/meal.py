def main():
    #Pedimos la hora al usuario
    hora_texto = input("Time? ")
    #Llamamos a convert para transformar el texto en un decimal puro
    hora_numerica = convert(hora_texto)
    #Evaluamos los rangos para cada comida
    if 7.0 <= hora_numerica <= 8.0:
        print("Breakfast time")
    if 12.0 <= hora_numerica <= 13.0:
        print("Lunch time")
    if 18.0 <= hora_numerica <= 19.0:
        print("Dinner time")
def convert(time):
    #Separamos las horas de los minutos usando puntos
    horas, minutos = time.split(":")
    #Convertimos a float y calculamos la proporcion en minutos
    resultado = float(horas) + (float(minutos)/60)

    #Devolvemos el resultado
    return resultado


if __name__ == "__main__":
    main()
