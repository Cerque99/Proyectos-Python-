#Tomamos como referencia fuel.py del Set 3 y definimos la funcion
def main():
    while True:
        fraccion = input("Fraction: ")
        try:
            #Intercambiamos convertir la fraccion
            porcentaje = convert(fraccion)

            #Si tiene exito, sacamos el medidor y rompemos el bucle
            resultado = gauge(porcentaje)
            print(resultado)
            break
        except (ValueError, ZeroDivisionError):
            #Si convert() da estos errores ignoramos y volvemos a preguntar
            pass

def convert(fraccion):
    #Separamos el texto usando la barra
    if "/" not in fraccion:
        raise ValueError

    x_str, y_str = fraccion.split("/")

    x = int(x_str)
    y = int(y_str)

    #Comprobamos las reglas del enunciado
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0 and y > 0 or x > 0 and y < 0:
        raise ValueError

    #Calculamos el porcentaje y redondeamos al entero mas cercano

    return round((x/y) * 100)

def gauge(percentage):
    #Evaluamos los limites para devolver la letra o el numero
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

