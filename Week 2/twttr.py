def main():
    text = input("Input: ")
    print(vowel_remover(text))


def vowel_remover(text):
    new_text =  text
    vowels = ["A", "E", "I", "O", "U", "a" , "e", "i", "o", "u"]
    for chars in vowels:
        new_text = new_text.replace(chars, "")

    return new_text
main()
