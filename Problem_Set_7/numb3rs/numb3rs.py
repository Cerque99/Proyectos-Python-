import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #Buscamos el patron exacto: "num.num.num.num
    #El ^ y el $ aseguran que no haya texto antes ni despues de la IP
    coincidencia = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

    #Si el formato es correcto extraemos los cuatro numeros
    if coincidencia:
        #Extraemos los grupos capturados por los parentesis
        a, b, c, d = coincidencia.groups()

        #Comprobamos que ningun bloque tenga 0 a la izquierda
        if str(int(a)) <= a and str(int(b)) <= b and str(int(c)) <= c and str(int(d)) <= d:

            #Comprobamso que no se pasen de 255
            if int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255:
                return True

    #Si falla el regex o los numeros son muy altos , es invalida
    return False

if __name__ == "__main__":
    main()
