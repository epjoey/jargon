#!/usr/bin/env python

"""
hw_strings_02.py

Assignment: Create a program that will prompt the user for a string. Take the
string input by the user. Output the sting in side a box that is centered on 
the screen. Use an 80 column screen for this example. Look at the example from
class on how to draw a box. There are many more ways to solve this problem than
the way I presented in the example.

Use the built in len function to determin the lenght of the string.
Also your box is not limited to using the characters I chose for my box. You 
might find it easier to use all * characters for example. 

"""

def main():
	# Set system paramaters
	SCREENWIDTH = 80
	BOXPADDING = 2
	BOXCHAR = '*'

	# Ask user for a string
	userString = raw_input('Please enter a string:')

	# See how long the string is.
	stringSize = len(userString)
	# Compute the size of the box
	boxSize = stringSize + BOXPADDING * 2 + 2
	# Set the left side padding
	leftPadding = (SCREENWIDTH - boxSize) / 2

	# Print the box
	print ' ' * leftPadding + BOXCHAR * boxSize
	print ' ' * leftPadding + '*' + ' ' * (boxSize - 2) + BOXCHAR
	print ' ' * leftPadding + BOXCHAR + ' ' * BOXPADDING + userString + ' ' * BOXPADDING + BOXCHAR
	print ' ' * leftPadding + '*' + ' ' * (boxSize - 2) + BOXCHAR
	print ' ' * leftPadding + BOXCHAR * boxSize








if __name__ == '__main__':
    main()