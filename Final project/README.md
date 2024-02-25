# CS50 ID MANAGER
#### Video Demo:  [Video Demo](https://youtu.be/EJIkcgb9UsU)
#### Description:
CS50 ID MANAGER is a application which is a id management program. Which can do certain tasks such as:
1. Creating a ID based on Valid Name, Email, Date of birth and Course,
2. Viewing all IDs,
3. Searching specific IDs with name,
4. Editing ID,
5. Deleting ID,
6. Uploading a ***CSV*** file with valid IDS and fieldnames which will be added to the database,
7. view Options and
8. exit

`All of the IDS are saved in a CSV database so the IDS can be stored in a long term way.`

#### Installation:
***Libraries required to installed for this program are:***
1. Pytest: Pytests are for my testing in ***test_project.py***. To install the Pytest module you need to paste it in the terminal:
Use [pip](https://pip.pypa.io/en/stable/) to install the package `pytest`:
```
$ pip install pytest
```
2. Tabulate:
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate`:
```
$ pip install tabulate
```
3. Use [pip](https://pip.pypa.io/en/stable/) to install the package `validator-collection`:
```
$ pip install validator-collection
```
4. Use [pip](https://pip.pypa.io/en/stable/) to install the package `validator`
```
$ pip install validators
```
#### Usage:
Use `python` to run the ***project.py***:
```
$ python project.py
```
After you run you will see:
```
╒═════════╤═══════════════════════════════════════════════════╕
│ Option  │ Description                                       │
╞═════════╪═══════════════════════════════════════════════════╡
│ create  │ Create a New ID                                   │
├─────────┼───────────────────────────────────────────────────┤
│ edit    │ edit an ID                                        │
├─────────┼───────────────────────────────────────────────────┤
│ delete  │ Delete an ID                                      │
├─────────┼───────────────────────────────────────────────────┤
│ search  │ Search specific ID with the Name                  │
├─────────┼───────────────────────────────────────────────────┤
│ view    │ View All IDs                                      │
├─────────┼───────────────────────────────────────────────────┤
│ upload  │ Upload a CSV File                                 │
├─────────┼───────────────────────────────────────────────────┤
│ V       │ View Options                                      │
├─────────┼───────────────────────────────────────────────────┤
│ exit    │ Exit                                              │
╘═════════╧═══════════════════════════════════════════════════|
What command do you want:
```
>Write the necessary commands in the "What command do you want: "  as according to the options given and `enjoy` the program.

And finally to `test` the program you have to use `pytest`:
```
$ pytest test_project.py
```
> Thank you for reading this far <3

