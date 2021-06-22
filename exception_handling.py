#!/usr/bin/env python3
import os
print("current working dir: ", os.getcwd())
dir_path=input("Enter dir path to change working dir: ")
try:
    os.chdir(dir_path)
    print("Now your current working dir: ", os.getcwd())
except FileNotFoundError:
    print("not a valid path")
except NotADirectoryError:
    print("not a dir path")
except PermissionError:
    print("not have permisiion")
except Exception as e:
    print(e)