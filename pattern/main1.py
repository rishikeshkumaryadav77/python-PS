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


# input = 4
# for row in range(1, input+1):
#   for col in range(1, (input*2)):
#     if (row+col == 5 or col-row==3):
#       print("*", end="")
#     elif row ==4:
#       if col%2 !=0:
#         print("*", end="")
#       else:
#         print("", end=" ")
#     else:
#       print("", end=" ")
#   print()

  # o/p
#    *   
#   * *
#  *   *
# * * * *