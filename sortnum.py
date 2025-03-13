# #or .sort
# a = [1, 5, 7, 4, 9]
# a.sort()  
# print(a)

# #or .sort(key=lambda)
# a = [1, 5, 7, 4, 9]
# a.sort(key=lambda x:x)  
# print(a)

# n = 10
# for i in range(n, -1, -1):
#   print(i)

##----------------------------------------------------------------------------
# i/p "20 10 154" o/p "2 1 145"

num = input("enter num: ").split()
empty_string = " "
for i in num:
  isort  = "".join(sorted(i))
  # print(isort)
  empty_string += isort+" "
  # print(isort)
  # if isort !=i:
  #   rule = False
  #   break

print(empty_string)