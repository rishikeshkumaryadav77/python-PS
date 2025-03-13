# ------------------------  
# middle row or col: n//2
# major diagonal: i == j
# right diagnol: i==j
# left diagnol: i+j == n-1

#---square Pattern
# def star(n):
#   for i in range(n):
#     for j in range(n):
#       print("*", end=' ')
#     print()
  
# n = 5
# star(n)

#---------output
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#-----square parallel bar pattern
# n = 5
# for i in range(n):
#   for j in range(n):
#     if(j==0 or j==n-1):
#       print('*', end=' ')
#     else:
#       print(' ', end=' ')
  
#   print()

  #-----------ouput
# *       * 
# *       *
# *       *
# *       *
# *       *

#--------square plus star
# n = 5
# for i in range(n):
#   for j in range(n):
#     if(i==n//2 or j==n//2):
#       print("*", end=' ')
#     else:
#       print(' ', end=' ')
#   print()

  # output
#     *     
#     *
# * * * * *
#     *
#     *

#----cross pattern
# n = 5
# for i in range(n):
#   for j in range(n):
#     if(i==j or i+j == n-1):
#       print("*", end=' ')
#     else:
#       print(' ', end=' ')
#   print()

# output
# *       * 
#   *   *
#     *
#   *   *
# *       *

#-----Hallow square pattern
# n = 5
# for i in range(n):
#   for j in range(n):
#     if(i ==0 or i==n-1 or j==0 or j==n-1):
#       print('*', end=' ')
#     else:
#       print(' ', end=' ')
  
#   print()
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *

#---------hallow increasing triangle
# n = 5
# for i in range(n):
#   for j in range(n):
#     if (i==n-1 or j == i or j==0):
#       print("*", end=' ')
#     else:
#       print(' ', end=' ')
#   print()

#output
# *
# * *
# *   *
# *     *
# * * * * *

#---------hallow decreasing triangle
# n = 5
# for i in range(n):
#   for j in range(i,n):
#     if (i==0 or j == i or j==n-1):
#       print("*", end=' ')
#     else:
#       print(' ', end=' ')
#   print()

#output
# * * * * * 
# *     *
# *   *
# * *
# *

#----hollow hill pattern
# n = 5
# for i in range(n):
#   for j in range(n-i):
#     print(' ', end=' ')
#   for j in range(i+1):
#     if (i==0 or j==0 or i==n-1):
#       print("*", end=' ')
#     else:
#       print(" ", end=' ')
#   print()

# for i in range(n):
#   for j in range(n):
#     if (j==0 or i==n-1):
#       print("*", end=' ')
#   print()                #not correct

#