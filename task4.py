tup=[("Ali",30),("Hassan",20),("Mohamoud",29),("Omar",25),("Ahmad",23)]
def sorting_tup(tup):
    result = sorted(tup)
    print(result)
print(sorting_tup(tup))


def sort_dict(data,key):
    return sorted(data , key= lambda x:x[key])
data = [ { 'name' : "alice" , 'age' : 24} ,
        { 'name' : 'ahmed' , 'age' : 20} ,
         { 'name' : "motaaz" , 'age' : 30}
]
print(sort_dict(data,"name"))
print(sort_dict(data,"age"))

tup=[("Ali",30),("Hassan",20),("Mohamoud",29),("Omar",25),("Ahmad",23)]
def sort_tup_to_dict(tup_):
    for k in tup_:
        return sorted({k: v for k,v in tup_}) # sort (big to small (Ahmad to Omar)\\ ['Ahmad', 'Ali', 'Hassan', 'Mohamoud', 'Omar']
        #return sorted({k: v for k,v in tup_}, reverse=True) # sort use (reverse=True) small to big (Omar to Ahmad)\\ ['Omar', 'Mohamoud', 'Hassan', 'Ali', 'Ahmad']
  
print(sort_tup_to_dict(tup))




 