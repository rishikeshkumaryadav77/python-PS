#static variable and instance variable
#class
# class Human:
#   specification = "humanbeing"   #static variable (it can call with help of class name and object)
#   def __init__(self, name, age, pno):   #constructor
#     self.name = name   #instance variable
#     self.age = age    #instance variable
#     self.pno = pno    #instance variable   (it can call only with object)

#   def setNmae(self, newName):
#     self.name = newName
#     print(self.name)

# #object
# person1 = Human("rishi", 20, 7780755042)
# # print(person1.pno)

# person1.setNmae("rishiroy")
# # print(person1.name)  #after updated name

# print(person1.specification)  #stactic variable
# print(Human.name)  #instance variable  can't call with class name


#----------------------------------------------instance method
#static methos, instance method, class method

#class
# class Human:
#   specification = "humanbeing"   #static variable (it can call with help of class name and object)
#   def __init__(self, name, age, pno):   #constructor
#     self.name = name   #instance variable
#     self.age = age    #instance variable
#     self.pno = pno    #instance variable   (it can call only with object)

#   def setNmae(self, newName): #instance method
#     self.name = newName
#     print(self.name)

#   @staticmethod
#   def staticMethod(self, newName):
#     self.specification = newName
#     print(self.specification)

# #object
# person1 = Human("rishi", 20, 7780755042)


#-------------------------------classmethod
class Student:
    school = "ABC High School"  # Class variable (static variable)

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):  # Class method
        cls.school = new_school  # Modifies class variable

# Calling class method
Student.change_school("XYZ Academy")

# Creating objects
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)  # Output: XYZ Academy
print(s2.school)  # Output: XYZ Academy
print(Student.name) #instance can't call with classname

#----------------------------------static method
# class MathUtils:
#     @staticmethod
#     def add(a, b):  # Static method
#         return a + b

# # Calling static method without creating an instance
# result = MathUtils()

# print("Sum:", result.add(8, 5))  # Output: Sum: 15





#----------------------------------------------------
# class Car:
#   def __init__(self, car, modal):
#     self.car=car
#     self.modal=modal

# # creaated new function
#   def full_name(self, year):
#     return f"{self.modal} {self.car} {year}"
  
# # accessing super class
# class ElectricVehicle(Car):
#   def __init__(self, car, modal, battery_storage):
#     super().__init__(car, modal)
#     self.battery_storage = battery_storage

  
# car_obj = Car("honda", "2022M")
# print(car_obj.car)

# # print(car_obj.full_name("2021"))

# electric_obj = ElectricVehicle("tesla", "30s", "30kmph")
# print(electric_obj.car)


# -----------------------------
# plymorphism
# class name:
#   def myName(self):
#     print("my name rishi")

# class kumar(name):
#   def myName(self):
#     super().myName()
#     print("my name is rishi kumar")

# obj = kumar()
# obj.myName()


