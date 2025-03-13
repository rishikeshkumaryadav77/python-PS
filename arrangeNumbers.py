##---araange number like negative,positive,zero i/p(-8,1,2,3,4,0,-5) o/p(-8, -5, 1, 2, 3, 4, 0)

num = input("enter num: ").split(" ,")
negativeNum = []
positiveNum = []
zeroNum = []
for i in num:
  # print(type(i))
  if i<'0':
    negativeNum += [i] 
  elif i>'0':
    positiveNum += [i]
  else:
    zeroNum += [i]
res = negativeNum + positiveNum + zeroNum
# print(* res)
print(" ,".join(res))