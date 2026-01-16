Input = [4, 1, 2, 2, 3, 4, 4, 2]
repeated_number = []

# Step 1: Collect numbers that appear more than once (no duplicates)
for i in Input:
    if Input.count(i) > 1:
        if i not in repeated_number:
            repeated_number += [i]

# Step 2: Sort the repeated_number list (bubble sort style)
for j in range(len(repeated_number)):
    for k in range(0, len(repeated_number)-1):
        if repeated_number[k] > repeated_number[k+1]:
            repeated_number[k], repeated_number[k+1] = repeated_number[k+1], repeated_number[k]

# Step 3: Print the sorted repeated numbers
print(repeated_number)

# Step 4: Print the smallest repeated number
print("Smallest repeated number:", repeated_number[0])