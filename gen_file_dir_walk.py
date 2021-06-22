#!/usr/bin/env python3
import os
path=input("PLease provide the path: ")
print("Example 1: ")
print(list(os.walk(path)))
print("---------------")
print("Example 2: ")
for r,d,f in os.walk(path):
    if len(f) !=0:
        print("Path which have files are: ")
        print(r)
        for each_file in f:
            print("file name: ", each_file)
            print("full path: ", os.path.join(r,each_file))
