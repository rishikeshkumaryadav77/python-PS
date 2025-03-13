##find num, str, sp witout methods
# a = "10kcoders@gmail.com"
# num = "1234567890"
# alp = "abcdefghijklmnopqrstuvwxyz"
# count_num = 0
# count_alp = 0
# count_sp = 0
# for i in a:
#   if i in num:
#     count_num += 1
#   elif i in alp:
#     count_alp += 1
#   else:
#     count_sp += 1
# print("number", count_num)
# print("alp", count_alp)
# print("sp", count_sp)

# ##or
# input = "10kcoders@gmail.com"
# num,alpha,sp=0,0,0
# for i in input:
#   if i>= "0" and i<= "9":
#     num += 1
#   elif (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
#     alpha += 1
#   else:
#     sp += 1
# print("num", num)
# print("alp", alpha)
# print("sp", sp)


##printing a list vertically in python
# list = [[20, 40, 50], [79, 80], ['hello']]
# temp =[]
# for listmethod in list:
#   for item in listmethod:
#     temp.append(item)

# print(temp)
##or
# nested_list = [[20, 40, 50], [79, 80], ['hello']]
# flat_list = sum(nested_list, [])
# print(flat_list)

# ###
# print("apple"<"ball")

###find largest word in the string
str = "google doc batter".split()
# print(str)
max_str = str[0]
words= []
for i in str:
  if len(i) >= len(max_str):
    words.append(i)

print(words)
