#!/usr/bin/python3 

'''
print("Hello World")
print("welcome to python scripting")
x=4.6869696914213123
print(x)
print(type(x))
print(id(x))
y=3+4j
print(y,type(y),id(y))
'''
print("comment")
my_value=True
print(my_value)



import os
from typing import NamedTuple, OrderedDict

term_len=os.get_terminal_size().columns
new_line = '#' * term_len
########
# For loop
########
print(new_line)

for x in range(1,4):
    print(x)

###########
# While Loop
############
print(new_line)

# value = "random"
# while value != "exit":
#     value = input("still in while, enter 'exit' to quit ")

###########
# List
############
print(new_line)

fruits = ['apple', 'pear', 'strawberry']
print(fruits)
print(fruits[1])
fruits.append('orange')
print(fruits)
print(fruits[1:3])
print(fruits[2:])
fruits.sort()
print(fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "n" in x:
    newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

##########
# Modules
#########
print(new_line)

import math
print(math.pi)
print(math.radians(60))

import custModule1
print(custModule1.add(10,2))

import modules.custModule2
print(modules.custModule2.sub(12))

# ##########
# # try and except
# #########
# print(new_line)

# text = input("Number: ")
# try:
#     num = int(text)
#     print("valid number: ", num)
# except: 
#     print("invalid number: ", text)

##########
# Map() function
#########
print(new_line)

li = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x**x

# # Tradional Method
# newLi = []
# for x in li:
#     newLi.append(func(x))
# print(newLi)

# # using map() function
# newList = list(map(func,li))
# print(newList)

# # List comprehension
# print([func(x) for x in li ])
# print([func(x) for x in li if x%2 ==0 ])

##########
# filter function
#########
print(new_line)

def add7(x):
    return x+7

def isOdd(x):
    return x&2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isOdd,a))
print(b)
c = list(map(add7, b))
print(c)


##########
# lambda function
#########
print(new_line)

func1 = lambda x: x+5
print(func1(6))
func2 = lambda x,y: x+y
print(func2(5,9))

a = [1,2,3,4,5,6,7,8,9,10]
new_list = list(map(lambda x: x+7, a))
print(new_list)

##########
# collections
#########
print(new_line)

# Collections
# list
# set
# dict
# tuple

# Types
# Counter
# deque
# NamedTuple
# orderedDict
# defaultdict


from collections import Counter

a = Counter('gallad')
print(a)
b = Counter(['a', 'b', 'c', 'a', 'c'])
print(b)
c = Counter({'a':1, "b":2})
print(c)
d = Counter(cats=4, dogs=7)
print(d)
print(list(d.elements()))
print(b.most_common(2))

b.subtract(c)
print(b)
b.update(d)

d.clear()
print(d)

print(b & c)
print(b | c)


print(new_line)

from collections import namedtuple

Point1 = namedtuple('Point1', 'x y z')
Point2 = namedtuple('Point2', ['x', 'y', 'z'])
Point3 = namedtuple('Point3', {'x':1, 'y':2, 'z': 4})

p1 = Point1(3,2,5)
print(p1)

p2 = Point2(2,3,4)
print(p2)

p3 = Point3(5,2,6)
print(p3)

print(p1.y, p2.y, p3.y)
print(p1[0])
print(p3._asdict())

print(p3._fields)

p3 = p3._replace(y=6)
print(p3)

p4 = Point3._make(['a', 'b', 'c'])
print(p4)


print(new_line)

from collections import deque

d = deque("hello")
print(d)

d.append('4')
d.appendleft('y')
print(d)

d.pop()
d.popleft()
print(d)

d.extend('Iam')
print(d)

d.rotate(3)
print(d)

e = deque("hello", maxlen=5) 
e.extend('add')
print(e)
