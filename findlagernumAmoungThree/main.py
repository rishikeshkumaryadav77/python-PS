# /*find larger num among three number*/
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
"Three are Equal" if num1==num2 and num2 ==num3 else "num1" if num1>num2 and num1>num3 else "nu2" if num2>num3 else "num3"


# /* find larger num given input= 5634*/
input = "5634"
# print(len(input)+1)
res = input[0]
for i in range(1, len(input)):
    # print(input[i])
    if (input[i] > res):
        
        res = input[i]
    
    
print(int(res))