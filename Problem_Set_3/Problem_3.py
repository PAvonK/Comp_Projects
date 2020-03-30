# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:17:30 2020

@author: pavk1


Problem 3 - Printing Out all Available Letters

Next, implement the function getAvailableLetters that takes in one parameter -
 a list of letters, lettersGuessed. This function returns a string that is
 comprised of lowercase English letters - all lowercase English letters that
 are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as
in the example above.

For this function, you may assume that all the letters in lettersGuessed are
lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string
comprised of all lowercase letters:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz

"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far returns:
    string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    baseString = string.ascii_lowercase
    print(baseString)
    for char in lettersGuessed:
        tempString = baseString.replace(char, "")
        baseString = tempString
        print(baseString)
    return baseString
    

print(getAvailableLetters(['e']))
