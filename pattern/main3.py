list1 = [1,2,3,1,4,5,6,7,5]
list2 = [i for i in range(len(list1)) if list1[i] == 5]
# for i in range(len(list1)):
#   if list1[i] == 5:
#     list2 += [i]
#     print(list2)
print(list2)

# or 
list2 = []
for i in range(len(list1)):
  if list1[i] == 5:
    list2 += [i]
   
print(list2)
