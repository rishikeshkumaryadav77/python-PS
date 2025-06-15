# find prime number
#   if a % i == 0:
#     val += 1
# if val == 0:
#   print("prime")
# else:
#   print("not a prime")
# # print("hko")


##find prime number and sum of prime number
# a = "4137"
# num = 0
# for i in a:
#   if int(i)>1:
#     val =0
#     for j in range (2, (int(i)//2)+1):
#       if int(i)% j == 0:
#         val +=1
#         break
#     if val == 0:
#       num += int(i)
# print(num)

##find sum of prime number and sum of non-prime number
# a = "4137"
# prime = 0
# non_prime = 0

# for i in a:
#   if int(i)>1:
#     val =0
#     for j in range (2, (int(i)//2)+1):
#       if int(i)% j == 0:
#         val += 1 
#         break
#     if val == 0:
#       prime += int(i)
#     else:
#       non_prime += int(i)
#   else:
#     non_prime += int(i)
# print("sum of prime number {}".format(prime))
# print("sum of non-prime number {}".format(non_prime))



##.capitalize() method
print("i love you".capitalize())   
## o/p I Love  You



##nearest prime number
# num = int(input("enter number: "))
# #function
# def isPrime(n):
#     if n > 1:
#         for i in range(2, (n//2)+1):
#             if n % i == 0:
#                 return False
        
#         return True
        
# if(isPrime(num)):
#     print("It is prime number")
# else:
#     lp,rp=num-1,num+1
#     while True:
#         if(isPrime(lp)):
#             break
#         lp -= 1
#     while True:
#          if(isPrime(rp)):
#             break
#          rp +=1
#     res =lp if(num - lp) < (rp-num) else rp
#     print(res)


###prime vs non prime
a = "43125"
non_prime =[]
prime= []
for i in a:
    if int(i)>1:
        is_prime = True
        for j in range(2, int(i)):
            if int(i) % j ==0:
                is_prime = False
                break
        if  is_prime:
            prime.append(i)
        else:
            non_prime.append(i)
    else:
        non_prime.append(i)
print("prime", prime)
print("non-prime", non_prime)
                