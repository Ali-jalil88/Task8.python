word = " Hallo "
word1 = 1

def str_word(word_):
   
   try:
     return len(word_)
   except TypeError as e:
     print("this is not Word this Number", e)

str_word(word)# word is String 

str_word(word1) # word1 is number (this is not String  object of type 'int' has no len())

