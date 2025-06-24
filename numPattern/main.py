#--------------number pattern
# n = 5
# for i in range(1,n+1):
#   for j in range(i):
#     print(j+1, end=" ")
#   print()
#------------------or
# n = 5
# num = ''
# for i in range(1,n+1):
#   num += str(i)+" "
#   print(num)
#--------output
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5




#----------------
# n = 5
# for i in range(n):
#   count = 0
#   for j in range(i+1):
#     print(n-count, end=' ')
#     count += 1
#   print()
#-----   or
# n = 5
# num = ''
# for i in range(n):
#   num += str(n-i)+' '
#   print(num)

#---------output
# 5 
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1



#--------------------
# n =5
# for i in range(n):
#   for j in range(i+1):
#     print(1, end=' ')
#   print()
#--------output
# 1 
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1


#---------------
# n = 5
# for i in range(n):
#   for j in range(i+1):
#     print(i+1, end=' ')
#   print()
#--------ouput
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

#-------------------
# n = 5
# for i in range(n):
#   for j in range(i+1):
#     print(n-i, end=' ')
#   print()
#--------output
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 

#-----------------------
# n = 10
# for i in range(n):
#   for j in range(i+1):
#     if i%2==0:
#       print(1, end=" ")
#     else:
#       print(2, end=" ")
#   print()
#---output
# 1 
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1

#-=---------------
# n = 5
# for i in range(n):
#   for j in range(n-i):
#     print(" ", end=' ')
#   for k in range(i+1):
#     print(i+1, end=' ')
#   for l in range(i):
#     print(i+1, end=' ')
#   print()


# for i in range(1, n):
#   for j in range(i+1):
#     print(" ", end=' ')
#   for k in range(n-i-1):
#     print(n+i, end=' ')
#   for l in range(n-i):
#     print(n+i, end=' ')
#   print()

#----output
  #         1 
  #       2 2 2
  #     3 3 3 3 3
  #   4 4 4 4 4 4 4
  # 5 5 5 5 5 5 5 5 5
  #   6 6 6 6 6 6 6
  #     7 7 7 7 7
  #       8 8 8
  #         9

#-------------------------------
# n = 5
# for i in range(n):
#   count=0
#   for j in range(i+1):
#     print(n-count, end=' ')
#     count+=1
#   print()

#----------output
# 5 
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


#-------------------------------
# n = 5
# k=5
# for i in range(n):
#   p=k
#   for j in range(i):
#     print(' ', end=' ')
  
#   for j in range(i, n):
#     print(p, end=' ')
#     p -= 1
#   k -=1  
#   print()

#-----output
# 5 4 3 2 1 
#   4 3 2 1
#     3 2 1
#       2 1
#         1

#----------------floyd Triangle
# n = 5
# k = 1
# for i in range(n):
#   for j in range(i+1):
#     print(k, end=' ')
#     k += 1
#   print()

#--------output
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



# --------------------
# n = 5
# for i in range(1, n+1):
#   for j in range(1, i+1):
#     print(j,end=" ")
#   print()
  
#---------------- output
# 1   
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# --------------------------
# n = 5
# for i in range(1, n+1):
#   for j in range(1, i+1):
#     print(i+j-1,end=" ")
#   print()

  # =-------o/p
# 1 
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

# ------------------------------------
# n = 5
# for i in range(1, n+1):
#   for j in range(0, i):
#     print(i-j,end=" ")
#   print()
  #-----------------o/p
# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1



# ----------------------------------
# a = 5
# for i in range(1,a+1):
#   for j in range(1,i+1):
#     print(i, end=' ')
#   print()
  
# -----o/p
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

a = 5
for i in range(1,a+1):
  for j in range(1,i+1):
    print(i, end=' ')
  print()