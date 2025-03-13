# n = 5
# for i in range(1, n+1):
#   print("* " * n)

# or

# for i in range(n):
#   for j in range(n):
#     print("* ", end="")
#   print()

  # output
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *


#-------------------------------triangle pattern
#n = 5
# for i in range(1,n+1):
#   for j in range(i):
#     print("* ", end="")
#   print()

# output
# * 
# * *
# * * *
# * * * *
# * * * * *

#-------------------------------triangle pattern
# n = 5
# for i in range(n):
#   for j in range(n-i):
#     print("* ", end="")
#   print()

# output
# * * * * * 
# * * * *
# * * *
# * *
# *

#----------------------------right sided triangle
# n = 5
# for i in range(1, n+1):
#   print(("  " *(n-i))+" *"*i)

# or
# for i in range(n):
#   for j in range(i, n):
#     print('',end='')
#   for j in range(i+1):
#     print("*", end='')
#   print()


#----------------right sided triangle
# n = 5
# for i in range(n):
#     for j in range(i):  # Print spaces before stars
#         print(" ", end="")
#     for j in range(i, n):  # Print stars
#         print("*", end="")
#     print()

#--------------hill pattern 
# n = 5
# for i in range(n):
#   for j in range(i, n):
#     print(" ", end=" ")
#   for k in range(i+1):
#     print("*", end=" ")
#   for j in range(i):
#     print('*', end=' ')
#   print()

#-----------reverse hill pattern
# n = 5
# for i in range(n):
#   for j in range(i):
#     print(" ", end=" ")
#   for k in range(n-i):
#     print("*", end=" ")
#   for j in range(n-i-1):
#     print('*', end=' ')
#   print()



#------------Diamond Pattern

n = 5
for i in range(n-1):
  for j in range(i, n):
    print(" ", end=" ")
  for k in range(i):
    print("*", end=" ")
  for l in range(i+1):
    print("*", end=" ")
  print()
for i in range(n):
  for j in range(i+1):
    print(" ", end=' ')
  for k in range(i, n-1):
    print("*", end=' ')
  for l in range(i, n-2):
    print("*", end=' ')
  print()