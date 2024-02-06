import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if match:
        first_hours = int(match.group(1))
        first_minutes = match.group(2)
        second_hours = int(match.group(4))
        second_minutes = match.group(5)
        first_AM_OR_PM = match.group(3)
        second_AM_OR_PM = match.group(6)

        new_first_minute, new_first_hour = convert_minute(first_hours, first_minutes, first_AM_OR_PM)
        new_second_minute, new_second_hour = convert_minute(second_hours, second_minutes, second_AM_OR_PM)

        return f"{new_first_hour:02}:{new_first_minute:02} to {new_second_hour:02}:{new_second_minute:02}"
    else:
        raise ValueError


def convert_minute(hours, minutes, AM_OR_PM):
    if 1 <= hours <= 12:
        if minutes is not None and 0 <= int(minutes) < 60:
            new_minutes = int(minutes)
            new_hours = hour_converter(hours, AM_OR_PM)
            return new_minutes, new_hours

        elif minutes is None:
            new_minutes = 0
            new_hours = hour_converter(hours, AM_OR_PM)
            return new_minutes, new_hours

        else:
            raise ValueError
    else:
        raise ValueError


def hour_converter(hour, AM_OR_PM):
    if AM_OR_PM == "AM":
        if hour == 12:
            return 0
        else:
            return hour
    else:
        if hour != 12:
            return hour + 12
        else:
            return hour


if __name__ == "__main__":
    main()
  #Completed Assingment
  #Alhamdullaih
