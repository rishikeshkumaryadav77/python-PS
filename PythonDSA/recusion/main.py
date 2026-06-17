def fibbo(n):
    if n <= 1:
        return n
    else:
        return fibbo(n - 1) + fibbo(n - 2)

num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number")
else:
    for i in range(num):
        print(fibbo(i))


# witout recursion

n = 5
a,b = 0,1
for i in range(n):
  print(a)
  c = a+b
  a = b
  b = c
  