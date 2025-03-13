# If given number multiple by 3 and 5 then print fizzBuzz
# If given number multiple by only 3 then print Fizz and if num is multiply only with 5 then print Buzz
# else print(num)

num = int(input("enter number: "))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num %3==0:
    print("Fizz")
elif num %5==0:
    print("Bizz")
else:
    print("given {} is not a Fizz and Buzz ".format(num))