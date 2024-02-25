import sys
import csv
import tabulate
import re
from validators import email as validator


def main():
    print()
    print(display_options())

    while True:
        command = input("What is you command: ").strip().lower()
        if command == "edit":
            id = input("Which id you want to edit?(Name) ")
            dob = input("Input the ID's DOB to confirm? ")
            section = input("Which section of ID you want to edit? ")
            new_value = input("What do you want to replace it with? ")
            edit_id(id, dob, section, new_value)
        elif command == "create":
            create_id()
        elif command == "delete":
            id_name = input("Which ID you want to delete?(Name) ")
            id_dob = input("Input the ID's DOB to confirm? ")
            delete_id(id_name, id_dob)
        elif command == "upload":
            try:
                file = input("Which file you want to Upload (csv only) ")
                upload(file)
            except FileNotFoundError:
                print("File Does not Exist")

        elif command == "view":
            ids = build_id()
            for id in ids:
                print(show_id(id))
        elif command == "exit":
            exit()
        elif command == "v":
            print(display_options())
        elif command == "search":
            id = input("Which ID you want to search?(Name) ")
            ids_found = search(id)
            if type(ids_found) is list:
                for id in ids_found:
                    print(show_id(id))
            elif type(ids_found) is str:
                print(ids_found)

        else:
            print("Invalid Option")


def display_options():
    options = [
        {"Option": "create", "Description": "Create a New ID"},
        {"Option": "edit", "Description": "edit an ID"},
        {"Option": "delete", "Description": "Delete an ID"},
        {"Option": "search", "Description": "Search specific ID with the Name"},
        {"Option": "view", "Description": "View All IDs"},
        {"Option": "upload", "Description": "Upload a CSV File"},
        {"Option": "V", "Description": "View Options"},
        {"Option": "exit", "Description": "Exit"},
    ]
    return tabulate.tabulate(options, headers="keys", tablefmt="fancy_grid")


def create_id():
    while True:
        name = input("Enter name: ").strip().title()
        if re.match(r"^[a-zA-Z\s]+$", name):
            break
        print("Invalid name. Please try again.")

    while True:
        email = input("Enter email: ")
        validate = validator(email)

        if validate == True:
            break
        else:
            print("Invalid email. Please try again.")

    while True:
        dob = input("Enter DOB (YYYY-MM-DD): ")
        if match := re.match(r"^(\d{4})-(\d{2})-(\d{2})$", dob):
            year, month, day = map(int, match.groups())
            if 1 <= month <= 12 and 1 <= day <= 31:
                # Additional checks for month and day validity can be added here
                break
        print("Invalid DOB. Please Try Again")

    while True:
        course = input("Enter course: ").title().strip()
        if re.match(r"^(Python|C\+\+|C#|R|HTML|JS|Java)$", course, re.IGNORECASE):
            break
        print("Invalid course.")

    with open("database.csv", "a") as database:
        writer = csv.DictWriter(database, fieldnames=["name", "email", "dob", "course"])
        writer.writerow({"name": name, "email": email, "dob": dob, "course": course})

    print("ID created successfully!!")


def edit_id(id, dob, key, new_value):

    with open("database.csv") as database:
        flag = False
        reader = csv.DictReader(database)
        data = []
        for row in reader:
            data.append(row)

    with open("database.csv", "w") as new_database:
        writer = csv.DictWriter(
        new_database, fieldnames=["name", "email", "dob", "course"]
        )
        writer.writeheader()
        for row in data:
            if row["name"].lower() == id.lower() and row["dob"].lower() == dob.lower() and key.lower() in row:
                flag = True
                row[key] = new_value
            writer.writerow(row)

    if flag == False:
        print("Invalid information given")
    else:
        print("ID edited successfully!!!")



def show_id(id):
    data = [
        {"CS50 ID": "Name", "": id["name"]},
        {"CS50 ID": "Date of birth", "": id["dob"]},
        {"CS50 ID": "Email", "": id["email"]},
        {"CS50 ID": "Course", "": id["course"]},
    ]
    return tabulate.tabulate(data, headers="keys", tablefmt="fancy_grid")


def build_id():
    with open("database.csv") as database:
        reader = csv.DictReader(database)
        id = [row for row in reader]
        return id


def delete_id(name, dob):
    name = name.title()
    with open("database.csv") as database:
        flag = False
        reader = csv.DictReader(database)
        new_data = []
        for row in reader:
            if not (row["name"] == name and row["dob"] == dob):
                new_data.append(row)
            elif row["name"] == name and row["dob"] == dob:
                flag = True

        if flag == False:
            print("The provided information was not found in the database.")
        elif flag:
            print("ID deleted successfully")

    with open("database.csv", "w") as new_database:
        writer = csv.DictWriter(
            new_database, fieldnames=["name", "email", "dob", "course"]
        )
        writer.writeheader()
        for data in new_data:
            writer.writerow(
                {
                    "name": data["name"],
                    "email": data["email"],
                    "dob": data["dob"],
                    "course": data["course"],
                }
            )


def upload(file):
    if file.endswith(".csv"):
        with open(file) as File:
            reader = csv.DictReader(File)
            if reader.fieldnames == ["name", "email", "dob", "course"]:
                ids = [rows for rows in reader]
                with open("database.csv", "a") as database:
                    writer = csv.DictWriter(
                        database, fieldnames=["name", "email", "dob", "course"]
                    )
                    for id in ids:
                        writer.writerow(
                            {
                                "name": id["name"],
                                "email": id["email"],
                                "dob": id["dob"],
                                "course": id["course"],
                            }
                        )
                    print("ID uploaded successfully")
            else:
                print(f"{file} has invalid fieldnames")

    else:
        print("Only CSV files are allowed")


def search(name):
    name = name.title().strip()
    with open("database.csv") as database:
        reader = csv.DictReader(database)
        ids = []
        for row in reader:
            if row["name"] == name:
                ids.append(row)

        if ids == []:
            return "Invalid ID name given"
        else:
            return ids


def exit():
    sys.exit("This program has been exited successfully!!!")


if __name__ == "__main__":
    main()
