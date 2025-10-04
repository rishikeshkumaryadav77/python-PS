# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# for i in sentences:
#   for j in sentences:
#     if len(i) <= len(j):
#       large_sen = j
# # sentences = large_sen.split()
# count = 1
# for i in large_sen:
#   if i == " ":
#     count += 1
# print(count)

for i in range(3):
  for j in range(3):
    print("*", end="")
    if j !=2:
      print("_", end ="")
  print()

  