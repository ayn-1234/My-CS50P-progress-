def main():
    amount_due()


def amount_due():
    amount_due = 50
    print("Amount Due:", amount_due)
    total = 0

    while total < 50:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            total += coin
            amount_due = 50 -total
            print("Amount Due:", amount_due)

        else:
             print("Amount Due:", amount_due)

        if amount_due <= 0:
            change = total - 50
            print("Change Owed:", change)

main()
#Alhamdulliah



