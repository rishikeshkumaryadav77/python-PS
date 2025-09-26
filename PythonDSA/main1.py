# for i in range(1, 11):
#     print(f"5 * {i} = {5*i}")

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
address = "1.1.1.1"
replace_dot = ""
for i in address:
    if i == ".":
        replace_dot += "[.]"
    else:
        replace_dot += i
print(replace_dot)
