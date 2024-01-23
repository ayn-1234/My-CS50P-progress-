import os
from PIL import Image
from PIL import ImageOps
import sys

def main():
    try:
        valid_exe = [".jpeg", ".jpg", ".png"]
        if len(sys.argv) == 3:
            extension1 = os.path.splitext(sys.argv[1])[1].lower()
            extension2 = os.path.splitext(sys.argv[2])[1].lower()
            if extension1 in valid_exe and extension1 == extension2:
                shirt_putter(sys.argv[1], sys.argv[2])
            elif not extension1 in valid_exe:
                sys.exit("Invalid input")
            elif not extension2 in valid_exe:
                sys.exit("Invalid output")
            else:
                sys.exit("Input and output have different extensions")

        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")


    except FileNotFoundError:
        sys.exit("Input does not exist")


def shirt_putter(before, after):
    before_image = Image.open(before)
    shirt = Image.open("shirt.png")
    size = shirt.size
    resized_image = ImageOps.fit(before_image, size=size)
    resized_image.paste(shirt, mask=shirt)
    resized_image.save(after)

if __name__ == "__main__":
    main()
