# input = 4
# for row in range(1, input+1):
#   for col in range(1, (input*2)):
#     if (row+col == 5 or col-row==3 or row ==4):
#       print("*", end="")
#     else:
#       print("", end=" ")
#   print()

  # o/p
#    *   
#   * *
#  *   *
# *******


n = int(input("enter num: "))
for row in range(1, n+1):
  for col in range(1, (n*2)):
    if (row+col == (n+1) or col-row== (n-1)):
      print("*", end="")
    elif row ==n:
      if col%2 !=0:
        print("*", end="")
      else:
        print("", end=" ")
    else:
      print("", end=" ")
  print()

  # o/p
#    *   
#   * *
#  *   *
# * * * *