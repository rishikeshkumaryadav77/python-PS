# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def degination(self, position):
#         self.position = position
#         print("My position is", position)

# class Pno(Human):
#     def __init__(self, name, age, Pno):
#         # Call the parent class constructor
#         super().__init__(name, age)
#         self.Pno = Pno
#         # Call the parent class method
#         # self.degination("hr")
#         super.degination()
#     def degination(self, position):
#         return self.position

# # Creating an instance of Pno
# obj2 = Pno("Rishi", 20, 77808766)

# print(obj2.degination("hr"))


class Parent:
    def show(self):
        
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        
        print("This is Child class method")
        super().show()  # Calling the Parent class method using super()

# Creating an object of the Child class
obj = Child()
obj.show()


#methods and constructor
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

    def greet(self):
        print(f"Hello, {self.name}! Greetings from Parent class.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling Parent's constructor
        self.age = age
        print("Child constructor called")

    def greet(self):
        print(f"Hello, {self.name}! Greetings from Child class.")
        super().greet()  # Calling Parent's greet method

# Creating an object of Child class
obj = Child("Rishi", 20)
obj.greet()