# num = [7, 5, -2, 3, 9 , 0, 6, 10]
# len_num = len(num)
# temp =num[-1] 
# # print(temp)
# for i in range(len_num-2, -1, -1):
#   # print(i)
#   num[i+1] = num[i]
# num[0]=temp
# print(num)


# -----------------or
# num[:] =[num[-1]]+num[0:len_num-2]
# print(num)
# rotateright by one element pratice
# num = [7, 5, -2, 3, 9 , 0, 6, 10]
# temp = num[-1]
# for i in range(len(num)-2, -1 , -1):
#   num[i+1] = num[i]
# num[0] = temp
# print(num)

# --------------------right rotate by k element 
num = [7, 5, -2, 3, 9 , 0, 6, 10]
k = 3
num_len = len(num)
rotations = k%num_len
# print(rotations)
for _ in range(0, rotations):
  e = num.pop()
  num.insert(0, e)
print(num)

# or with slicing
# end_num = num[num_len - rotations:]
# start_num = num[0:num_len -rotations]
# print( end_num+start_num)
