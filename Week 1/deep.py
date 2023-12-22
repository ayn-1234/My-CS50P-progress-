answer = input("implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower().strip()



if (answer == "42" ):
    print("Yes")
elif (answer == "forty-two"):
    print("Yes")
elif (answer == "forty two"):
    print("Yes")
else:
    print("No")
