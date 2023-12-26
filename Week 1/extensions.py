def main():
    file = input("File name: ")
    print(media_type(file))


def media_type(exe):
    exe = exe.strip().lower()

    if exe.endswith(".jpg") or exe.endswith(".jpeg"):
        return "image/jpeg"

    elif exe.endswith(".gif"):
        return "image/gif"

    elif exe.endswith(".png"):
        return "image/png"

    elif exe.endswith(".pdf"):
        return "application/pdf"

    elif exe.endswith(".txt"):
        return "text/plain"

    elif exe.endswith(".zip"):
        return "application/zip"

    else:
        return "application/octet-stream"


main()


