import random
import sys


def main():
    while True:
        Level = input("Level: ")

        if Level.isdigit() and int(Level) > 0:
            Level = int(Level)
            n = random.randint(1, Level)

            while True:
                guess = input("Guess: ")
                if guess.isdigit():
                    guess = int(guess)

                    if guess > n:
                        print("Too Large!")

                    elif guess < n:
                        print("Too small!")

                    else:
                        sys.exit("Just right!")


main()

#Completed assingment
#Alhamdulliah
