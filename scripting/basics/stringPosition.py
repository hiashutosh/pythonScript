#!/usr/bin/python3 
import os
cols=os.get_terminal_size().columns
given_str=input("Enter your string: ")

print(given_str.center(100))

print(given_str.ljust(cols))

print(given_str.rjust(cols).title())
