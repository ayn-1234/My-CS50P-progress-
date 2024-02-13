from fpdf import FPDF
from PIL import Image

class Shirt_generetor(FPDF):
    def __init__(self):
        self.fdf = FPDF()

    def header(self, header):
        self.fdf.add_page()
        self.fdf.set_margin(0)
        self.fdf.set_font("helvetica", "", 50)
        self.fdf.set_xy(0, 40)
        self.fdf.cell(200, 10, header, 0, align='C' )


    def shirt(self, name):
        shirt_image= Image.open("shirtificate.png")
        width, height = shirt_image.size
        mm_per_pixel = 25.4 / 96
        width_mm = width * mm_per_pixel
        height_mm = height * mm_per_pixel
        x = (210 - width_mm) / 2
        y = (297 - height_mm) / 2
        self.fdf.image('shirtificate.png', x=x, y=y, w=width_mm, h=height_mm)
        self.fdf.set_text_color(255, 255, 255)
        self.fdf.set_font_size(20)
        self.fdf.text(x=67, y=140, text=f"{name} took CS50")

    def generate_shirt(self, name):
        self.fdf.output(name + ".pdf")


def main():
    shirtificate = Shirt_generetor()
    shirtificate.header("CS50 Shirtificate")
    shirtificate.shirt(input("Name: "))
    shirtificate.generate_shirt("shirtificate")


if __name__ == "__main__":
    main()

#Alhamdulliah
#Completed Assingment
