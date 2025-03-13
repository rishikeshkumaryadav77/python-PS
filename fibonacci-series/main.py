##fibonacci series
# num = 5
# a,b=0,1
# for i in range(1, num+1):
#   print(a)
#   c = a+b
  
#   a = b
#   b = c
  
  
##if given number is there print up to that number else print less then given number
# num = 8
# a,b=0,1
# for i in range(1, num+1):
#   if a==num:
#     print("it is a fib num")
#     break
#   if a > num:
#     print("not a fin num")
#   c = a+b

#   a = b
#   b = c

########## if its fib num then do sum else skip(with using function  function)
num  = "526"
fibSum = 0
def sumFib(num):
  a,b=0,1
  while True:
    a,b = b,a+b
    if a == num:
      return True
    if a > num:
      return False
     

for i in num:
  if(sumFib(int(i))):
    fibSum += int(i)
print(fibSum)