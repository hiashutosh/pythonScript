#!/usr/bin/env python3
import os
import time
import platform
def myfunc(cmd1,cmd2):
    print("Please wait. clearing the screen......")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait finding the list of dir and files: ")
    time.sleep(2)
    os.system(cmd2)
if platform.system()=="Windows":
    myfunc("cls","dir")
else:
    myfunc("clear","ls -lrt")
