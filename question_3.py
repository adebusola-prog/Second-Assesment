# (3)# -Write a method that takes a word and a text and returns the positions the word is in the text e.g.
#  “pencil” in “The smart boy took a pencil from the shelf has position 6. If the word is not in the text, return 0.

# def positn(word):
#    text="The smart boy took a pencil from the shelf pencil"
#    x = text.strip().split()
#    for index, value in enumerate(x, 1):
#       if word in value:
#          print(f"{word} is on positions {index}")

# positn("pencil")

def positn(word, text):
   x = text.strip().split()
   for index, value in enumerate(x, 1):
      if word in value:
         print(f"{word} is on position {index}")

positn("pencil", "The smart boy took a pencil from the shelf pencil")