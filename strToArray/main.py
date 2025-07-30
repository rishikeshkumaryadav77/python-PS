# string into array without methods
a = "I LOVE MY INDIA"
str_a = ""
list_a = []
for i in a:
    if (i != " "):
        str_a += i
    else:
        list_a = list_a + [str_a]
        str_a = ""
if(str_a):
    list_a += [str_a]
print(list_a)