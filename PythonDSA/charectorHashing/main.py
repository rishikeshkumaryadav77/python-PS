s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]
set_q = {}
for char in q:
  if char in s:
    set_q[char] = s.count(char) #//one way
    
  else:
    set_q[char] =0

print(set_q)
