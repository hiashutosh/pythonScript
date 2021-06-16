#!/usr/bin/env python3
import os
import datetime
import sys
def file_age(path_file):
    today=datetime.datetime.now()
    create_time=datetime.datetime.fromtimestamp(os.path.getctime(path_file))
    ageis=(today-create_time).days
    return ageis

def file_created(file_dir):
    files=os.listdir(file_dir)

    for each_file in files:
        path_file=os.path.join(file_dir,each_file)
        if os.path.isfile(path_file):
            create_time=datetime.datetime.fromtimestamp(os.path.getctime(path_file))             
            ageoffile=file_age(path_file)
            print(f"{path_file} created on {create_time} age: {ageoffile} days")
    remove=input("Want to remove above files [y/n]: ")
    if remove == 'y':
        age=input("Enter the age of file to find: ")
        for each_file in files:
            path_file=os.path.join(file_dir,each_file)
            files_age=file_age(path_file)
            if files_age >= int(age):
                os.remove(path_file)
    else:
        sys.exit(1)


def main():
    print("This script finds the files of certain age")
    file_dir=input("Enter the directory: ")
    if os.path.exists(file_dir):
        file_created(file_dir)
    else:
        print("Directory not exists")
        sys.exit(0)

main()
