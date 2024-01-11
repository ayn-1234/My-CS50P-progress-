from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()

    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        Input = input("Input: ")
        f = random.choice(fonts)
        figlet.setFont(font=f)
        print(figlet.renderText(Input))

    elif len(sys.argv) == 3 and "-f" in sys.argv or "--font" in sys.argv:

        if not sys.argv[2] in fonts:
            sys.exit("Invalid usage")

        Input = input("Input: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(Input))

    else:
        sys.exit("Invalid usage")


main()


#completed code
#Alhamdulliah
