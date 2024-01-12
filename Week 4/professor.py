import random


def main():
    Level = get_level()
    score = 0

    for i in range(10):
        a = generate_integer(Level)
        b = generate_integer(Level)
        real_answer = a + b
        attempts = 3
        while True:
            user_answer = int(input(f"{a} + {b} = "))
            if user_answer == real_answer:
                if attempts > 0:
                    score += 1
                    break

            else:
                attempts -= 1
                if attempts == 0:
                    print(f"{a} + {b} = {real_answer}")
                    break
                print("EEE")




    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isdigit() and 1 <= int(level) <= 3:
                return int(level)
            else:
                raise ValueError

        except ValueError:
            pass




def generate_integer(level):
    while True:

            if level in [1, 2,3] :
                if level == 1:
                    return random.randint(0, 9)
                elif level == 2:
                    return random.randint(10, 99)
                else:
                    return random.randint(100, 999)



if __name__ == "__main__":
    main()
