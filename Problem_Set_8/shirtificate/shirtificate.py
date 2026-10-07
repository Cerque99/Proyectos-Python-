#pip install fpdf2

from fpdf import FPDF

def main():
    #Solicitamos el nombre del usuario
    nombre = input("Name: ")

    #Inicializamos el PDF con orientacion vertical (Portrait) y formato A4
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    #Añadimos el titulo superior
    pdf.set_font("helvetica", "B", 45)
    #width=0 indica que la celda ocupa todo el ancho de la pagina, permitiendo centrar el texto
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")

    #Añadimos la imagen de la camiseta
    #Un A4 mide 210mm de ancho, si le damos a la imagen 190mm de ancho quedan 10mm
    # de margen a cada lado quedando perfectamente centrada
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    #Añadimos el nombre de usuario a la camiseta
    pdf.set_font("helvetica", "B", 25)
    #Configuramos el color del texto en blanco usando valores RGB(255,255,255)
    pdf.set_text_color(255, 255, 255)

    #Bajamos el cursor (coordenada Y) hasta la altura del pecho de la camiseta
    pdf.set_y(140)
    pdf.cell(0, 10, f"{nombre} took CS50", align="C")

    #Generamos el archivo final
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()



