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
n = 5873
num_n = n
while num_n > 0:
  last_digit = num_n % 10
  print(last_digit)
  num_n = num_n //10


