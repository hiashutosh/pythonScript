#!/usr/bin/env python3
import os
import sys
def val_dir():
    f_d_dir=os.listdir(path)
    if len(f_d_dir) == 0:
        print(f"{path} is empty")
    else:
        ext_func(f_d_dir)
def ext_func(f_d_dir):
    file_ext=input("Enter ext to be search: ")
    files = []
    for each_file in f_d_dir :
        if each_file.endswith(file_ext):
            files.append(each_file)
    if len(files) == 0:
        print(f"No files with \"{file_ext}\"")
    else:
        print(f"There are {len(files)} files in {path} directory")
        print(f"Files with extention \"{file_ext}\" are: ")
        for item in files:
            print(item)
path=input("Enter a directory: ")
if os.path.exists(path):
    val_dir()
else:
    print(f"{path} is not a valid directory")
    sys.exit()


