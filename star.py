# n = 5
# for i in range(1, n+2):
#   leftTopStar = ("* "*(n-i) +("    "*(i-1))+ "* "*(n-i))
#   print(leftTopStar)
# for j in range(1,n+1):
#     leftDownStar = "* "*j +("    "*(n-j))+"* "*j
#     print(leftDownStar)


# num = "12345"
# print(num.isdigit())  #true

# words = ['hello', 'world']
# print("-".join(words))  # Output: hello world


# text = "apple,banana,orange"
# print(text.split(","))  # Output: ['apple', 'banana', 'orange']

# arr = [1, 2, 3]
# copy_arr = arr.copy()
# print(copy_arr)  # Output: [1, 2, 3]

#-------------error handling in python
# try:
#     x = 10 / 0  # Division by zero
# except :
#     print("Error: Cannot divide by zero!")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")



try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print(f"Result: {result}")  # Only runs if no exceptions occur