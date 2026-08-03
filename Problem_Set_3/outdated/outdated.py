#Guardamos la lista que nos da el problema
meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        fecha = input("Date: ").strip()
        #Camino 1: El formato es 9/8/1632
        if "/" in fecha:
            #Dividimos el texto en 3 elementos
            m, d, a = fecha.split("/")
            #Convertimos todo a numeros
            mes = int(m)
            dia = int(d)
            anio = int(a)
            #Validamos que los dias y meses tengan sentido
            if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                continue
            #Imprimimos el formato ISO YYYY-MM-dD
            print(f"{anio:04}-{mes:02}-{dia:02}")
            break
        #Camino 2: El formato es September 8, 1992
        elif "," in fecha:
            #Separamos el dia y el mes del anio, esta vez con comas
            mes_dia, anio_str = fecha.split(",")
            anio_str = anio_str.strip()
            #Separamos el mes del dia
            mes_str, dia_str = mes_dia.split(" ")
            mes_str = mes_str.title()
            #Comprobamos que el mes este en la lista de meses
            if mes_str in meses:
                #Buscamos la posicion y sumamos 1 pues las listas empiezan por 0
                mes = meses.index(mes_str) + 1
                dia = int(dia_str)
                anio = int(anio_str)
                #Validamos el dia otra vez
                if 1 <= dia <= 31:
                    print(f"{anio:04}-{mes:02}-{dia:02}")
                    break
    except ValueError:
        #Si algo falla ignoramos el error con pass
        pass
    except EOFError:
        print()
        break
