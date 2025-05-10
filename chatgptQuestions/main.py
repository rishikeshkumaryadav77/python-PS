# 1. Reverse a String
# Problem:
# Write a function that reverses a string.
# Example:
# Input: "hello" → Output: "olleh"
# Concept: String slicing or iteration.

# string = 'hello'
# # reversed_string = string[::-1]  # Using slicing
# # print(reversed_string)
# reverse = ''
# for i in string:
#   reverse = i + reverse   # Using second vaiable
# print(reverse)


# 2. Palindrome Check
# Problem:
# Check if a given string is a palindrome (reads the same backward).
# Example:
# Input: "racecar" → Output: True
# Concept: Compare string with its reverse.

# string = "raceca"
# reversed_string = string[::-1]  # Using slicing
# print(reversed_string == string)

# 4. Sum of Digits
# Problem:
# Find the sum of digits in a number.
# Example:
# Input: 1234 → Output: 10
# Concept: Loop and modulus.

# num = 1234
# num_str = str(num)
# # print(num_str)
# sum_num = 0
# for i in num_str:
#   sum_num += int(i)
# print((sum_num))

# 5. Count Vowels in a String
# Problem:
# Count how many vowels are in a string.
# Example:
# Input: "hello world" → Output: 3
# Concept: Loops and membership check (in).

# str = "hello world"
# vowels = "aeiou"
# count = 0
# for i in str:
#   if i in vowels:
#     count += 1
# print(count)

# 6. Find Maximum in List
# Problem:
# Find the largest number in a list.
# Example:
# Input: [1, 5, 2, 9] → Output: 9
# Concept: Loop or use Python's max().

# list_num = [1, 5, 2, 9]
# temp = list_num[0]
# # print(temp)
# for i in list_num:
#   if i > temp:
#     temp = i
# print(temp)


# 7. Even or Odd
# Problem:
# Check if a number is even or odd.
# Concept: Use modulo (% 2).

# 8. Remove Duplicates from List
# Problem:
# Remove duplicates from a list and return the new list.
# Example:
# Input: [1, 2, 2, 3] → Output: [1, 2, 3]
# Concept: Use set() or loop.

num_list = [1, 2, 2, 3]

# print(set(num_list))
# set_num= list(set(num_list))
# print(set_num)

# temp = []

# for i in num_list:
#   if i not in temp:
#     temp.append(i)
# print(temp)


# 9. Factorial
# Problem:
# Calculate the factorial of a number.
# Example:
# Input: 5 → Output: 120
# Concept: Loop or recursion.


# num = 5
# fact_num = 1
# for i in range(1, num + 1):
#    fact_num*= i
# print(fact_num)

# by using functions

def factorial(n):
  if n <=1:
    return 1
  return n * factorial(n - 1)

num = 5
result = factorial(num)
print(result)


# Example 1:

# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
# Example 2:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
# Output: [0,2]
# Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
# Example 3:

# Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
# Output: []
# Explanation: "z" does not occur in any of the words. Hence, we return an empty array.



