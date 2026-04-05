s = "A man, a plan, a canal: panama"
res = ''
for char in s:
  if char.isalnum():
    res += char.lower()
if res == res[::-1]:
  print("palindrome")
else:
  print("not a palindrome")
