tup=[("A",1),("B",2),("C",3)] # list of tuple
result={x[0]:x[1] for x in tup} # change list of tuple to dict
print(result)

tup=[("Ali",1),("Hassan",2),("Ziad",3)]
def dict_from_tuple(tup):
    return { k : v for k,v in tup}
print(dict_from_tuple(tup))