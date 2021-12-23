#!/usr/bin/python3
# import csv
c_file=input("Enter your File with path: ")

f=open(c_file,'w')
# f = open('file.txt', 'r')
fo = f.readlines()
newList = []
for line in fo:
    newList.append(line.strip())

print(newList)