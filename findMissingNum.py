# find missing numbers
num = [8,0,1]

max_num = max(num)
# print(max_num)

for i in range(max_num+1):
  
  if i not in num:
    num.append(i)

num.sort()
print(num)

