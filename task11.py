list1 = [1, 2, 3,4,5,6,"ali","hassan"]
list2 = [7,8,9,10,11,12,"ahmad","mahmoud"]
result=list1+list2
print(result) #[1, 2, 3, 4, 5, 6, 'ali', 'hassan', 7, 8, 9, 10, 11, 12, 'ahmad', 'mahmoud']

lis1=["ahmad","mahmoud"]
lis2=["ali","hassan"]
lis1.extend(lis2)
print(lis1) # ['ahmad', 'mahmoud', 'ali', 'hassan']
