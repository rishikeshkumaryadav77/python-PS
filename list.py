a = ["green", "red", "green","green", "green", "black", "red", "black", "blue"]
b = []
for i in a:
  num = a.count(i)
  c = num // 2
  b.append("shock" + str(c) )
print(b)

    