#!/usr/bin/env python3
import csv
c_file=input("Enter your File with path: ")

fo=open(c_file,'r')
data=csv.reader(fo,delimiter=",")
for each in data:
    print(each)
fo.close()