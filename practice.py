# num = [int(i) for i in input("enter num: ").split()]
# print(num)
# for i in num:
#   print(i)

##i/p ("i love india") o/p ['i', 'love', 'india']

# text = "i love india"
# word = ""
# words = []
# for i in text:
#   if i != " ":
#     word += i
#   else:
#     words.append(word)
#     word= ""
# if(words):
#   words.append(word)
# print(words)

##  i/p[1,2,3,4,5,6] o/p[0,1,2,'Hi',"Bye", "Dom", 6]
arr = [1, 2, 3, 4, 5, 6]
arr.insert(0, 0)            # Insert 0 at the beginning
arr[3] = "Hi"               # Replace 3 with "Hi"
arr[4] = "Bye"              # Replace 4 with "Bye"
arr[5] = "Dom"              # Replace 5 with "Dom"

print(arr)

