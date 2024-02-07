import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    count = len(ums)
    return count


if __name__ == "__main__":
    main()


#Completed Assingment
#Alhamdulliah
