import csv
import sys


def main():
    try:
        if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            csv_formatter(sys.argv[1], sys.argv[2])
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Not a CSV file")

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def csv_formatter(before_file, after_file):
    namesAndHouse = []
    with open(before_file) as before:
        reader = csv.DictReader(before)
        for row in reader:
            namesAndHouse.append(row)

    with open(after_file, "w") as after:
        writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for lines in namesAndHouse:
            last, first = lines["name"].split(",")
            first = first.lstrip()
            writer.writerow({"first": first, "last": last, "house": lines["house"]})


if __name__ == "__main__":
    main()

  
#Completed Assingment
#Alhamdulliah
