# perfect number
# ex--6--> 1,2,3,6(but exculde the 6)add remaing num if equla to 6 then its perfect number
n = 8
sum = 0
for i in range(1, n):
  if n%i == 0:
    sum +=i
    print(sum)
if sum ==n:
  print("Given num is perfect number")
else:
  print("Not a perfect nmber")
