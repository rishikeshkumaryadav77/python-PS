##ascii  A-Z(65-90)
##       a-z(97-122)
##       0-9(48-57)

##chr(65)-->code to character <=> print(chr(65))
##ord(A)-->charater to code   <=> print(ord('A'))

##=--------------
# n = 5
# char = 65
# for i in range(n):
#   for j in range(i+1):
#     print(chr(char+i), end=' ')
#   print()

##output
# A 
# B B
# C C C
# D D D D
# E E E E E

##------------------
# n = 5
# char = 65
# k = 0
# for i in range(n):
#   for j in range(i+1):
#     print(chr(char+k), end=' ')
#     k += 1
#   print()

##output
# A 
# B C
# D E F
# G H I J
# K L M N O

##--------------------
# n = 5
# char = 65
# for i in range(n):
#   for j in range(i+1):
#     if i % 2==0:
#       print(chr(char), end=' ')
#     else:
#       print(chr(char+1), end=' ')
    
#   print()

##output
# A         
# B B
# A A A
# B B B B
# A A A A A

##--------------------
n = 5

for i in range(n):
  char = 65
  for j in range(i+1):
      print(chr(char), end=' ')
      char +=1
  print()
##ouput
# A 
# A B
# A B C
# A B C D
# A B C D E