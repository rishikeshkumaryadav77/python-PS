# # Input two numbers without function
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Implement the Euclidean algorithm without a function
# a, b = num1, num2

# while b != 0:
#     a, b = b, a % b

# # `a` now holds the GCD
# print(f"The GCD of {num1} and {num2} is {a}")

####with function
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")