def faces(text):
    face = text.replace(":)" , "🙂").replace(":(" , "🙁")
    return face


text = input("text: ")
text = faces(text)
print(text)

#completed assingment
