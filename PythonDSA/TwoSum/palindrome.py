n =1234
num = n
result = 0
while num > 0:
  last = num % 10
  result = (result * 10)+ last
  print(result)
  num = num // 10
print(result)