word= ["Das wetter hete ist schön","Hallo"]
def word_of_list(word_):
    for v in word_:
        if len(v) > 5 :
            print("List of String is greater than..... ")
        else:
             print("List of String is Smaller than..... ")
word_of_list(word)
result = list[filter(word_of_list,word)]
print(result)
