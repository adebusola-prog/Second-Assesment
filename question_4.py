# Write a program that takes a word and returns the number of consonants and vowels in that word.
# vow=[]
# con=[]
# word = "adeolaklsjdeteyrndjdlk"
# vowel= "aeiou"
# for i in word:
#    if i in vowel:
#       vow.append(i)
# length_word=len(word)
# length_vow=len(v)
# length_con= length_word - length_vow
# print(f"The word is {word}" )
# print(f"number of vowel(s) is {length_vow}")
# print(f"number of consonant(s) is {length_con}")

def filt_word(word):
   vow=[]
   con=[]
   vowel= "aeiou"
   consonants="bcdfghjklmnpqrstvwxyz"
   for i in word:
      if i in vowel:
         vow.append(i)
      if i in consonants:
         con.append(i)
   print(vow)
   print(con)
   length_con=len(con)
   length_vow=len(vow)
   print(f"The word is {word}" )
   print(f"number of vowel(s) is {length_vow}")
   print(f"number of consonant(s) is {length_con}")

filt_word("adeolaadeyeyeolaoluwa")