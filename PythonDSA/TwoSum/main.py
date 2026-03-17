# arr = [5, 7, 11, 20, 24, 30, 45]
# sumOfTwo = []
# for i in arr:
#   for j in arr:
#     if(i+j == 41):
#       sumOfTwo += [[i,j]]
# print(sumOfTwo)


# [6, 5, 3, 9, 7, 0, 0, 0, 0]
arr = [0, 6, 5, 0, 3,0,9,0,7]
for i in range(0, len(arr)):  
  if arr[i] ==0:
    for j in range(i, len(arr)-1):
      arr[j], arr[j+1] = arr[j+1], arr[j]
      print(arr)
    
    
