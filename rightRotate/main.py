num = [7, 5, -2, 3, 9 , 0, 6, 10]
len_num = len(num)
temp =num[-1] 
# print(temp)
for i in range(len_num-2, -1, -1):
  # print(i)
  num[i+1] = num[i]
num[0]=temp
print(num)
# num = [7, 5, -2, 3, 9 , 0, 6, 10]
# len_num = len(num)
# temp = num[-1]  # temp = 10

# for i in range(len_num - 2, -1, -1):
#     num[i + 1] = num[i]  # shifting elements to the right

# num[0] = temp  # putting 10 at index 0

# print(num)
