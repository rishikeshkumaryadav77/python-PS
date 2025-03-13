num = input("enter num: ").split()
temp = []
first_num = num[0]
# print(first_num)
for i in num:
  # print(i)
  for j in range(0, len(num)):
    if (first_num > num[j]):
      temp += num[j]
      print(temp)

# print(temp)
