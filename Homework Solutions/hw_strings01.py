#!/usr/bin/env python

"""
hw_strings_01.py

Assignment: Create a program that will prompt the user for a date and convert that date into stardate

Rules for computing stardate.

1. Stardate is a number composed of 4 digits followed by a . and then three more digits.
2. The first four digits are the year the user gave.
3. The number after the period is the percentage of days that have passed in the year. 

Example Dec 01, 2011 would be converted to stardate 2011.91
That is computed by using Dec 1, 2011 is the 335th day of the year and this year has 365 days
So 365/335 = .91 or 91% 

I have added some code to help you compute dates. 

Secondly to do math with decimals you will have to cast your numbers as floats.

I have included an example.

"""

import datetime


def main():

    # Welcome the User
    print("Welcome to Kellan's Stardate Converter")
    
    # Ask the user to enter a date in MM/DD/YYYY format. Store
    # information in userDate variable.
    userDate = raw_input("Enter a date in MM/DD/YYYY format:")

    # Split the string into three variables
    # Converting it to a int while I am at it
    # Next week we will do this with a list and the split function
    month = int(userDate[:2])
    day = int(userDate[3:5])
    year = int(userDate[-4:])
    
    # Find the number of days in the users year
    daysInTheYear = datetime.date(year,12,31).strftime("%j")

    # Find the number of days from Jan 1 to users date.
    daysOfYear = datetime.date(year,month,day).strftime("%j")

    # Find Percentage of year that has passed.
    # Type cast to float to get accurate number
    percentOfYear = (float(daysOfYear) / float(daysInTheYear)) * 100.0

    # Print out Stardate
    print "Stardate: %s.%d" % (year, percentOfYear)


    
    




if __name__ == '__main__':
    main()