# print in reverse order
# num = 5873
# str_num = ""
# for i in str(num):
#   str_num = i + str_num
#   # print(str_num) 
# print(int(str_num))    # Output: 3758


# or

# num = 5873
# str_num = str(num)
# len_num = len(str_num)
# # print(len_num)
# for i in range(1,len_num+1):
#   print(str_num[(len_num)-i])  
  
  # print(str_num) 
# print(int(str_num))  #reverse order in new 

# or

# reverse_str= str(num)[::-1]
# for i in reverse_str: 
#     print(int(i))  

#   with % or // operator
# n = 5873
# num_n = n
# while num_n > 0:
#   last_digit = num_n % 10
#   print(last_digit)
#   num_n = num_n //10


#checking lenth with conveting string
# 1st methods

# n= 5438
# num = n
# count = 0
# while num > 0:
#   count += 1
#   num = num//10
# print(count)

# 2nd methods
from math import *
def total_digit(n):
  return int(log10(n)) + 1


n= 5438
result = total_digit(n)
print(result)


