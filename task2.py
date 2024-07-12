list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
def common_element(list1,list2):
    return  [element for element in list1 if element in list2]
print(common_element(list1,list2))
