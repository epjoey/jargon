#!/usr/bin/env python

"""
list_example.py
Examples that will be used in showing lists in python. 
Created by Kellan Jacobs on 2011-12-10.
"""

def main():
    # Create a list of numbers 1 - 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

    # Show the list we are starting with. Note the comma at the end. I used
    # this because simple print can't add a list to a string and I wanted
    # them to print on the same line.
    print "Print the list:",
    print numbers

    # Slicing works for lists too
    print 'Slicing works:',
    print numbers[3:5]

    # Print every other item in a list
    print 'Print Every other item:',
    print numbers[::2]

    # Print the evens
    print 'Print the Even numbers:',
    print numbers[1::2]


if __name__ == '__main__':
    main()