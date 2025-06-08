# num = [int(i) for i in input("enter num: ").split()]
# print(num)
# for i in num:
#   print(i)

## i/p ("i love india") o/p ['i', 'love', 'india']

text = "i love india"
word = ""
words = []
for i in text:
  if i != " ":
    word += i
  else:
    words.append(word)
    word= ""
if(words):
  words.append(word)
print(words)
