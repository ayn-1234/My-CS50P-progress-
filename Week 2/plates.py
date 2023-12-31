def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        for chars in s[:-1]:
            if not chars.isalpha() and not chars.isdigit():
                return False
            if chars == "0":
                return False
        return True


    else:
        return False




main()
# Alhamdulliah
