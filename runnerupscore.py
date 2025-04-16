# n = int(input())
# arr = list(map(int, input().split()))

#     # Remove duplicates and sort
# unique_scores = list(set(arr))
# unique_scores.sort(reverse=True)

#     # Print the second highest
# print(unique_scores[1])


# for num in (int, ['4', '5', '6']):
#     print(num)


##
students = []

# Step 1: Read number of students
n = int(input())

# Step 2: Read student data
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# Step 3: Extract grades and find the second lowest
grades = sorted(set([score for name, score in students]))
second_lowest = grades[1]

# Step 4: Filter names with the second lowest grade
second_lowest_students = [name for name, score in students if score == second_lowest]

# Step 5: Sort names alphabetically and print
for name in sorted(second_lowest_students):
    print(name)