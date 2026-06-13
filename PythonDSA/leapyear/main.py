year = int(input("enter a year "))

if (year % 400 ==0) and (year % 100 ==0):
  print(year, "a Leap year")

elif(year % 4 ==0) and (year % 100 !=0):
  print(year, "a Leap year")
else:
  print("Not a leap year")