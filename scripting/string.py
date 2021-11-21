#!/usr/bin/python3 
import os
cols=os.get_terminal_size().columns
given_str=input("Enter your string: ")
print(given_str.center(102))
print(given_str.ljust(102))
print(given_str.rjust(102))
print(given_str.center(cols))
print(given_str.ljust(cols))
print(given_str.rjust(cols))

print(given_str.center(cols).title())
print(given_str.ljust(cols).title())
print(given_str.rjust(cols).title())