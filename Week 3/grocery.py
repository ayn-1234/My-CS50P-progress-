def main():
    listMaker()

def listMaker():
    groceryList = {}

    while True:
        try:
            item = input().lower()

            if item in groceryList:
                groceryList[item] = groceryList.get(item, 0) + 1
            else:
                groceryList[item] = 1

        except EOFError:
            break

    for key in sorted(groceryList):
        print(groceryList[key] , key.upper())




main()

#completed assingment
#alhamdulliah
