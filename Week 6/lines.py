import sys

# This is the main function


def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):

            lines = count_lines(sys.argv[1])
            print(lines)
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Not a Python file")

    except FileNotFoundError:
        sys.exit("File does not exist")

# This function counts lines


def count_lines(file_name):
    count = 0
    with open(file_name) as file:
        for lines in file:
            lines = lines.strip()
            if lines and not lines.startswith("#"):
                count += 1
        return count


if __name__ == "__main__":
    main()
