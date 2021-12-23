#!/usr/bin/env 
import os
import sys
def test_func():
    f_d_dir=os.listdir(path)
    if len(f_d_dir) == 0:
        print(f"{path} is empty")
    else:
        for each in f_d_dir:
            path_to=os.path.join(path,each)
            if os.path.isfile(path_to):
                print(f"{path_to} is a file")
            else:
                print(f"{path_to} is a directory")

path=input("Enter a directory: ")
if os.path.exists(path):
    test_func()
else:
    print(f"{path} is not a valid directory")
    sys.exit()


