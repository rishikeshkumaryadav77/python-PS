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
##-------------------------------

##check the given password length is greater than 7
a = input()
length = len(a)
#int_len = int(length)
print(length > 7)
##------------------------------

##take input A,B and check B is there in A
a = input()
b = input()
length_a = len(a)
length_b = len(b)
last_string = a[length_a - length_b:]
result = b == last_string
print(result)

##check profit or loss
selling_price = int(input())
buying_price = int(input())
print(selling_price > buying_price)