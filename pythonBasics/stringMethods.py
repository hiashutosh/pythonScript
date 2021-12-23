#!/usr/bin/env python

# Referemce https://www.w3schools.com/python/python_strings_methods.asp

import os

term_len=os.get_terminal_size().columns
new_line = '#' * term_len

###########
# .lower() .upper()
############
print(new_line)

txt = "Hello my FRIENDS"

print(txt.lower())
print(txt.upper())

###########
# .join()
############
print(new_line)

myTuple = ("John", "Peter", "Vicky")
x = " & ".join(myTuple)
print(x)

###########
# .split()
############
print(new_line)

txt = "welcome to the jungle"
x = txt.split("e")
print(x)


#########
# .find() .count()
############
print(new_line)

string = "hello I am ashutosh"
print(string.find('a'))
print(string.count('a'))