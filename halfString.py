a = input()
length = len(a)/2
half_word = int(length)
word = a[:half_word]
print(word)

##-------------------------------------
#skip the fourth charector
#i/p :- equality
#o/p:- equlity
a = input()
starting_index = a[:3]
last_index = a[4:]
word = starting_index + last_index
print(word)
##-------------------------------------------------
##find the percentage of 70% of given input()
a = int(input())
b = (70 / 100) * a
print(b)

##-------------------------------------------------
# Area of the square 
# Perimeter of the square of the perimeter

a = input()
a = int(a)
c = int(a * a)
d = 4 * a
print("Area of the square is:"  ,c)
print("Perimeter of the square is:" , d)

##--------------------------------------------
##replace the letter of the given index and add letter of the given
a = input()
number = int(input())
sub_c = input()
first_index = a[:number]
last_index = sub_c + a[number+1:]
print(first_index + last_index)
