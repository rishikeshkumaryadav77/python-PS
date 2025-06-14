#i/p [3,45,5,6,10,19, 8, 7,19]  o/p[19,19]

a = [3,45,5,6,10,19, 8, 7,19, 20, 20, 30, 30]
unique = list(set(a))
for i in range(0, len(unique)):
    for j in range(0, len(unique)-1):
        if unique[j]>unique[j+1]:
            unique[j], unique[j+1] = unique[j+1], unique[j]
second_lar = [unique[-2]]
for k in unique:
    if k in second_lar:
        second_lar.append(k)
print(second_lar)