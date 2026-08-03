def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #Quitamos el simbolo del $ y forzamos que sea decimal
    d = d.replace("$","")
    return float(d)

def percent_to_float(p):
    # Quitamos el simbolo %, lo pasamos a decimal y dividimos entre 100
    p = p.replace("%", "")
    return float(p) / 100


main()
