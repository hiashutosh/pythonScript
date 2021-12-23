#!/usr/bin/env python3

def add(x , y):
    return x + y

def sub(x , y = 0):
    return x - y

print("Enter two numbers: ")
x = int(input("x: "))
y = int(input("y: "))

print("y+x=", add(x,y))
print("x-y=", sub(x,y))