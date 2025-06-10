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
# arr = [1, 2, 3, 4, 5, 6]
# arr.insert(0, 0)            # Insert 0 at the beginning
# arr[3] = "Hi"               # Replace 3 with "Hi"
# arr[4] = "Bye"              # Replace 4 with "Bye"
# arr[5] = "Dom"              # Replace 5 with "Dom"

# print(arr)

##second largest number with method i/p [1,13,4,5,5,9] o/p [5,5]

# num = [1, 3, 4, 5, 5, 9]
# num.sort(reverse=True)
# num.pop(0)
# secondLargest_num = [num[0]]
# for i in num:
#   if i in secondLargest_num:
#     secondLargest_num.append(i)
# # print(arr)
# secondLargest_num.pop()
# print(secondLargest_num)


##with methods  i/p [1,13,4,5,5,9] o/p [5,5]
# num = [1, 3, 4, 5, 5, 9]
# larNum= num[0]
# max= []
# min=[]
# for i in num:
#   if i >= larNum:
#     max.append(i)
#   else:
#     min.append(i)
# print(min)

# num2=num[::-1]
# num2.pop(0)
# print(num2)

##without method  i/p [1,13,4,5,5,9] o/p [5,5]

## i/n [ 2, 9,8,4,3] o/p [8]

num = [2, 9,8,4,3, 1, 10]


for i in range(0,len(num)):
  for j in range(i,len(num)):
    if num[i] > num[j]:
      temp = num[i]
      num[i] = num[j]
      num[j] = temp
    # elif num[i]:
      # temp = num[i]
print(num[-2])  # Output: 8