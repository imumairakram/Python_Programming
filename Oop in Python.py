#====================== Topic: Object-Oriented Programming (OOP) ======================

# Introduction:
# OOP is a programming paradigm based on the concept of objects.
# Objects can contain both data (attributes) and functions (methods).

#------------------------------------------------------------------------

# 1. Creating a Basic Class with a Method

class Calculator:
    # Method to calculate sum of two numbers
    def calc_sum(self, a, b):
        return a + b

# Creating an object of the Calculator class
calc = Calculator()

# Calling the method through the object
result = calc.calc_sum(5, 7)
print(f"Sum of 5 and 7: {result}")

#------------------------------------------------------------------------

# 2. Using a Constructor to Initialize Objects

class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Person class
person1 = Person("Umair", 19)
person2 = Person("Sara", 25)

# Displaying the details of each person
person1.display()
person2.display()

#------------------------------------------------------------------------

# 3. Class Attributes vs Instance Attributes

class Car:
    wheels = 4  

    def __init__(self, model, color):
        self.model = model  # Instance attribute
        self.color = color  # Instance attribute

    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}, Wheels: {Car.wheels}")

# Creating objects of the Car class
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Displaying information of each car
car1.display_info()
car2.display_info()

#------------------------------------------------------------------------

# 4. Encapsulation (Private Attributes)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount")

    # Method to check balance
    def check_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount("Umair", 1000)

account.deposit(500)
account.withdraw(200)
account.check_balance()

#------------------------------------------------------------------------

# 5. Inheritance (Base and Derived Classes)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

# Derived class (Inheritance)
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()
cat.sound()

#------------------------------------------------------------------------

# 6. Polymorphism (Same Method, Different Implementations)

class Bird:
    def fly(self):
        print("Some birds can fly")

class Eagle(Bird):
    def fly(self):
        print("Eagles soar high in the sky")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Creating objects of Eagle and Penguin classes
eagle = Eagle()
penguin = Penguin()

# Demonstrating polymorphism
eagle.fly()
penguin.fly()

#------------------------------------------------------------------------

# 7. Class Method and Static Method

class Student:
    university = "XYZ University"  

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def get_university(cls):
        return cls.university

    @staticmethod
    def is_adult(age):
        return age >= 18

student = Student("Ali", 101)

print(f"University: {Student.get_university()}")
print(f"Is student an adult? {Student.is_adult(19)}")

#------------------------------------------------------------------------

# 8. Multiple Inheritance

class Father:
    def height(self):
        print("Height: 6 feet")

class Mother:
    def intelligence(self):
        print("High Intelligence")

class Child(Father, Mother):
    def hobby(self):
        print("Loves playing football")

child = Child()

child.height()
child.intelligence()
child.hobby()

#------------------------------------------------------------------------

# 9. Abstraction using Abstract Classes (Using `abc` Module)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

car = Car()

car.start()
car.stop()

#------------------------------------------------------------------------

# 10. Magic Methods (Operator Overloading)

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

result = num1 + num2

print(f"Result of addition: {result}")


