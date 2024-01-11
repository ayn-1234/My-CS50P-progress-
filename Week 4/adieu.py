import inflect
import sys


def main():
    names_list = []
    Inflect = inflect.engine()

    while True:
        try:
            Name = input("Name: ")
            if Name == "Liesl":
                names_list.append("to " + Name)
            else:
                names_list.append(Name)

        except EOFError:
            formatted_names = Inflect.join(names_list)
            print()
            print(f"Adieu, adieu, {formatted_names}")
            sys.exit()


main()

#Completed assingments
#Alhamdulliah
