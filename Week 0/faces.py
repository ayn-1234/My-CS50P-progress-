def faces(text):
    face = text.replace(":)" , "🙂").replace(":(" , "🙁")
    return face


text = input("text: ")
text_to_emoji = faces(text)
print(text_to_emoji)

