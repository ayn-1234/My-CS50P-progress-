def main():
    date_converter()


def date_converter():
    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")
            if "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                day = int(day)
                year = int(year)

                if month in months_list and 1 <= day <= 31:
                    month_index = months_list.index(month) + 1
                    print(f"{year:04}-{month_index:02}-{day:02}")
                    break
                else:
                    continue

            elif "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= day <= 31 and 1 <= month <= 12:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
                else:
                    continue

            else:
                continue

        except ValueError:
            pass


#completed assingment
#alhamdulliah
main()

