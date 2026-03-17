arr = [5, 7, 11, 20, 24, 30, 45]
sumOfTwo = []
for i in arr:
  for j in arr:
    if(i+j == 41):
      sumOfTwo += [[i,j]]
print(sumOfTwo)