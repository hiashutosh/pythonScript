#!/usr/bin/env python3
import os
import time
import platform
if platform.system()=="Windows":
    print("Please wait. clearing the screen......")
    time.sleep(2)
    os.system("cls")
    print("Please wait finding the list of dir and files: ")
    time.sleep(2)
    os.system("dir")
else:
    print("Please wait. clearing the screen......")
    time.sleep(2)
    os.system("clear")
    print("Please wait finding the list of dir and files: ")
    time.sleep(2)
    os.system("ls -lrt")