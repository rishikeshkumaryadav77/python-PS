n = 5
for i in range(n):
  val = i+1
  dec = n-1
  for j in range(i+1):
    print(val, end=' ')
    val += dec
    dec -= 1
  print()