from datetime import date
import re
import sys
import inflect


def main():
    try:
        DOB = input("Date of Birth: ")
        birthday = check_date(DOB)
        current_date = date.today()
        days_passed = count_days(current_date, birthday)
        minutes_passed = count_minutes(days_passed)

        print(minutes_passed)

    except ValueError:
        sys.exit("Invalid format")


def check_date(dob):
    match = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", dob)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        DOB = date(year, month, day)

        return DOB
    else:
        raise ValueError


def count_days(before, after):
    difference = before - after
    return difference.days


def count_minutes(days):
    minutes = round(days * 24 * 60)
    Inflect = inflect.engine()
    word = Inflect.number_to_words(minutes).capitalize().replace(" and ", " ")
    
    return word + " minutes"


if __name__ == "__main__":
    main()
