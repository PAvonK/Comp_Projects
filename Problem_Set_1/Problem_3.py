# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:30:37 2020

@author: pavk1

Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you 
move on to a different part of the course. If you have time, come back to this 
problem after you've had a break and cleared your head.

"""

s = 'azcbobobegghakl'
# Set's s to the string.
long = 0
length = 0
result = 0
# Creates the variables of long, length, and result with the starting values
#   of 0
for char in range(len(s) -1):
#   Sets the 'for' loop to run on each character equal to the number of 
#   characters in the length of the string(s)
    if (s[char] <= s[char + 1]):
    # starting at the first index this basically each letter in the string to
    #   The one after to see if the one after is greater than or equal to it
        long += 1
        #   If true it adds that digit and increases the long by 1 which is
        #   that same number
        if long > length:
            length = long
            # This next section says that if the the new long in greater than
            # the previous longest which is recorded in length than to replace
            # the previous length with the new long
            result = char + 1
            #This adds one to the result for tracking I think...
    else:
        long = 0
        # this says that if the new character is less than the previous
        # and sets log to start back at zero to try again.
longstring = result - length
print('Longest substring in alphabetical order is:', s[longstring:result + 1])