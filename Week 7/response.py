from validators import email

def main():
    print(email_validator(input("What's your email address? ")))


def email_validator(s):
    validate = email(s)
    if validate == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

#Completed assingment
#Alhamdulliah
