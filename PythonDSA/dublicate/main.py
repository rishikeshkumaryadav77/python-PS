def dublicates(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      print("j loop", i, j)
      if i != j and numbers[i] == numbers[j]:
        print("if condition",i, j)
        return True
  return False



number = dublicates([10, 20, 30, 40, 50, 50])

if number:
  print("dublicate exits")
else:
  print("No Dublicates")