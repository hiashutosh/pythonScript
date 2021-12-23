#!/usr/bin/env python
import os

term_len=os.get_terminal_size().columns
new_line = '#' * term_len


######
# Creating class
######
# print(new_line)

# class Dog(object):
#     def __init__(self):
#         print('Nice you name a dog')
    
#     def speak(self):
#         pass

# tim = Dog()

# ###########
# print(new_line)

# class Dog(object):
#     def __init__(self, name, age='1'):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age, "years old")

#     def add_weight(self, weight):
#         self.weight = weight

# tim = Dog('Tim')
# fred = Dog('Fred', '3')
# tim.speak()
# fred.speak()
# tim.add_weight(70)
# print(tim.age)
# print(tim.weight)
# print(fred.weight)

###########
# Inheritence
###########
# print(new_line)

# class Dog(object):
#     def __init__(self, name, age='1'):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age, "years old")

#     def add_weight(self, weight):
#         self.weight = weight
    
#     def talk(self):
#         print('Bark!')

# class Cat(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age=age)
#         self.color = color
    
#     def talk(self):
#         print("Meow!")

# tim = Cat ('tim', 5 ,'black')
# tim.speak()
# tim.talk()


#### default class

# class Vehicle():
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color = color
    
#     def fillUpTalk(self):
#         self.gas = 100
#     def emptyTank(self):
#         self.gas = 0
#     def gasLeft(self):
#         return self.gas

# class Car(Vehicle):
#     def __init__(self, price, gas, color, speed):
#         super().__init__(price, gas, color)
#         self.speed = speed
    
#     def beep(self):
#         print("Beep Beep")

# class Truck(Vehicle):
#     def __init__(self, price, gas, color, tyre):
#         super().__init__(price, gas, color)
#         self.tyre = tyre

#     def beep(self):
#         print("Honk Honk")

# car1 = Car ('1000', 10, 'blue', 100)
# truck1 = Truck ('2000', 20 ,'black', 12)

# print(car1.beep(), car1.gasLeft())
# print(truck1.beep(), truck1.gasLeft())

#########
# Overriding Method
# ref https://web.archive.org/web/20200529000722/http://www.siafoo.net/article/57
#########
# print(new_line)

# class Point():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         self.coords = (self.x, self.y)
    
#     def move(self, x, y):
#         self.x += x
#         self.y += y

#     def __add__(self,p):
#         return Point(self.x + p.x, self.y + p.y)
    
#     def __sub__(self, p):
#         return Point(self.x - p.x, self.y - p.y)
    
#     def __mul__(self, p):
#         return self.x * p.x + self.y + p.y

#     def __str__(self):
#         return "(" +str(self.x) + ',' + str(self.y) + ')'
    
#     def length(self):
#         import math
#         return math.sqrt(self.x**2 + self.y**2)

#     def __eq__(self, p) -> bool:
#         return self.length() == p.length()

#     def __lt__(self, p):
#         return self.length() < p.length()

# p1 = Point(3,4)
# p2 = Point(3,2)
# p3 = Point(1,3)
# p4 = Point(-1,3)
# p5 = p1 + p2
# p6 = p1 - p2
# p7 = p1 * p2
# print(p3 == p4)
# print(p2 - p1)
# print(p6)
# print(p7)
# print(p1 < p2)

#########
# Static Methods and Class Methods
#########
# print(new_line)

# class Dog:
#     # This is used with all instances which call class Dog
#     dogs = []

#     def __init__(self, name):
#         self.name = name
#         self.dogs.append(self)

#     @classmethod
#     def num_dogs(cls):
#         return len(cls.dogs)
# # static method are just functions which can be called with the help of class
# # they are used to easily import and organise func
#     @staticmethod
#     def bark(n):
#         for i in range(n):
#             print("bark")

# print(Dog.num_dogs())
# tim = Dog('tim')
# print(tim.num_dogs())
# fred = Dog('fred')
# print(tim.num_dogs())
# print(Dog.num_dogs())
# print(tim.num_dogs())
# Dog.bark(2)

#########
# Private and Public classes
# ref https://web.archive.org/web/20200529000722/http://www.siafoo.net/article/57
#########
# print(new_line)

## importing from modules/mod.py

# import mod

# from mod import NotPrivate

# test = NotPrivate('tim')

# test.display()
# test._display()