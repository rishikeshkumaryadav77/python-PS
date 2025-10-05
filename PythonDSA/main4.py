# n = 10
# for i in range(1,n+1):
#   for j in range(1, n+1):
#     if i ==1 or i == n:
#       print("*", end=" ")
#     else:
#       if j ==1 or j==n: 
#         print("*", end = " ")
#       else:
#         print(" ", end=" ")
#   print()
#o/p 
# * * * * * * * * * * 
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *

# ###############
# n = 6
# for i in range(1,n+1):
#   for j in range(n-i):
#     print(" ", end=" ")
#   for k in range(1,n):
#     print("*", end = "")
#   print()
  #o/p
#             *****
#         *****
#       *****
#     *****
#   *****
# *****

# ###############
n = 6
for i in range(n):
  for j in range(i):
    print(" ", end=" ")
  for k in range(1,n):
    print("*", end = "")
  print()
#o/p
# *****
#   *****
#     *****
#       *****
#         *****
#           *****