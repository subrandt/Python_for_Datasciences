"""
Educational goal:
Learn to handle command-line arguments with sys.argv and validate user input.

This script takes a number as argument and checks if it's odd or even.
"""

import sys 

if len(sys.argv) == 1:
    # No argument provided: do nothing (exit silently)
    pass

elif len(sys.argv) == 2:

    try:
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
            
    except ValueError:
        print("AssertionError: argument is not an integer")

else:
    print("AssertionError: more than one argument is provided")