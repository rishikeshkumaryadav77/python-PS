# Balanced Parentheses
# Write a function to check if a string of parentheses is balanced.
# Input: "(()())"
# Output: true
# Input: "(()()"
# Output: false


def is_balanced_parentheses(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced_parentheses("(()())"))  # True
# print(is_balanced_parentheses("(()"))  