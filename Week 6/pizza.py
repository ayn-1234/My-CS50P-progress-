import csv
import sys
import tabulate


def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
            menu = menu_shower(sys.argv[1])
            print(menu)
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Not a CSV file")

    except FileNotFoundError:
        sys.exit("File does not exist")


def menu_shower(file_name):
    menu = []
    with open(file_name) as file:
        reader = csv.reader(file)
        header = next(reader)
        for lines in reader:
            menu.append(lines)
        return tabulate.tabulate(menu, headers=header, tablefmt="grid")

if __name__ == "__main__":
    main()

#Completed Assingments
#Alhamdulliah
