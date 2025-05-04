# Write a program that prints the numbers from 1 to n. But:
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

##
# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example






# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:
# [1, 3, 2]
if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            my_list.remove(int(command[1]))
        elif command[0] == 'append':
            my_list.append(int(command[1]))
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
