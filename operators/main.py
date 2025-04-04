##check the given number is greater or not
a=int(input())
print(a>70)

##-----------------------------------------

##given number is negative or not
a = int(input())
print(a < 0)

##check first and last lettter is same or not
a = input()
first_letter = a[0]
length = len(a)-1
last_letter = a[length:]
result = first_letter != last_letter
print(result)