num = 9
sqr = num **2
sum_digit = 0
while sqr > 0:
    digit = sqr % 10
    print(digit)
    sum_digit += digit
    sqr = sqr // 10
    print(sqr)
print(sum_digit)
    