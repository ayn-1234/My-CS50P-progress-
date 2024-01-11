import emoji

def main():
    Input = input("Input: ")
    emojize = emoji.emojize(Input, language='alias')
    print(f"Output: {emojize}")

main()
