def main():
    fuel = fuelChecker("Fraction: ")
    print(fuel)

def fuelChecker(prompt):
    while True:
        try:
             Input = input(prompt)
             x,y = Input.split("/")
             fraction = round(int(x) / int(y) * 100)

             if fraction <= 1:
                 return "E"
             elif fraction > 100:
                 continue
             elif fraction >= 99:
                 return "F"
             else:
                 return f"{fraction}%"


        except (ValueError, ZeroDivisionError):
            pass

main()
#Completed Assingment
#Alhamdulliah
