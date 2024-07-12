dict = [ { 'name' : "alice" , 'age' : 24} ,
        { 'name' : 'ahmed' , 'age' : 20} ,
         { 'name' : "motaaz" , 'age' : 30}
]
def dict_remove(dict_):
    result = [dict_ for dict_ in dict if dict_["age"] !=20] # [{'name': 'alice', 'age': 24}, {'name': 'motaaz', 'age': 30}]
    print(result)
dict_remove(dict)