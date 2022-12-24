# Write a program add.py that takes 2 numbers as command line arguments and prints its sum.

""" to use commend line arguments we need to import library to access the OS (oprating system command line)
On command line/ terminal we just need to run python add.py 5 6
here we can take any number inted of 5 and 6"""

# note save file by name add.py


import sys #importing library system

x = int(sys.argv[1])
y = int(sys.argv[2])
add = x+y
print("Add= ",add)
