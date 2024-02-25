from project import display_options, show_id, upload
import tabulate
import pytest


def test_display_options():
    options = [
        {"Option": "edit", "Description": "edit an ID"},
        {"Option": "create", "Description": "Create a New ID"},
        {"Option": "delete", "Description": "Delete an ID"},
        {"Option": "upload", "Description": "Upload a CSV File"},
        {"Option": "view", "Description": "View All IDs"},
        {"Option": "V", "Description": "View Options"},
        {"Option": "search", "Description": "Search specific ID with the Name"},
        {"Option": "exit", "Description": "Exit"},
    ]

    expected_output = tabulate.tabulate(options, headers="keys", tablefmt="fancy_grid")

    assert display_options() == expected_output


def test_show_id():
    id = {
        "name": "Ayan",
        "email": "Ayan@gmail.com",
        "dob": "1999-08-07",
        "course": "Python",
    }
    data = [
        {"CS50 ID": "Name", "": id["name"]},
        {"CS50 ID": "Date of birth", "": id["dob"]},
        {"CS50 ID": "Email", "": id["email"]},
        {"CS50 ID": "Course", "": id["course"]},
    ]
    expected_output = tabulate.tabulate(data, headers="keys", tablefmt="fancy_grid")
    assert show_id(id) == expected_output


def test_upload():
    with pytest.raises(FileNotFoundError):
        upload("Invalid_File.csv")
