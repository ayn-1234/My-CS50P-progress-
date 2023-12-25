def main(greet):
    greet = greet.strip().lower()

    if "hello" in greet:
        print("$0")

    elif greet.startswith("h"):
        print("$20")

    else:
        print("$100")


answer = input("Greeting: ")
main(answer)

# completed assingment
# Alhamdulliah
