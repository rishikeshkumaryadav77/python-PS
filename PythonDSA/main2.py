num_a = [5,8,10,11,50,15,20,25,51]
# num_first = num_a[0]
# for i in num_a:
#     if num_first < i:
#         num_first = i
# print(num_first)
for i in num_a:
    for j in num_a:
        if i < j:
            break
        biggest = j
print(biggest)